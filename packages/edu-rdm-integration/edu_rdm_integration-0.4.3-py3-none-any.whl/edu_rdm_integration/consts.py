REGIONAL_DATA_MART_INTEGRATION_COLLECTING_DATA = 'regional_data_mart_integration_collecting_data'
REGIONAL_DATA_MART_INTEGRATION_EXPORTING_DATA = 'regional_data_mart_integration_exporting_data'

# Формат даты. Используется для выгрузки
DATE_FORMAT = '%Y-%m-%d'

# Формат даты/времени. Для выгрузки не используется (в выгрузке ISO формат)
DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S'

# Формат даты/времени. Для выгрузки
EXPORT_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

LOGS_DELIMITER = '    '

HASH_ALGORITHM = 'md_gost12_512'

LOGS_SUB_PERIOD_DAYS = 0
BATCH_SIZE = 5000

ACADEMIC_YEAR = {
    'start_day': 1,
    'start_month': 9,
    'end_day': 31,
    'end_month': 8,
}

TASK_QUEUE_NAME = 'RDM'
