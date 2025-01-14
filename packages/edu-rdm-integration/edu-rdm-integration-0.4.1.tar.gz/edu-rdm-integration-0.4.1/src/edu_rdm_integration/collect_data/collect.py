from datetime import (
    date,
    datetime,
    time,
    timedelta,
)
from typing import (
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
    Type,
)

from django.db.models import (
    F,
    Max,
)
from django.utils import (
    timezone,
)
from m3.db import (
    BaseEnumerate,
)

from educommon import (
    logger,
)
from educommon.audit_log.models import (
    AuditLog,
)
from educommon.utils.date import (
    get_today_min_datetime,
)
from function_tools.managers import (
    RunnerManager,
)
from m3_db_utils.consts import (
    DEFAULT_ORDER_NUMBER,
)
from m3_db_utils.models import (
    ModelEnumValue,
)

from edu_rdm_integration.app_settings import (
    RDM_TRANSFER_TASK_TIMEDELTA,
)
from edu_rdm_integration.consts import (
    LOGS_SUB_PERIOD_DAYS,
    REGIONAL_DATA_MART_INTEGRATION_COLLECTING_DATA,
)
from edu_rdm_integration.models import (
    CollectingDataSubStageStatus,
    CollectingExportedDataSubStage,
    RegionalDataMartModelEnum,
)
from edu_rdm_integration.signals import (
    manager_created,
)
from edu_rdm_integration.storages import (
    RegionalDataMartEntityStorage,
)


class BaseCollectModelsData:
    """Базовый класс сбора данных моделей РВД."""

    def __init__(
        self,
        models: Iterable[str],
        logs_period_started_at=datetime.combine(date.today(), time.min),
        logs_period_ended_at=datetime.combine(date.today(), time.min),
        **kwargs,
    ):
        # Если модели не указаны, берется значение по умолчанию - все модели:
        models = models if models else RegionalDataMartModelEnum.get_enum_data().keys()
        self.models: List[ModelEnumValue] = [
            RegionalDataMartModelEnum.get_model_enum_value(model) for model in models
        ]

        self.logs_period_started_at = logs_period_started_at
        self.logs_period_ended_at = logs_period_ended_at

        # Классы менеджеров Функций, которые должны быть запущены для сбора данных моделей РВД
        self._collecting_data_managers: Dict[str, Type[RunnerManager]] = {}

        # Результаты работы Функций сбора данных моделей РВД
        self._collecting_data_results = []

        # Идентификатор CollectDataCommandProgress для передачи сигналу manager_created
        self.command_id: Optional[int] = kwargs.get('command_id')

    def _find_collecting_models_data_managers(self):
        """
        Поиск менеджеров Функций, которые должны быть запущены для сбора данных моделей РВД.
        """
        logger.info('collecting_models_data_managers..')

        entity_storage = RegionalDataMartEntityStorage()
        entity_storage.prepare()

        collecting_models_data_managers_map = entity_storage.prepare_entities_manager_map(
            tags={REGIONAL_DATA_MART_INTEGRATION_COLLECTING_DATA},
        )

        for model_enum in self.models:
            manager_class = collecting_models_data_managers_map.get(model_enum.key)

            if manager_class:
                self._collecting_data_managers[model_enum.key] = manager_class

        logger.info('collecting models data managers finished')

    def _collect_models_data(self, *args, logs: Optional[Dict[str, List[AuditLog]]] = None, **kwargs):
        """
        Запуск Функций по формированию данных моделей РВД из логов.
        """
        logger.info('collect models data..')

        kwargs['logs_period_started_at'] = self.logs_period_started_at
        kwargs['logs_period_ended_at'] = self.logs_period_ended_at

        for model_key, manager_class in self._collecting_data_managers.items():
            model_logs = logs.get(model_key) if logs else None
            manager = manager_class(*args, logs=model_logs, **kwargs)

            if self.command_id:
                # Подается сигнал, что менеджер создан:
                manager_created.send(sender=manager,
                                     command_id=self.command_id)

            manager.run()

            self._collecting_data_results.append(manager.result)

        logger.info('collecting entities data finished.')

    def collect(self):
        """Запускает сбор данных."""
        logger.info(
            f'start collecting data of models - {", ".join([model.key for model in self.models])}..'
        )

        self._find_collecting_models_data_managers()
        self._collect_models_data()

        logger.info('collecting models data finished.')


class BaseCollectModelsDataByGeneratingLogs(BaseCollectModelsData):
    """Сбор данных моделей РВД на основе существующих в БД данных моделей ЭШ.

    Можно регулировать, для каких моделей должен быть произведен сбор данных, и период, за который должны
    быть собраны логи. Логи формируются в процессе выполнения команды при помощи генератора логов
    EduSchoolLogGenerator для указанной модели.
    """

    def __init__(
        self,
        models: Iterable[str],
        logs_period_started_at=datetime.combine(date.today(), time.min),
        logs_period_ended_at=datetime.combine(date.today(), time.min),
        logs_sub_period_days=LOGS_SUB_PERIOD_DAYS,
        school_ids=(),
        **kwargs,
    ):
        super().__init__(models, logs_period_started_at, logs_period_ended_at, **kwargs)

        self.logs_sub_period_days = logs_sub_period_days
        # Школы, для которых производится выгрузка
        self.school_ids = school_ids
        # Генератор логов
        self.log_generator = self._prepare_log_generator()

    def _prepare_log_generator(self) -> 'BaseEduLogGenerator':
        """Возвращает генератор логов."""
        raise NotImplementedError

    def _generate_logs_by_subperiod(self):
        """
        Генерация логов с учетом подпериодов.
        """
        temp_logs_period_started_at = self.logs_period_started_at
        temp_logs_period_ended_at = self.logs_period_started_at + timedelta(days=self.logs_sub_period_days)

        if temp_logs_period_ended_at > self.logs_period_ended_at:
            temp_logs_period_ended_at = self.logs_period_ended_at

        temp_logs: Dict[str, List[AuditLog]] = {}

        while temp_logs_period_started_at < temp_logs_period_ended_at <= self.logs_period_ended_at:
            for model in self.models:
                logs = self.log_generator.generate(
                    model=model,
                    logs_period_started_at=temp_logs_period_started_at,
                    logs_period_ended_at=temp_logs_period_ended_at,
                    school_ids=self.school_ids,
                )

                temp_logs[model.key] = logs

            yield temp_logs, temp_logs_period_started_at, temp_logs_period_ended_at

            temp_logs_period_started_at = temp_logs_period_ended_at
            temp_logs_period_ended_at += timedelta(days=self.logs_sub_period_days)

            if temp_logs_period_ended_at > self.logs_period_ended_at:
                temp_logs_period_ended_at = self.logs_period_ended_at

            temp_logs.clear()

    def _generate_logs_for_all_period(self):
        """
        Генерация логов за весь период.
        """
        temp_logs: Dict[str, List[AuditLog]] = {}

        for model in self.models:
            logs = self.log_generator.generate(
                model=model,
                logs_period_started_at=self.logs_period_started_at,
                logs_period_ended_at=self.logs_period_ended_at,
                school_ids=self.school_ids,
            )

            temp_logs[model.key] = logs

        return [(temp_logs, self.logs_period_started_at, self.logs_period_ended_at)]

    def _generate_logs(self) -> List[Tuple[Dict[str, List[AuditLog]], datetime, datetime]]:
        """
        Генерация логов.

        Осуществляет генерацию логов по уже существующим записям в базе данных. В качестве параметров указываются
        начало и конец периода сбора логов, размер подпериодов, на которые должен быть разбит основной период.
        Генерация логов производится только для указанных моделей.
        """
        if self.logs_sub_period_days:
            logs = self._generate_logs_by_subperiod()
        else:
            logs = self._generate_logs_for_all_period()

        return logs

    def collect(self):
        """Главный метод, через который происходит сбор данных."""
        logger.info(
            f'start collecting data of models - {", ".join([model.key for model in self.models])}..'
        )
        self._find_collecting_models_data_managers()

        temp_kwargs = {}

        for logs, logs_period_started_at, logs_period_ended_at in self._generate_logs():
            temp_kwargs['logs_period_started_at'] = logs_period_started_at
            temp_kwargs['logs_period_ended_at'] = logs_period_ended_at

            self._collect_models_data(logs=logs, **temp_kwargs)

        logger.info('collecting models data finished.')


class BaseCollectLatestModelsData(BaseCollectModelsData):
    """
    Сбор данных моделей РВД на основе логов за период с последней сборки до указанной даты.
    """

    def __init__(
        self,
        models: Iterable[str],
        logs_period_started_at=datetime.combine(date.today(), time.min),
        logs_period_ended_at=datetime.combine(date.today(), time.min),
        **kwargs,
    ):
        super().__init__(models, logs_period_started_at, logs_period_ended_at, **kwargs)

        # Перечисление с очередностью сбора данных по моделям
        self.order_number_model_enum = self._get_order_number_model_enum()

    def _get_order_number_model_enum(self) -> BaseEnumerate:
        """Возвращает перечисление с очередностью сбора данных по моделям."""
        raise NotImplementedError

    def _find_collecting_models_data_managers(self, *args, **kwargs) -> None:
        """
        Поиск менеджеров Функций, которые должны быть запущены для сбора данных моделей РВД.
        """
        logger.info('collecting_models_data_managers..')

        entity_storage = RegionalDataMartEntityStorage()
        entity_storage.prepare()

        collecting_models_data_managers_map = entity_storage.prepare_entities_manager_map(
            tags={REGIONAL_DATA_MART_INTEGRATION_COLLECTING_DATA},
        )

        export_models = filter(
            lambda entity: entity.order_number not in (None, DEFAULT_ORDER_NUMBER), self.models
        )

        # Сортируем модели по очередности загрузки
        sorted_models = sorted(
            export_models,
            key=lambda model: self.order_number_model_enum.get_constant_value_by_name(model.key)
        )

        for model_enum in sorted_models:
            manager_class = collecting_models_data_managers_map.get(model_enum.key)

            if manager_class:
                self._collecting_data_managers[model_enum.key] = manager_class

        logger.info('collecting models data managers finished')

    def _get_last_finished_entity_upload(self) -> Dict[str, datetime]:
        """
        Возвращает словарь с uuid менеджера и датой последней успешной выгрузки по указанным сущностям.
        """
        manager_to_last_date = CollectingExportedDataSubStage.objects.annotate(
            max_logs_period_ended_at=Max('stage__logs_period_ended_at'),
        ).values(
            'stage__manager_id', 'max_logs_period_ended_at',
        ).annotate(
            manager_id=F('stage__manager_id'),
            date_end=F('max_logs_period_ended_at'),
        ).filter(
            status_id=CollectingDataSubStageStatus.READY_TO_EXPORT.key,
            manager_id__in=[m.uuid for m in self._collecting_data_managers.values()],
        ).values('manager_id', 'date_end')

        return {str(m['manager_id']): m['date_end'] for m in manager_to_last_date}

    def _collect_models_data(self, *args, logs: Optional[Dict[str, List[AuditLog]]] = None, **kwargs) -> None:
        """
        Запуск Функций по формированию данных из логов для дальнейшей выгрузки.
        """
        logger.info('collect entities data..')

        last_finished_entity_upload = self._get_last_finished_entity_upload()

        if logs is None:
            logs = {}

        for entity_key, manager_class in self._collecting_data_managers.items():
            entity_logs = logs.get(entity_key)

            kwargs['logs_period_started_at'] = (
                last_finished_entity_upload.get(manager_class.uuid)
                or get_today_min_datetime()
            )
            kwargs['logs_period_ended_at'] = timezone.now()

            if kwargs['logs_period_started_at'] > kwargs['logs_period_ended_at']:
                kwargs['logs_period_started_at'] = kwargs['logs_period_ended_at'] - datetime.timedelta(
                    seconds=RDM_TRANSFER_TASK_TIMEDELTA
                )

            manager = manager_class(*args, logs=entity_logs, **kwargs)

            if self.command_id:
                # Подается сигнал, что менеджер создан:
                manager_created.send(sender=manager,
                                     command_id=self.command_id)

            manager.run()

            self._collecting_data_results.append(manager.result)

        logger.info('collecting entities data finished.')


class CollectModelsData(BaseCollectModelsData):
    """Сбор данных моделей РВД за указанных период по существующим логам."""
