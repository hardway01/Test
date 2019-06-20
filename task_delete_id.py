import requests
from pprint import pprint

base_url = 'https://jsonplaceholder.typicode.com/'
resource = 'comments'

response = requests.get(base_url + resource)  # https://jsonplaceholder.typicode.com/comments/
all_comments = response.json()

new_comments = [i for i in all_comments if not (i['id'] == 233)]

ids_dict = {}
for comment in new_comments:
    if not ids_dict.get(comment['postId']):
        ids_dict[comment['postId']] = []
        ids_dict[comment['postId']].append(comment)

# print(ids_dict.items())


for k, v in ids_dict.items():
    f = open(str(k)+'.json', 'w+')
    f.write(str(v))
    f.close()