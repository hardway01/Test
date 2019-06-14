import requests
from pprint import pprint


base_url = 'https://jsonplaceholder.typicode.com/'
resource = 'users'

response = requests.get(base_url + resource + '/2')  # https://jsonplaceholder.typicode.com/users/2

print(response.status_code)
pprint(response.headers, indent=2)
pprint(response.json())

user = response.json()
user['username'] = 'MyName'

response = requests.post(base_url + resource, user) #https://jsonplaceholder.typicode.com/users/
print(response.status_code)
pprint(response.headers, indent=2)
pprint(response.json())

