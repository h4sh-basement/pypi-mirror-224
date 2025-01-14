from datetime import (
    date,
    datetime,
    time,
)
from typing import (
    TYPE_CHECKING,
    Iterable,
    List,
    Optional,
    Tuple,
)

from django.apps import (
    apps,
)
from django.db import (
    connection,
)

from m3_db_utils.models import (
    ModelEnumValue,
)

from edu_rdm_integration import (
    consts,
)
from edu_rdm_integration.consts import (
    DATE_FORMAT,
)
from edu_rdm_integration.models import (
    RegionalDataMartModelEnum,
)
from edu_rdm_integration.utils import (
    split_by_academic_years,
    split_interval_by_delta,
)


if TYPE_CHECKING:
    from educommon.audit_log.models import (
        AuditLog,
    )


class BaseEduLogGenerator:
    """
    Базовый класс генератора логов для указанной модели РВД за определенный период времени.

    Для каждой модели РВД есть модели в продукте, создание экземпляров которых, сигнализирует о необходимости сбора
    и выгрузки данных в РВД. Модели можно найти в
    edu_rdm_integration/mapping.py MODEL_FIELDS_LOG_FILTER, принадлежность к конкретной
    модели РВД необходимо определять в функциях.
    """

    def generate(
        self,
        model: ModelEnumValue,
        logs_period_started_at: datetime = datetime.combine(date.today(), time.min),
        logs_period_ended_at: datetime = datetime.combine(date.today(), time.max),
        school_ids: Optional[Tuple[int]] = (),
    ) -> List['AuditLog']:
        """
        Возвращает список сгенерированных экземпляров модели AuditLog.

        Формирование логов производится для указанной модели РВД за указанный период времени.

        Args:
            model: значение модели РВД из модели-перечисления;
            logs_period_started_at: начало периода формирования логов;
            logs_period_ended_at: конец периода формирования логов;
            school_ids: список идентификаторов школ.
        """
        generate_logs_method = getattr(self, f'_generate_{model.key.lower()}_logs')

        logs = generate_logs_method(
            logs_period_started_at=logs_period_started_at,
            logs_period_ended_at=logs_period_ended_at,
            school_ids=school_ids,
        )

        return logs


class BaseFirstCollectModelsDataCommandsGenerator:
    """Класс, который генерирует список данных для формирования команд для сбора данных РВД."""

    def __init__(
        self,
        models: Iterable[str],
        logs_period_started_at=datetime.combine(date.today(), time.min),
        logs_period_ended_at=datetime.combine(date.today(), time.min),
        logs_sub_period_days=consts.LOGS_SUB_PERIOD_DAYS,
        batch_size=consts.BATCH_SIZE,
    ):
        """Инициализация."""
        # Если модели не указаны, берется значение по умолчанию - все модели:
        models = models if models else RegionalDataMartModelEnum.get_enum_data().keys()
        self.regional_data_mart_models: List[ModelEnumValue] = [
            RegionalDataMartModelEnum.get_model_enum_value(model) for model in models
        ]

        self.logs_period_started_at = logs_period_started_at
        self.logs_period_ended_at = logs_period_ended_at
        self.logs_sub_period_days = logs_sub_period_days

        self.batch_size = batch_size

        # Правую дату нужно увеличивать на одну секунду, т.к. подрезались миллисекунды
        self.get_logs_periods_sql = (
            """
            select min(created),
                   max(created)  + interval '1 second',
                   row_batched
            from (
                select row_num,
                       ((row_num - 1) / {batch_size}) + 1 AS row_batched,
                       created
                from (
                    select row_number() over (order by created) as row_num,
                           created
                    from (
                        select *
                        from (
                        {ordered_rows}
                        ) as union_rows
                        order by created
                    ) as ordered
                ) as numbered
            ) as batched
            group by row_batched
            order by row_batched;
            """
        )

        self.ordered_rows_query = (
            """
            select distinct date_trunc('second', created) as created
            from {table_name}
            where created between '{period_started_at}' and '{period_ended_at}'
            """
        )

    def generate(self) -> List:
        """Генерирует список данных для формирования команд для сбора данных РВД."""
        params_for_commands = []

        for rdm_model in self.regional_data_mart_models:
            # Если подпериод указан, то формируется список с разбиением по logs_sub_period_days
            if self.logs_sub_period_days:
                # Получаем интервалы учебных годов
                academic_year_intervals = split_by_academic_years(
                    self.logs_period_started_at, self.logs_period_ended_at
                )

                for academic_year_start_datetime, academic_year_end_datetime in academic_year_intervals:
                    intervals_by_delta = split_interval_by_delta(
                        academic_year_start_datetime, academic_year_end_datetime, self.logs_sub_period_days
                    )
                    for start_datetime, end_datetime in intervals_by_delta:
                        params_for_commands.append(
                            {
                                'period_started_at': start_datetime,
                                'period_ended_at': end_datetime,
                                'model': rdm_model.key,
                                'logs_sub_period_days': self.logs_sub_period_days,
                            }
                        )

            # Если подпериод не указан, то формируется список с разбиением по batch_size
            else:
                ordered_rows_queries = [
                    self.ordered_rows_query.format(
                        table_name=model._meta.db_table,
                        period_started_at=self.logs_period_started_at,
                        period_ended_at=self.logs_period_ended_at,
                    )
                    for model in rdm_model.creating_trigger_models
                ]

                if hasattr(rdm_model, 'plugins_info'):
                    for app_name, app_models in rdm_model.plugins_info.items():
                        if apps.is_installed(app_name):
                            for app_model in app_models:
                                model = apps.get_model(app_model)
                                if model:
                                    ordered_rows_queries.append(
                                        self.ordered_rows_query.format(
                                            table_name=model._meta.db_table,
                                            period_started_at=self.logs_period_started_at.strftime(DATE_FORMAT),
                                            period_ended_at=self.logs_period_ended_at.strftime(DATE_FORMAT),
                                        )
                                    )

                ordered_rows_queries_sql = 'union'.join(ordered_rows_queries)

                temp_get_logs_periods_sql = self.get_logs_periods_sql.format(
                    batch_size=self.batch_size,
                    ordered_rows=ordered_rows_queries_sql,
                )

                with connection.cursor() as cursor:
                    cursor.execute(temp_get_logs_periods_sql)
                    rows = cursor.fetchall()

                for period_started_at, period_ended_at, batch_number in rows:
                    params_for_commands.append(
                        {
                            'period_started_at': period_started_at,
                            'period_ended_at': period_ended_at,
                            'model': rdm_model.key,
                            'logs_sub_period_days': self.logs_sub_period_days,
                        }
                    )

        return params_for_commands
