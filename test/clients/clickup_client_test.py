import pytest
from unittest.mock import patch
from clients.clickup_client import ClickUpClient


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    def raise_for_status(self):
        pass


@pytest.fixture
def requests_mock():
    with patch('clients.clickup_client.requests') as mock_requests:
        yield mock_requests


def test_create_task(requests_mock):
    # Configurar el mock para la respuesta de la API de ClickUp
    task_data = {
        "name": "Test Task",
        "description": "This is a test task"
    }
    response_data = {"id": "123", "name": "Test Task"}
    requests_mock.post.return_value = MockResponse(response_data, 201)

    # Crear una instancia del cliente de ClickUp
    client = ClickUpClient()

    # Llamar a la función de creación de tarea
    response = client.create_task(task_data)

    assert response == response_data


def test_create_task_error(requests_mock):
    # Configurar el mock para la respuesta de la API de ClickUp con un error
    task_data = {
        "name": "Test Task",
        "description": "This is a test task"
    }
    error_message = "Error creating task"
    requests_mock.post.return_value = MockResponse(error_message, 400)

    # Crear una instancia del cliente de ClickUp
    client = ClickUpClient()

    # Llamar a la función de creación de tarea
    response = client.create_task(task_data)

    assert response == error_message
