import random

import pytest
import requests


def test_single_user():
    response = requests.get('https://reqres.in/api/users/2')
    response_get = response.json()
    assert response_get['data']['id'] == 2
    assert response_get['data']['email'] == 'janet.weaver@reqres.in'
    assert response_get['data']['first_name'] == 'Janet'
    assert response_get['data']['last_name'] == 'Weaver'
    assert response_get['data']['avatar'] == 'https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg'


@pytest.mark.parametrize('random_id', [random.randint(1, 10), random.randint(1, 10)])
@pytest.mark.parametrize('resource_endpoint', ['users', 'unknown', 'login', 'register'])
def test_single_resource(random_id, resource_endpoint):
    response = requests.get(f'https://reqres.in/api/{resource_endpoint}/{random_id}')
    assert response.status_code == 200
    assert isinstance(response.json()['data']['id'], int)


@pytest.mark.parametrize('random_integer', [random.randint(100, 1000), random.randint(100, 1000)])
@pytest.mark.parametrize('resource_name', ['users', 'unknown'])
def test_single_resource_not_found(random_integer, resource_name):
    response = requests.get(f'https://reqres.in/api/{resource_name}/{random_integer}')
    assert response.status_code == 404


@pytest.fixture()
def new_user():
    new_user = {"name": "morpheus", "job": "leader"}
    return new_user


def test_create_new_user(new_user):
    response = requests.post('https://reqres.in/api/users/', new_user)
    response_user = response.json()
    assert response.status_code == 201
    assert response_user["name"] == new_user["name"]
    assert response_user["job"] == new_user["job"]


def test_update_user():
    change_user = {"name": "morpheus", "job": "zion resident"}
    response = requests.put('https://reqres.in/api/users/2/', change_user)
    response_user = response.json()
    assert response.status_code == 200
    assert response_user["name"] == change_user["name"]
    assert response_user["job"] == change_user["job"]


def test_delete_user():
    response = requests.delete('https://reqres.in/api/users/2/')
    assert response.status_code == 204


@pytest.mark.parametrize('register',
                         [({"email": "eve.holt@reqres.in", "password": "pistol"}),
                          {"email": "eve.holt@reqres.in", "password": "cityslicka"}])

def test_post_register(register):
    response = requests.post('https://reqres.in/api/register/', register)
    response_register = response.json()
    assert response.status_code == 200
    assert response_register["id"] == 4
    assert response_register["token"] == "QpwL5tke4Pnpja7X4"

@pytest.mark.parametrize('wrong_register',
                         [({"email": "eve.holt@reqres.in"})])
def test_post_wrong_register(wrong_register):
    response = requests.post('https://reqres.in/api/register/', wrong_register)
    assert response.status_code == 400


def test_correct_login():
    new_login = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post('https://reqres.in/api/login/', new_login)
    response_login = response.json()
    assert response.status_code == 200
    assert response_login["token"] == "QpwL5tke4Pnpja7X4"


def test_wrong_login():
    new_login = {"email": "peter@klaven"}
    response = requests.post('https://reqres.in/api/login/', new_login)
    response_login = response.json()
    assert response.status_code == 400
    assert response_login["error"] == "Missing password"
