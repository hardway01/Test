import random

import pytest
import requests


def test_single_user():
    response = requests.get('https://reqres.in/api/users/2')
    assert response.status_code == 200

    response_get = response.json()
    assert response_get['data']['id'] == 2
    assert response_get['data']['email'] == 'janet.weaver@reqres.in'
    assert response_get['data']['first_name'] == 'Janet'
    assert response_get['data']['last_name'] == 'Weaver'
    assert response_get['data']['avatar'] == 'https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg'

def test_user_not_found():
    response = requests.get('https://reqres.in/api/users/23')
    assert response.status_code == 404

def test_single_resource():
    response = requests.get('https://reqres.in/api/unknown/2')
    assert response.status_code == 200
    assert isinstance(response.json()['data']['id'], int)

def test_single_resource_not_found():
    response = requests.get('https://reqres.in/api/unknown/23')
    assert response.status_code == 404

def test_create_new_user():
    new_user = {"name": "morpheus", "job": "leader"}
    response = requests.post('https://reqres.in/api/users/', new_user)
    print(response.json())
    assert response.status_code == 201

    response_user = response.json()
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

def test_post_register():
    new_register = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = requests.post('https://reqres.in/api/register/', new_register)
    response_register = response.json()
    assert response.status_code == 200
    assert response_register["id"] == 4
    assert response_register["token"] == "QpwL5tke4Pnpja7X4"

def test_post_wrong_register():
    new_register = {"email": "sydney@fife"}
    response = requests.post('https://reqres.in/api/register/', new_register)
    assert response.status_code == 400

def test_correct_login():
    new_login = {"email": "eve.holt@reqres.in",  "password": "cityslicka"}
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



