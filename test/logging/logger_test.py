from unittest.mock import patch
from log.logger import Logger


@patch('logging.getLogger')
def test_logger_info(mock_get_logger):
    # Configurar el mock para el método getLogger
    mock_logger = mock_get_logger.return_value

    # Crear una instancia del logger
    logger = Logger()

    # Llamar al método info del logger
    logger.info("Test message")

    # Verificar que se haya llamado al método info del logger
    mock_logger.info.assert_called_once_with("Test message")


@patch('logging.getLogger')
def test_logger_error(mock_get_logger):
    # Configurar el mock para el método getLogger
    mock_logger = mock_get_logger.return_value

    # Crear una instancia del logger
    logger = Logger()

    # Llamar al método error del logger
    logger.error("Test error")

    # Verificar que se haya llamado al método error del logger
    mock_logger.error.assert_called_once_with("Test error")
