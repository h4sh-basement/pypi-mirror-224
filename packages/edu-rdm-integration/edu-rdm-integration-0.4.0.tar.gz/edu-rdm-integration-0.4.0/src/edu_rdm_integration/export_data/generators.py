from datetime import (
    date,
    datetime,
    time,
)
from typing import (
    Iterable,
    List,
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
from edu_rdm_integration.models import (
    RegionalDataMartEntityEnum,
)


class BaseFirstExportEntitiesDataCommandsGenerator:
    """Класс, который генерирует список данных для формирования команд для экспорта данных РВД."""
    def __init__(
        self,
        entities: Iterable[str],
        period_started_at=datetime.combine(date.today(), time.min),
        period_ended_at=datetime.combine(date.today(), time.min),
        batch_size=consts.BATCH_SIZE,
        **kwargs,
    ):
        """Инициализация."""
        # Если сущности не указаны, берется значение по умолчанию - все сущности:
        entities = entities if entities else RegionalDataMartEntityEnum.get_enum_data().keys()
        self.entities: List[ModelEnumValue] = [
            RegionalDataMartEntityEnum.get_model_enum_value(entity) for entity in entities
        ]

        self.period_started_at = period_started_at
        self.period_ended_at = period_ended_at

        self.batch_size = batch_size

        self.get_logs_periods_sql = (
            """
            select min(modified),
                   max(modified),
                   row_batched
            from (
                select row_num,
                       ((row_num - 1) / {batch_size}) + 1 AS row_batched,
                       modified
                from (
                    select row_number() over (order by modified) as row_num,
                           modified
                    from (
                        select *
                        from (
                        {ordered_rows}
                        ) as union_rows
                        order by modified
                    ) as ordered
                ) as numbered
            ) as batched
            group by row_batched
            order by row_batched;
            """
        )

        self.ordered_rows_query = (
            """
            select modified
            from {table_name}
            where modified between '{period_started_at}' and '{period_ended_at}'
            """
        )

    def generate(self) -> List:
        """Генерирует список данных для формирования команд для экспорта данных РВД."""
        params_for_commands = []

        for entity in self.entities:
            ordered_rows_queries_sql = self.ordered_rows_query.format(
                table_name=entity.main_model._meta.db_table,
                period_started_at=self.period_started_at.strftime(consts.DATE_FORMAT),
                period_ended_at=self.period_ended_at.strftime(consts.DATE_FORMAT),
            )

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
                        'entity': entity.key,
                    }
                )

        return params_for_commands
