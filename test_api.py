import random

import pytest
import requests


def test_get_status_code():
  response = requests.get('https://jsonplaceholder.typicode.com/users/8')
  assert response.status_code == 200


def test_get_status_code_failing():
  response = requests.get('https://jsonplaceholder.typicode.com/users/13')
  assert response.status_code == 200


def test_get_status_code_failing_custom_message():
  response = requests.get('https://jsonplaceholder.typicode.com/users/13')
  assert response.status_code == 200, f"Incorrect status code {response.status_code}"


def test_get_non_empty():
  response = requests.get('https://jsonplaceholder.typicode.com/users/11')
  assert not response.json()


def test_get_id():
  _id = random.randint(1, 10) # 1-10 3
  response = requests.get(f'https://jsonplaceholder.typicode.com/users/{_id}') # 3
  assert response.json()['id'] == _id, response.json() # 3 == 3


param_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


@pytest.mark.parametrize('_id', range(1, 100))
def test_get_id_parametrize(_id):
  response = requests.get(f'https://jsonplaceholder.typicode.com/users/{_id}')
  assert response.json()['id'] == _id
