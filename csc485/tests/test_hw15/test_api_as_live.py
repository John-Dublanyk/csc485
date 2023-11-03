"""
Testable things-
first(get endpoint) -
make sure the GET request with a query string work.
see if it accepts params and able to accociate their strength with 'good' or 'bad'
make sure the returned data is correct
make sure the paramateres are correctly asscoated with good and bad and nothing can sneak by
Second(post endpoint) -
Make sure the post requests with a JSON payload.
test to very the payload has the correct inputs and is able to returns the correct JSON response.
Test to see how JSON payload reacts with the HTTP request.
Would the below #code be considered a conditional test within the API code?
#if 'password' not in data:
#return jsonify({"error": "Missing key 'password' in the JSON payload"}), 400
verify the JSON payload to make sure it has proper assocatiaton to make is considered a good or bad password
Third(test the evaluate_strength function) -
test various password inputs to ensure it correctly assesses password strength.
we are testing to see what a strong password with only special characters does.
we look for a strong password with bot normal and special character.
look at weak password with just normal characters, looking for it not to pass.
we see what happens when you add numbers to the password, hopping it does not pass
we are make sure no password is not accepted
fourth(error) -
check for json error
Fifth(application)
very the application is able to integrate with the testable things provided.
Some of the stuff i just dont know how to go about testing it.
"""
import pytest
from csc485.projects.hw15.api import get_password_strength_by_get, get_password_strength_by_post


BASE_URL = 'http://127.0.0.1:5000'

@pytest.fixture
def test_client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.mark.parametrize('password', [
    "goodpassword",
    "securepassword123!",
    "weak",
    "password123",
    "",
    " ",
])
def test_evaluate_strength(test_client, password):
    """
    Testing the strength for different password cases, we are looking how strong each possible password can be.
    """
    request_type = {
        "goodpassword": "get",
        "securepassword123!": "post",
        "weak": "get",
        "password123": "post",
        "": "get",
        " ": "post",
    }

    if request_type[password] == "get":
        response = test_client.get(f'/get_strength?password={password}')
    else:
        payload = {"password": password}
        response = test_client.post('/get_strength', json=payload)

    assert response.status_code == 200
    data = response.get_json()
    assert data['password'] == password
    assert data['strength'] == "good" if request_type[password] == "get" else "bad"

def test_get_endpoint_live():
    response = requests.get(f'{BASE_URL}/get_strength?password=goodpassword')
    assert response.status_code == 200
    data = response.json()
    assert data['password'] == 'goodpassword'
    assert data['strength'] == 'good'

def test_post_endpoint_live():
    payload = {"password": "securepassword123!"}
    response = requests.post(f'{BASE_URL}/get_strength', json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data['password'] == "securepassword123!"
    assert data['strength'] == 'good'
