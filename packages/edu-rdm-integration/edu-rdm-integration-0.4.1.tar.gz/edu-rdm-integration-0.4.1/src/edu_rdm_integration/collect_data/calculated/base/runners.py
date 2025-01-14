from typing import (
    Type,
)

from edu_rdm_integration.collect_data.base.runners import (
    BaseCollectingDataRunner,
)
from edu_rdm_integration.collect_data.calculated.base.helpers import (
    BaseCollectingCalculatedExportedDataRunnerHelper,
)
from edu_rdm_integration.collect_data.calculated.base.results import (
    BaseCollectingCalculatedExportedDataRunnerResult,
)
from edu_rdm_integration.collect_data.calculated.base.validators import (
    BaseCollectingCalculatedExportedDataRunnerValidator,
)


class BaseCollectingCalculatedExportedDataRunner(BaseCollectingDataRunner):
    """
    Базовый класс ранеров функций сбора расчетных данных для интеграции с "Региональная витрина данных".
    """

    def _prepare_helper_class(self) -> Type[BaseCollectingCalculatedExportedDataRunnerHelper]:
        """
        Возвращает класс помощника ранера функции.
        """
        return BaseCollectingCalculatedExportedDataRunnerHelper

    def _prepare_validator_class(self) -> Type[BaseCollectingCalculatedExportedDataRunnerValidator]:
        """
        Возвращает класс валидатора ранера функции.
        """
        return BaseCollectingCalculatedExportedDataRunnerValidator

    def _prepare_result_class(self) -> Type[BaseCollectingCalculatedExportedDataRunnerResult]:
        """
        Возвращает класс результата ранера функции.
        """
        return BaseCollectingCalculatedExportedDataRunnerResult
