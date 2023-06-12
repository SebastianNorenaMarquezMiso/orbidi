from api.models.contact import ContactCreateRequest, ContactProperties
import pytest
from unittest.mock import MagicMock, patch
from clients.hubspot_client import HubSpotClient


@pytest.fixture
def mock_requests():
    return MagicMock()


@patch('clients.hubspot_client.requests.post')
def test_create_contact(mock_post):
    # Configurar el mock para la respuesta de la API de HubSpot
    contact_request = ContactCreateRequest(properties=ContactProperties(firstname="John", lastname="Doe", website="test.com", email="john.doe@example.com", phone="3333333333"))
    response_data = {"id": "123", "name": "John Doe", "email": "john.doe@example.com"}

    # Mockear el método post y su respuesta
    mock_post.return_value.json.return_value = response_data
    # Crear una instancia del cliente de HubSpot
    client = HubSpotClient()

    # Llamar a la función de creación de contacto
    response = client.create_contact(contact_request)

    assert response == response_data


def test_update_status_synced_error(mock_requests):
    # Configurar el mock para la respuesta de la API de HubSpot con un error
    contact_id = "123"
    error_message = "404 Client Error: Not Found for url: https://api.hubapi.com/crm/v3/objects/contacts/123"
    mock_requests.patch.return_value.json.return_value = {"error": error_message}
    mock_requests.patch.return_value.status_code = 400
    # Crear una instancia del cliente de HubSpot
    client = HubSpotClient()
    # Llamar a la función de actualización de estado sincronizado
    with pytest.raises(Exception) as e:
        client.update_status_synced(contact_id)
    assert str(e.value) == error_message
