# test file should be named as test_*.py
# or *_test.py
from app import app


# need to start with test_{function name}
def test_index():
    client = app.test_client()
    response = client.get('/')
    assert response.status.code == 200


# response checking should be test_{function name}_response
def test_index_response():
    client = app.test_client()
    response = client.get('/')
    assert b"Employee Data" in response.data
