import pytest


@pytest.fixture
def app():
    app = create_app(
        test_config={'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_clients(client):
    response = client.get('/clients')
    assert response.status_code == 200
    assert len(response.json) == 0  # Assuming no clients in the test database


def test_create_client(client):
    response = client.post(
        '/clients', json={'phone_number': '1234567890', 'name': 'John Doe'})
    assert response.status_code == 201
    assert response.json['message'] == 'Client created successfully'


def test_get_appointments(client):
    response = client.get('/appointments')
    assert response.status_code == 200
    # Assuming no appointments in the test database
    assert len(response.json) == 0


def test_create_appointment(client):
    response = client.post(
        '/appointments', json={'date': '2023-12-01', 'time': '10:00 AM', 'dog_id': 1})
    assert response.status_code == 201
    assert response.json['message'] == 'Appointment created successfully'


def test_create_appointment_missing_fields(client):
    response = client.post('/appointments', json={'date': '2023-12-01'})
    assert response.status_code == 400
    assert response.json['error'] == 'Missing required fields'
