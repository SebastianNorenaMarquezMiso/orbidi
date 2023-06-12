import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env.local
load_dotenv('.env.local')


class Settings:
    # Configuración de HubSpot
    HUBSPOT_API_KEY = os.getenv('HUBSPOT_API_KEY', '')
    HUBSPOT_BASE_URL = os.getenv('HUBSPOT_BASE_URL', '')

    # Configuración de ClickUp
    CLICKUP_API_KEY = os.getenv('CLICKUP_API_KEY', '')
    CLICKUP_BASE_URL = os.getenv('CLICKUP_BASE_URL', '')
    CLICKUP_LIST_ID = os.getenv('CLICKUP_LIST_ID', '')

    # Configuración de la base de datos
    DB_HOST = os.getenv('DB_HOST', '')
    DB_PORT = os.getenv('DB_PORT', '')
    DB_USER = os.getenv('DB_USER', '')
    DB_PASS = os.getenv('DB_PASS', '')
    DB_NAME = os.getenv('DB_NAME', '')
    DB_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # Otras configuraciones
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'INFO')


settings = Settings()
