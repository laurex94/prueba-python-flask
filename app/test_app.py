from app import create_app  # Importa create_app desde el paquete app
import pytest
import requests

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

def test_get_all_greetings():
    response = requests.get('http://localhost:5000/saludos')
    assert response.status_code == 200

def test_create_new_greeting():
    new_greeting_data = {'mensaje': 'Buenos días'}
    response = requests.post('http://localhost:5000/saludos', json=new_greeting_data)
    assert response.status_code == 200

def test_get_greeting_by_id():
    response = requests.get('http://localhost:5000/saludos/1')
    assert response.status_code == 200