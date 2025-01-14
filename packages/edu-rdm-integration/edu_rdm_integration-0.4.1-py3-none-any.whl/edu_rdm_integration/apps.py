from django.apps.config import (
    AppConfig,
)
from django.conf import (
    settings,
)


class EduRDMIntegrationConfig(AppConfig):
    """Интеграция с Региональной витриной данных."""

    name = 'edu_rdm_integration'
    label = 'edu_rdm_integration'

    def __set_default_settings(self):
        """Установка дефолтных значений настроек приложения."""
        from django.conf import (
            settings,
        )

        from edu_rdm_integration import (
            app_settings as defaults,
        )

        for name in dir(defaults):
            if name.isupper() and not hasattr(settings, name):
                setattr(settings, name, getattr(defaults, name))

    def __setup_uploader_client(self):
        """
        Инициализация клиента для взаимодействия с Региональной витриной данных.
        """
        import uploader_client
        from uploader_client.contrib.rdm.interfaces.configurations import (
            RegionalDataMartUploaderConfig,
        )

        if settings.RDM_UPLOADER_CLIENT_ENABLE_REQUEST_EMULATION:
            uploader_client.set_config(
                RegionalDataMartUploaderConfig(
                    interface='uploader_client.contrib.rdm.interfaces.rest.OpenAPIInterfaceEmulation',
                    url=settings.RDM_UPLOADER_CLIENT_URL,
                    datamart_name=settings.RDM_UPLOADER_CLIENT_DATAMART_NAME,
                    timeout=1,
                    request_retries=1,
                )
            )
        else:
            uploader_client.set_config(
                RegionalDataMartUploaderConfig(
                    url=settings.RDM_UPLOADER_CLIENT_URL,
                    datamart_name=settings.RDM_UPLOADER_CLIENT_DATAMART_NAME,
                    timeout=settings.RDM_UPLOADER_CLIENT_REQUEST_TIMEOUT,
                    request_retries=settings.RDM_UPLOADER_CLIENT_REQUEST_RETRIES,
                )
            )

    def ready(self):
        """Вызывается после инициализации приложения."""
        super().ready()

        # Инициализация клиента загрузчика данных в Витрину
        self.__setup_uploader_client()

        # Установка дефолтных значений в settings.py
        self.__set_default_settings()
