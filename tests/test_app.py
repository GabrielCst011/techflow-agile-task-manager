import pytest
from src.app import create_app, db, Task

@pytest.fixture
def client():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})
    with app.app_context():
        db.create_all()  # cria tabelas explicitamente
        yield app.test_client()
        db.drop_all()  # limpa após o teste

def test_create_task(client):
    response = client.post('/tasks', json={'title': 'Test Task'})
    assert response.status_code == 201
    assert response.get_json()['title'] == 'Test Task'
