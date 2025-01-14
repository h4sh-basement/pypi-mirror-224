from edu_rdm_integration.export_data.export import (
    BaseExportEntitiesData,
    ExportEntitiesData,
)
from edu_rdm_integration.management.general import (
    BaseExportEntityDataCommand,
)


class Command(BaseExportEntityDataCommand):
    """
    Команда для выгрузки данных сущностей РВД.
    """

    # flake8: noqa: A003
    help = 'Команда для выгрузки данных сущностей РВД за указанных период.'

    def _prepare_export_entities_data_class(self, *args, **kwargs) -> BaseExportEntitiesData:
        """Возвращает объект класса экспорта данных сущностей РВД."""
        return ExportEntitiesData(
            entities=kwargs.get('entities'),
            period_started_at=kwargs.get('period_started_at'),
            period_ended_at=kwargs.get('period_ended_at'),
        )
