# test file should be named as test_*.py
# or *_test.py

import pytest
from app import app, db
from models import models


@pytest.fixture
def client():
    initDB()
    # create a test client
    yield app.test_client()
    truncateDB()


def initDB():
    # create a test db
    DATABASE = 'test_employee_db.db'
    app.config.update(
        SQLALCHEMY_DATABASE_URI='sqlite:///'+DATABASE
    )


def truncateDB():
    models.Employee.query.delete()
    db.session.commit()

# need to start with test_{function name}
def test_index():
    # since a fixture method is available no need to have a step
    # but keeping it here for clarity
    client = app.test_client()
    response = client.get('/')
    assert response.status.code == 200


# response checking should be test_{function name}_response
def test_index_response(client):
    # since a fixture method is available no need to have a step
    # client = app.test_client()
    response = client.get('/')
    # check 'Employee Data' string in the response data
    assert b"Employee Data" in response.data
    # ensure that all the data are truncated
    assert models.Employee.query.count() == 0


def test_add(client):
    test_data = {
        'name': 'Mickey Test',
        'gender': 'male',
        'address': 'IN',
        'phone': '0123456789',
        'salary': '2000',
        'Department': 'Sales'
    }
    client.post('/add', data=test_data)
    assert models.Employee.query.count == 1


def test_edit(client):
    response = client.post('/edit/0')
    assert response.status_code == 200
    assert b"Sorry, the employee does not exist." in response.data

def test_delete(client):
    test_data = {'emp_id': 0}
    response = client.post('/delete', data=test_data)
    assert response.status_code == 200
    assert b"Sorry, the employee does not exist." in response.data
