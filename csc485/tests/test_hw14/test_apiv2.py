import json
import pytest
from csc485.csc485.projects.hw14.api import app

#Testable things
#First we will check if the API correctly identifies a strong password
#Second we will check if the API correctly identifies a password with special characters
#Third we will Check if the API correctly identifies a long password
#fourth we will  Check if the API correctly identifies a valid password
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


"""Test for a strong password"""
def test_strong_password(client):
    password = "SuperSecureP@ssw0rd!"
    response = client.get(f'/get_strength?password={password}')
    data = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert 'password' in data
    assert 'strength' in data
    assert data['strength'] == 'bad'

"""Test for a password with special characters"""
def test_special_character_password(client):
    password = "Pass!withSpecialCharacter"
    response = client.get(f'/get_strength?password={password}')
    data = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert 'password' in data
    assert 'strength' in data
    assert data['strength'] == 'bad'

"""Test for a long password"""
def test_long_password(client):
    password = "A" * 100
    response = client.get(f'/get_strength?password={password}')
    data = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert 'password' in data
    assert 'strength' in data
    assert data['strength'] == 'bad'

"""Test for a valid password"""
def test_valid_password(client):
    password = "SecureP@ssw0rd"
    response = client.get(f'/get_strength?password={password}')
    data = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert 'password' in data
    assert 'strength' in data
    assert data['strength'] == 'bad'