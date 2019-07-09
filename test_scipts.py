
import random

import pytest
import requests

# endpoints for test scripts:
#/Post
#/comments
#/albums
#/photos
#/todos
#/users

#post
#testscript1: check if max post is 100
#testscript2: check if all fields(keys) are there
#testscript3: create new post
#testscript4: check if title exists in post
#comment
#testscript5: Check if max comment is 500
#testscript6: Check if all fields(keys) are there
#testscript7: create new comment
#testscript8: check email in comment
#albums
#testscript1: check if max albums is 100
#Delete album 2




def test_max_post_100():
  response = requests.get('https://jsonplaceholder.typicode.com/posts/100')
  assert response.status_code == 200

def test_max_post_100_2():
  response = requests.get('https://jsonplaceholder.typicode.com/posts/101')
  assert response.status_code == 404

def test_post_fields():
  postid = random.randint(1,100)
  expected_fields = {"userId", "id", "title", "body"}
  response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{postid}')
  assert expected_fields == set(response.json().keys())

def test_create_new_post():
  new_post = {"userId": 10, "id": 101, "title": "New Post", "body": "This is a new post"}
  response = requests.post('https://jsonplaceholder.typicode.com/posts/', new_post)
  assert isinstance(response.json()['id'], int)
  assert response.json()["id"] == 101
  assert response.json()["title"] == "New Post"
  assert response.json()["body"] == "This is a new post"

# is the same as:

  assert response.json()["id"] == new_post["id"]
  assert response.json()["title"] == new_post["title"]
  assert response.json()["body"] == new_post["body"]

def test_title_exist_in_post():
  response = requests.get('https://jsonplaceholder.typicode.com/posts/3')
  assert response.json()["title"] == "ea molestias quasi exercitationem repellat qui ipsa sit aut"

def test_max_comments_500():
  response = requests.get('https://jsonplaceholder.typicode.com/comments/500')
  assert response.status_code == 200

def test_max_post_500_2():
  response = requests.get('https://jsonplaceholder.typicode.com/comments/501')
  assert response.status_code == 404

def test_comment_fields():
  commentid = random.randint(1,500)
  expected_fields = {"postId", "id", "name", "email", "body"}
  response = requests.get(f'https://jsonplaceholder.typicode.com/comments/{commentid}')
  assert expected_fields == set(response.json().keys())

def test_create_new_comment():
  new_comment = {"postId": 101, "id": 501, "name": "Andries Fokkema", "email": "andries_fokkema@epam.com", "body": "This is a new comment"}
  response = requests.post('https://jsonplaceholder.typicode.com/comments/', new_comment)
  assert isinstance(response.json()['id'], int)
  assert response.json()["id"] == new_comment["id"]
  assert response.json()["postId"] == new_comment["postId"]
  assert response.json()["name"] == new_comment["name"]
  assert response.json()["email"] == new_comment["email"]
  assert response.json()["body"] == new_comment["body"]

def test_email_exist_in_comment():
  response = requests.get('https://jsonplaceholder.typicode.com/comments/3')
  assert response.json()["email"] == "Nikita@garfield.biz"

def test_max_albums_100():
  response = requests.get('https://jsonplaceholder.typicode.com/albums/100')
  assert response.status_code == 200

def test_max_albums_100_2():
  response = requests.get('https://jsonplaceholder.typicode.com/albums/101')
  assert response.status_code == 404

def test_delete_album():
  response = requests.delete('https://jsonplaceholder.typicode.com/albums/2')
  assert response.json() == {}