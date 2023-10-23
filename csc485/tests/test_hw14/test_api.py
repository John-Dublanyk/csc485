import json
import pytest
from csc485.projects.hw14.api import app  # Replace 'path_to_the_api_code' with the actual path to your API code
"""the first two test are your test. First- we are looking for the happy path, which is where we check to make sure 
there are no error and all of our input and outputs work.
Second- we are looking for expected errors.
Third- we are testing to see what we would get with no password, and making sure it is bad for not having a password.
Fourth- We are testing in order to gage strength of passwords, we are looking for a strong password.
Fifth- we are testing for weak passwords to ensure that is not a problem
"""

# This is a pytest fixture
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# This is a simplified happy path test
def test_expect_good(client):
    response = client.get('/get_strength?password=%%%%%%%')
    assert response.status_code == 200
    data = json.loads(response.data.decode())

    assert data.get('password') == '%%%%%%%'
    assert data.get('strength') == 'good'


# This is an example negative test
def test_api_error(client):
    password = '#password'
    response = client.get(f"/get_strength?password={password}")
    assert response.status_code == 200  # The API should return a response
    data = json.loads(response.data.decode())
    assert data.get('password') == '#password'
    assert data.get('strength') == 'bad'


# This is testing that an empty password should be considered bad
def test_empty_password(client):
    response = client.get('/get_strength?password=')
    assert response.status_code == 200
    data = json.loads(response.data.decode())
    assert data.get('password') == ''
    assert data.get('strength') == 'bad'


# This is testing for a strong password
def test_strong_password(client):
    response = client.get('/get_strength?password=StrongPassword123!')
    assert response.status_code == 200
    data = json.loads(response.data.decode())
    assert data.get('password') == 'StrongPassword123!'
    assert data.get('strength') == 'good'


# this is testing for a very weak password
def test_very_weak_password(client):
    response = client.get('/get_strength?password=123456')
    assert response.status_code == 200
    data = json.loads(response.data.decode())
    assert data.get('password') == '123456'
    assert data.get('strength') == 'bad'
