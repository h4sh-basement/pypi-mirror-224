from datetime import (
    datetime,
)

from django.db.models import (
    CASCADE,
    PROTECT,
    SET_NULL,
    BooleanField,
    CharField,
    DateTimeField,
    FileField,
    ForeignKey,
    PositiveSmallIntegerField,
    SmallIntegerField,
)
from m3.db import (
    BaseObjectModel,
)
from uploader_client.models import (
    Entry,
)

from educommon.django.db.mixins import (
    ReprStrPreModelMixin,
)
from educommon.integration_entities.enums import (
    EntityLogOperation,
)
from educommon.utils.caching import (
    cached_function,
)
from educommon.utils.date import (
    get_today_max_datetime,
    get_today_min_datetime,
)
from function_tools.models import (
    Entity,
)
from m3_db_utils.models import (
    ModelEnumValue,
    TitledModelEnum,
)

from edu_rdm_integration.enums import (
    FileUploadStatusEnum,
)
from edu_rdm_integration.utils import (
    get_exporting_data_stage_attachment_path,
)


class CollectingDataStageStatus(TitledModelEnum):
    """Статус этапа сбора данных."""

    CREATED = ModelEnumValue(
        title='Создан',
    )

    IN_PROGRESS = ModelEnumValue(
        title='В процессе сбора',
    )

    FAILED = ModelEnumValue(
        title='Завершено с ошибками',
    )

    FINISHED = ModelEnumValue(
        title='Завершено',
    )

    class Meta:
        db_table = 'rdm_collecting_data_stage_status'
        verbose_name = 'Модель-перечисление статусов этапа сбора данных'
        verbose_name_plural = 'Модели-перечисления статусов этапов сбора данных'


class CollectingExportedDataStage(ReprStrPreModelMixin, BaseObjectModel):
    """Этап подготовки данных в рамках Функций. За работу Функции отвечает ранер менеджер."""

    manager = ForeignKey(
        to=Entity,
        verbose_name='Менеджер ранера Функции',
        on_delete=PROTECT,
        null=True,
        blank=True,
    )

    logs_period_started_at = DateTimeField(
        'Левая граница периода обрабатываемых логов',
        db_index=True,
        default=get_today_min_datetime,
    )

    logs_period_ended_at = DateTimeField(
        'Правая граница периода обрабатываемых логов',
        db_index=True,
        default=get_today_max_datetime,
    )

    started_at = DateTimeField(
        'Время начала сбора данных',
        auto_now_add=True,
        db_index=True,
    )

    ended_at = DateTimeField(
        'Время завершения сбора данных',
        null=True,
        blank=True,
        db_index=True,
    )

    status = ForeignKey(
        to=CollectingDataStageStatus,
        verbose_name='Статус',
        on_delete=PROTECT,
        default=CollectingDataStageStatus.CREATED.key,
    )

    class Meta:
        db_table = 'rdm_collecting_exported_data_stage'
        verbose_name = 'Этап формирования данных для выгрузки'
        verbose_name_plural = 'Этапы формирования данных для выгрузки'

    @property
    def attrs_for_repr_str(self):
        return ['manager_id', 'logs_period_started_at', 'logs_period_ended_at', 'started_at', 'ended_at', 'status_id']

    def save(self, *args, **kwargs):
        if (
            self.status_id in (CollectingDataStageStatus.FAILED.key, CollectingDataStageStatus.FINISHED.key)
            and not self.ended_at
        ):
            self.ended_at = datetime.now()

        super().save(*args, **kwargs)


class CollectingDataSubStageStatus(TitledModelEnum):
    """Статус этапа сбора данных."""

    CREATED = ModelEnumValue(
        title='Создан',
    )

    IN_PROGRESS = ModelEnumValue(
        title='В процессе сбора',
    )

    READY_TO_EXPORT = ModelEnumValue(
        title='Готово к выгрузке',
    )

    FAILED = ModelEnumValue(
        title='Завершено с ошибками',
    )

    EXPORTED = ModelEnumValue(
        title='Выгружено',
    )

    NOT_EXPORTED = ModelEnumValue(
        title='Не выгружено',
    )

    class Meta:
        db_table = 'rdm_collecting_data_sub_stage_status'
        verbose_name = 'Модель-перечисление статусов подэтапа сбора данных'
        verbose_name_plural = 'Модели-перечисления статусов подэтапов сбора данных'


class CollectingExportedDataSubStage(ReprStrPreModelMixin, BaseObjectModel):
    """Подэтап сбора данных для сущностей в рамках функции."""

    stage = ForeignKey(
        to=CollectingExportedDataStage,
        verbose_name='Этап подготовки данных для экспорта',
        on_delete=PROTECT,
    )

    function = ForeignKey(
        to=Entity,
        verbose_name='Функция',
        on_delete=PROTECT,
    )

    started_at = DateTimeField(
        'Время начала сбора данных',
        auto_now_add=True,
        db_index=True,
    )

    ended_at = DateTimeField(
        'Время завершения сбора данных',
        null=True,
        blank=True,
        db_index=True,
    )

    previous = ForeignKey(
        'self',
        null=True,
        blank=True,
        verbose_name='Предыдущий сбор данных',
        on_delete=CASCADE,
    )

    status = ForeignKey(
        to=CollectingDataSubStageStatus,
        verbose_name='Статус',
        on_delete=PROTECT,
        default=CollectingDataSubStageStatus.CREATED.key,
    )

    class Meta:
        db_table = 'rdm_collecting_exported_data_sub_stage'
        verbose_name = 'Подэтап формирования данных для выгрузки'
        verbose_name_plural = 'Подэтапы формирования данных для выгрузки'

    @property
    def attrs_for_repr_str(self):
        return ['stage_id', 'function_id', 'started_at', 'ended_at', 'previous_id', 'status_id']

    def save(self, *args, **kwargs):
        if (
            self.status_id in (
                CollectingDataSubStageStatus.FAILED.key,
                CollectingDataSubStageStatus.READY_TO_EXPORT.key
            )
            and not self.ended_at
        ):
            self.ended_at = datetime.now()

        super().save(*args, **kwargs)


class ExportingDataStageStatus(TitledModelEnum):
    """
    Статус этапа выгрузки данных.
    """

    CREATED = ModelEnumValue(
        title='Создан',
    )

    IN_PROGRESS = ModelEnumValue(
        title='В процессе',
    )

    FAILED = ModelEnumValue(
        title='Завершено с ошибками',
    )

    FINISHED = ModelEnumValue(
        title='Завершено',
    )

    class Meta:
        db_table = 'rdm_exporting_data_stage_status'
        verbose_name = 'Модель-перечисление статусов этапа выгрузки данных'
        verbose_name_plural = 'Модели-перечисления статусов этапов выгрузки данных'


class ExportingDataStage(ReprStrPreModelMixin, BaseObjectModel):
    """
    Этап выгрузки данных.
    """

    manager = ForeignKey(
        to=Entity,
        verbose_name='Менеджер ранера Функции',
        on_delete=PROTECT,
        null=True,
        blank=True,
    )

    period_started_at = DateTimeField(
        'Левая граница периода выборки данных для выгрузки',
        db_index=True,
    )

    period_ended_at = DateTimeField(
        'Правая граница периода выборки данных для выгрузки',
        db_index=True,
    )

    started_at = DateTimeField(
        'Время начала выгрузки данных',
        auto_now_add=True,
    )

    ended_at = DateTimeField(
        'Время завершения выгрузки данных',
        null=True,
        blank=True,
    )

    status = ForeignKey(
        to=ExportingDataStageStatus,
        verbose_name='Статус',
        on_delete=PROTECT,
        default=ExportingDataStageStatus.CREATED.key,
    )

    class Meta:
        db_table = 'rdm_exporting_data_stage'
        verbose_name = 'Этап формирования данных для выгрузки'
        verbose_name_plural = 'Этапы формирования данных для выгрузки'

    @property
    def attrs_for_repr_str(self):
        return ['manager_id', 'started_at', 'ended_at', 'status_id']

    def save(self, *args, **kwargs):
        if (
            self.status_id in (ExportingDataStageStatus.FAILED.key, ExportingDataStageStatus.FINISHED.key)
            and not self.ended_at
        ):
            self.ended_at = datetime.now()

        super().save(*args, **kwargs)


class ExportingDataSubStageStatus(TitledModelEnum):
    """
    Модель-перечисление статусов этапа выгрузки данных
    """

    CREATED = ModelEnumValue(
        title='Создан',
    )

    IN_PROGRESS = ModelEnumValue(
        title='Запущен',
    )

    FAILED = ModelEnumValue(
        title='Завершено с ошибками',
    )

    FINISHED = ModelEnumValue(
        title='Завершен',
    )

    class Meta:
        db_table = 'rdm_exporting_data_sub_stage_status'
        verbose_name = 'Модель-перечисление статусов подэтапа выгрузки данных'
        verbose_name_plural = 'Модели-перечисления статусов подэтапов выгрузки данных'


class ExportingDataSubStage(ReprStrPreModelMixin, BaseObjectModel):
    """
    Подэтап выгрузки данных.
    """

    function = ForeignKey(
        to=Entity,
        verbose_name='Функция',
        on_delete=PROTECT,
        null=True,
        blank=True,
    )

    stage = ForeignKey(
        to=ExportingDataStage,
        verbose_name='Этап выгрузки данных',
        on_delete=CASCADE,
    )

    started_at = DateTimeField(
        verbose_name='Время начала сбора данных',
        auto_now_add=True,
        db_index=True,
    )

    ended_at = DateTimeField(
        verbose_name='Время завершения сбора данных',
        null=True,
        blank=True,
        db_index=True,
    )

    status = ForeignKey(
        to=ExportingDataSubStageStatus,
        verbose_name='Статус',
        on_delete=PROTECT,
        default=ExportingDataSubStageStatus.CREATED.key,
    )

    class Meta:
        db_table = 'rdm_exporting_data_sub_stage'
        verbose_name = 'Стадия выгрузки данных'
        verbose_name_plural = 'Стадии выгрузки данных'

    @property
    def attrs_for_repr_str(self):
        return ['function_id', 'collecting_data_sub_stage_id', 'stage_id', 'started_at', 'ended_at', 'status_id']

    def save(self, *args, **kwargs):
        if (
            self.status_id in (ExportingDataSubStageStatus.FAILED.key, ExportingDataSubStageStatus.FINISHED.key)
            and not self.ended_at
        ):
            self.ended_at = datetime.now()

        super().save(*args, **kwargs)


class ExportingDataSubStageAttachment(ReprStrPreModelMixin, BaseObjectModel):
    """
    Сгенерированный файл для дальнейшей выгрузки в "Региональная витрина данных".
    """

    exporting_data_sub_stage = ForeignKey(
        to=ExportingDataSubStage,
        verbose_name='Подэтап выгрузки данных',
        on_delete=CASCADE,
    )

    # TODO PYTD-22 В зависимости от принятого решения по инструменту ограничения доступа к media-файлам, нужно будет
    #  изменить тип поля или оставить как есть
    attachment = FileField(
        verbose_name='Сгенерированный файл',
        upload_to=get_exporting_data_stage_attachment_path,
        max_length=512,
        null=True,
        blank=True,
    )

    operation = SmallIntegerField(
        verbose_name='Действие',
        choices=EntityLogOperation.get_choices(),
    )

    created = DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        null=True,
        blank=True,
    )
    modified = DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True,
        null=True,
        blank=True,
    )

    class Meta:
        db_table = 'rdm_exporting_data_sub_stage_attachment'
        verbose_name = 'Сгенерированный файл для дальнейшей выгрузки в "Региональная витрина данных"'
        verbose_name_plural = 'Сгенерированные файлы для дальнейшей выгрузки в "Региональная витрина данных"'

    @property
    def attrs_for_repr_str(self):
        return ['exporting_data_sub_stage_id', 'attachment', 'operation', 'created', 'modified']


class UploadStatus(ReprStrPreModelMixin, BaseObjectModel):
    """
    Модель-перечисления для статусов загрузки в витрину.
    """
    code = SmallIntegerField(
        "Код статуса загрузки в витрину",
        null=True,
        blank=True,
    )
    description = CharField(
        "Описание статуса загрузки в витрину",
        max_length=100
    )

    @classmethod
    @cached_function(3600, 'rdm_upload_status_id', ('code', 'description',))
    def get_cached_status(cls, code, description):
        """Возвращает закешированный id статуса загрузки по коду и описанию"""
        status = cls.objects.get(code=code, description=description)
        return status

    class Meta:
        db_table = 'rdm_upload_status'
        verbose_name = 'Статус загрузки данных в витрину'
        verbose_name_plural = 'Статусы загрузки данных в витрину'


class ExportingDataSubStageUploaderClientLog(ReprStrPreModelMixin, BaseObjectModel):
    """
    Связь лога Загрузчика данных с подэтапом выгрузки данных.
    """

    entry = ForeignKey(
        to=Entry,
        verbose_name='Лог запроса и ответа',
        on_delete=CASCADE,
        related_name='uploader_client_log',
    )

    sub_stage = ForeignKey(
        to=ExportingDataSubStage,
        verbose_name='Подэтап выгрузки данных',
        on_delete=CASCADE,
    )

    attachment = ForeignKey(
        to=ExportingDataSubStageAttachment,
        verbose_name='Прикрепленный файл',
        on_delete=CASCADE,
    )

    request_id = CharField(
        verbose_name='Id запроса загрузки в витрину',
        max_length=100,
        blank=True
    )

    is_emulation = BooleanField(
        verbose_name='Включен режим эмуляции',
        default=False,
    )

    file_upload_status = SmallIntegerField(
        verbose_name="Общий статус загрузки файла в витрину",
        choices=FileUploadStatusEnum.get_choices(),
        null=True,
        blank=True,
    )

    created = DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        null=True,
        blank=True,
        db_index=True,
    )
    modified = DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True,
        null=True,
        blank=True,
        db_index=True,
    )

    class Meta:
        db_table = 'rdm_exporting_data_sub_stage_uploader_client_log'
        verbose_name = 'Лог запроса подэтапа выгрузки данных'
        verbose_name_plural = 'Лог запроса подэтапа выгрузки данных'


class UploadStatusRequestLog(ReprStrPreModelMixin, BaseObjectModel):
    """
    Модель связывающая статусы, загрузку файла в витрину и http-запрос к витрине.
    """

    upload = ForeignKey(
        verbose_name='Cвязь запроса статуса с загрузкой файла в витрину',
        to=ExportingDataSubStageUploaderClientLog,
        on_delete=CASCADE,
    )
    entry = ForeignKey(
        verbose_name='Cвязь запроса статуса с запросом в витрину',
        to=Entry,
        on_delete=CASCADE,
        related_name='upload_status_request_log',
    )
    status = ForeignKey(
        verbose_name='Cвязь с таблицей возможных статусов',
        to=UploadStatus,
        on_delete=CASCADE,
    )

    class Meta:
        db_table = 'rdm_upload_status_request_log'
        verbose_name = 'Лог запроса подэтапа выгрузки данных'
        verbose_name_plural = 'Логи запроса подэтапа выгрузки данных'


class BaseEntityModel(ReprStrPreModelMixin, BaseObjectModel):
    """Базовая модель сущности."""

    collecting_sub_stage = ForeignKey(
        verbose_name='Подэтап сбора данных сущности',
        to=CollectingExportedDataSubStage,
        on_delete=CASCADE,
    )
    exporting_sub_stage = ForeignKey(
        verbose_name='Подэтап выгрузки',
        to=ExportingDataSubStage,
        blank=True,
        null=True,
        on_delete=CASCADE,
    )
    operation = SmallIntegerField(
        verbose_name='Действие',
        choices=EntityLogOperation.get_choices(),
    )

    created = DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        null=True,
        blank=True,
        db_index=True,
    )
    modified = DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True,
        null=True,
        blank=True,
        db_index=True,
    )

    @property
    def attrs_for_repr_str(self):
        return ['collecting_sub_stage', 'exporting_sub_stage', 'operation', 'created', 'modified']

    class Meta:
        abstract = True


class RegionalDataMartModelEnum(TitledModelEnum):
    """Модель-перечисление моделей "Региональная витрина данных"."""

    class Meta:
        db_table = 'rdm_model'
        extensible = True
        verbose_name = 'Модель-перечисление моделей "Региональной витрины данных"'
        verbose_name_plural = 'Модели-перечисления моделей "Региональной витрины данных"'


class RegionalDataMartEntityEnum(TitledModelEnum):
    """Модель-перечисление сущностей выгрузки в Региональная витрина данных."""

    class Meta:
        db_table = 'rdm_entity'
        extensible = True
        verbose_name = 'Модель-перечисление сущностей "Региональной витрины данных"'
        verbose_name_plural = 'Модели-перечисления сущностей "Региональной витрины данных"'


class AbstractCollectDataCommandProgress(ReprStrPreModelMixin, BaseObjectModel):
    """
    Модель, хранящая данные для формирования и отслеживания асинхронных задач по сбору данных.

    В реализации необходимо определить поля:
        1. Ссылку на асинхронную задачу, например:
            task = ForeignKey(
                to=RunningTask,
                verbose_name='Асинхронная задача',
                blank=True, null=True,
                on_delete=SET_NULL,
            )
        2. Поле хранения лога:
            logs_link = FileField(
                upload_to=upload_file_handler,
                max_length=255,
                verbose_name='Ссылка на файл логов',
            )
    """

    task = ...

    logs_link = ...

    stage = ForeignKey(
        to=CollectingExportedDataStage,
        verbose_name='Этап формирования данных для выгрузки',
        blank=True, null=True,
        on_delete=SET_NULL,
    )
    model = ForeignKey(
        to=RegionalDataMartModelEnum,
        verbose_name='Модель РВД',
        on_delete=PROTECT,
    )
    logs_period_started_at = DateTimeField(
        'Левая граница периода обрабатываемых логов',
    )
    logs_period_ended_at = DateTimeField(
        'Правая граница периода обрабатываемых логов',
    )
    logs_sub_period_days = PositiveSmallIntegerField(
        'Размер подпериода',
        default=0,
    )

    class Meta:
        abstract = True
        db_table = 'rdm_collecting_data_command_progress'
        verbose_name = 'Задача по сбору данных'
        verbose_name_plural = 'Задачи по сбору данных'
