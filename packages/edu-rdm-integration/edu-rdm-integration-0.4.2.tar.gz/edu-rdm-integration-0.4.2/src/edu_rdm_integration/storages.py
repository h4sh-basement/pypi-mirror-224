from collections import (
    defaultdict,
)
from typing import (
    Dict,
    List,
    Set,
    Type,
)

from function_tools.models import (
    EntityType,
)
from function_tools.runners import (
    BaseRunner,
)
from function_tools.storages import (
    EntityStorage,
)
from m3_db_utils.models import (
    ModelEnumValue,
)

from edu_rdm_integration.consts import (
    REGIONAL_DATA_MART_INTEGRATION_COLLECTING_DATA,
    REGIONAL_DATA_MART_INTEGRATION_EXPORTING_DATA,
)


class RegionalDataMartEntityStorage(EntityStorage):
    """
    Хранилище классов сущностей реализованных в системе.

    Собираются только те сущности, типы которых указаны в модели-перечислении
    function_tools.models.function_tools.models.EntityType. Расширение произведено в связи с необходимостью получения
    карт соответствия менеджеров и сущностей, функций и сущностей.
    """

    def _collect_runner_regional_data_mart_integration_entities(
        self,
        runner_class: Type[BaseRunner],
        runner_regional_data_mart_integration_entities: List[str],
    ):
        """
        Собирает и возвращает список сущностей.
        """
        for runnable_class in runner_class._prepare_runnable_classes():
            if hasattr(runnable_class, '_prepare_runnable_classes'):
                self._collect_runner_regional_data_mart_integration_entities(
                    runner_class=runnable_class,
                    runner_regional_data_mart_integration_entities=runner_regional_data_mart_integration_entities,
                )

                continue

            if hasattr(runnable_class, 'entities'):
                entities = getattr(runnable_class, 'entities')

                runner_regional_data_mart_integration_entities.extend(entities)

    def prepare_entities_map(
        self,
        entity_type: ModelEnumValue,
        tags: Set[str],
        *args,
        **kwargs,
    ) -> Dict[str, Type[object]]:
        """
        Формирование карты соответствия сущности интеграции с "Региональная витрина данных" и сущности function_tools.
        """
        rdm_integration_function_tools_entities_map: Dict[str, Type[object]] = {}

        registered_function_tools_entities_classes = [
            entity['class']
            for entity in self.entities[entity_type.key].values()
            if not tags.difference(entity['class'].tags)
        ]

        for function_tools_entity_class in registered_function_tools_entities_classes:
            regional_data_mart_integration_entities = []

            if hasattr(function_tools_entity_class, 'runner_class'):
                runner_class = function_tools_entity_class.runner_class

                self._collect_runner_regional_data_mart_integration_entities(
                    runner_class=runner_class,
                    runner_regional_data_mart_integration_entities=regional_data_mart_integration_entities,
                )
            elif hasattr(function_tools_entity_class, 'entities'):
                regional_data_mart_integration_entities = function_tools_entity_class.entities

            for rdm_integration_entity in regional_data_mart_integration_entities:
                rdm_integration_function_tools_entities_map[rdm_integration_entity.key] = function_tools_entity_class

        return rdm_integration_function_tools_entities_map

    def prepare_entities_manager_map(self, tags: Set[str]) -> Dict[str, Type[object]]:
        """
        Формирование карты соответствия сущности интеграции с "Региональная витрина данных" и менеджера Функции.

        Стоит учитывать, что в рамках одной Функции может производиться работа с несколькими сущностями.
        """
        return self.prepare_entities_map(
            entity_type=EntityType.MANAGER,
            tags=tags,
        )

    def prepare_manager_entities_map(self, tags: Set[str]) -> Dict[Type[object], List[str]]:
        """
        Формирование карты соответствия менеджера Функции и сущности интеграции с "Региональная витрина данных".

        Стоит учитывать, что в рамках одной Функции может производиться работа с несколькими сущностями.
        """
        _manager_entities_map = defaultdict(set)
        exporting_entities_data_managers_map = self.prepare_entities_manager_map(tags=tags)

        for entity in exporting_entities_data_managers_map:
            _manager_entities_map[exporting_entities_data_managers_map[entity]].add(entity)

        return _manager_entities_map

    def prepare_entities_functions_map(self, tags: Set[str]) -> Dict[str, Type[object]]:
        """
        Формирование карты соответствия сущности интеграции с "Региональная витрина данных" и функции.

        Стоит учитывать, что в рамках одной Функции может производиться работа с несколькими сущностями.
        """
        return self.prepare_entities_map(
            entity_type=EntityType.FUNCTION,
            tags=tags,
        )

    def prepare_exporting_collecting_functions_map(self) -> Dict[str, str]:
        """
        Возвращает карту соответствия функций выгрузки и сбора данных.

        Returns:
            Возвращает словарь в качестве ключей и значений используются UUID-ы функций.
        """
        exporting_collecting_functions_map = {}

        exporting_entities_data_functions_map = self.prepare_entities_functions_map(
            tags={REGIONAL_DATA_MART_INTEGRATION_EXPORTING_DATA},
        )
        collecting_entities_data_functions_map = self.prepare_entities_functions_map(
            tags={REGIONAL_DATA_MART_INTEGRATION_COLLECTING_DATA},
        )

        for entity in exporting_entities_data_functions_map.keys():
            exporting_collecting_functions_map[exporting_entities_data_functions_map[entity].uuid] = (
                collecting_entities_data_functions_map[entity].uuid
            )

        return exporting_collecting_functions_map
