import pytest

# Importar la aplicación Flask para crear el cliente
from . import create_app

@pytest.fixture
def app():
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_test_page(client):
    response = client.get('/test')
    assert response.status_code == 200
    assert b'Testing the Flask Application Factory Pattern' in response.data

def test_page_not_found(client):
    response = client.get('/invalid_route')
    assert response.status_code == 404
