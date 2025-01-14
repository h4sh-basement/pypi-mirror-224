from abc import (
    ABCMeta,
)
from datetime import (
    date,
    datetime,
    time,
)
from typing import (
    Dict,
    Tuple,
    Type,
)

from educommon import (
    logger,
)
from m3_db_utils.models import (
    ModelEnumValue,
)

from edu_rdm_integration.adapters.managers import (
    WebEduRunnerManager,
)
from edu_rdm_integration.consts import (
    LOGS_DELIMITER,
)
from edu_rdm_integration.export_data.base.runners import (
    BaseExportDataRunner,
)
from edu_rdm_integration.models import (
    CollectingDataStageStatus,
    ExportingDataStage,
    ExportingDataStageStatus,
)
from edu_rdm_integration.storages import (
    RegionalDataMartEntityStorage,
)


class BaseExportDataRunnerManager(WebEduRunnerManager, metaclass=ABCMeta):
    """
    Менеджер ранеров функций выгрузки данных для интеграции с "Региональная витрина данных".
    """

    def __init__(
        self,
        *args,
        is_only_main_model: bool = False,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        # Выгрузка данных производится только для основной модели сущности
        self._is_only_main_model = is_only_main_model

        self._period_started_at, self._period_ended_at = self._prepare_period(*args, **kwargs)

        self._stage = ExportingDataStage.objects.create(
            manager_id=self.uuid,
            period_started_at=self._period_started_at,
            period_ended_at=self._period_ended_at,
        )

        logger.info(f'{LOGS_DELIMITER}{repr(self._stage)} created.')

    @classmethod
    def _prepare_runner_class(cls) -> Type[BaseExportDataRunner]:
        """
        Возвращает класс ранера.
        """
        return BaseExportDataRunner

    def _find_exporting_data_stage(self):
        """
        Поиск последнего подэтапа выгрузки данных сущности РВД.
        """
        entity_storage = RegionalDataMartEntityStorage()
        entity_storage.prepare()

        exporting_data_stage = ExportingDataStage.objects.filter(
            manager_id=self.uuid,
            status_id__in=(
                CollectingDataStageStatus.FAILED.key,
                CollectingDataStageStatus.FINISHED.key,
            ),
        ).latest('period_ended_at')

        if exporting_data_stage:
            logger.info(f'{LOGS_DELIMITER}{repr(exporting_data_stage)} sub stages found.')
        else:
            logger.info(f'{LOGS_DELIMITER} sub stages not found.')

        return exporting_data_stage

    def _prepare_period(self, *args, **kwargs) -> Tuple[datetime, datetime]:
        """
        Формирование периода сбора данных моделей РВД.
        """
        period_started_at = kwargs.get('period_started_at')
        period_ended_at = kwargs.get('period_ended_at')

        if not period_started_at:
            last_exporting_data_stage = self._find_exporting_data_stage()

            if last_exporting_data_stage:
                period_started_at = last_exporting_data_stage.period_ended_at
            else:
                period_started_at = datetime.combine(date.today(), time.min)

        if not period_ended_at:
            period_ended_at = datetime.combine(date.today(), time.max)

        return period_started_at, period_ended_at

    def _prepare_model_ids_map(self) -> Dict[ModelEnumValue, Tuple[int]]:
        """
        Осуществляется поиск записей моделей добавленных или обновленных за указанный период времени.

        Т.к. моделей влияющих на сущность может быть множество, то в методе формируется словарь, содержащий в качестве
        ключа название модели, значение - кортеж идентификаторов записей.
        """
        return {}

    def _create_runner(self, *args, **kwargs):
        """
        Производится расширение для осуществления поиска идентификаторов записей моделей РВД для дальнейшей выгрузки.

        model_ids_map пробрасывается в ранер для дальнейшей обработки записей для формирования чанков.
        is_force_fill_cache указывается для отказа от заполнения кешей запускаемых объектов при их создании.
        """
        model_ids_map = self._prepare_model_ids_map()

        super()._create_runner(
            *args,
            model_ids_map=model_ids_map,
            stage=self._stage,
            is_force_fill_cache=False,
            **kwargs,
        )

    def _before_start_runner(self, *args, **kwargs):
        """
        Точка расширения поведения менеджера ранера перед запуском ранера.
        """
        self._stage.status_id = ExportingDataStageStatus.IN_PROGRESS.key
        self._stage.save()

        logger.info(f'{LOGS_DELIMITER}change status {repr(self._stage)}')

    def _start_runner(self, *args, **kwargs):
        """
        Ранер необходимо запустить с отложенным заполнением кешей, чтобы заполнение произошло перед запуском объекта.
        """
        super()._start_runner(*args, is_force_fill_cache=False, **kwargs)

    def _after_start_runner(self, *args, **kwargs):
        """
        Точка расширения поведения менеджера ранера после запуска ранера.
        """
        if self._runner.result.has_not_errors:
            self._stage.status_id = ExportingDataStageStatus.FINISHED.key
        else:
            self._stage.status_id = ExportingDataStageStatus.FAILED.key

        self._stage.save()

        logger.info(f'{LOGS_DELIMITER}change status {repr(self._stage)}')
