import requests
from pprint import pprint

base_url = 'https://jsonplaceholder.typicode.com/'
resource = 'comments'

response = requests.get(base_url + resource)  # https://jsonplaceholder.typicode.com/comments/
all_comments = response.json()

ids_dict = {}
for comment in all_comments:
    if not ids_dict.get(comment['postId']):
        ids_dict[comment['postId']] = []
        ids_dict[comment['postId']].append(comment)


for comment in all_comments:
    if comment['email'].endswith('.com'):
        comment["body"] = ""
#        print(ids_dict.items())

#response = requests.post(base_url + resource, ) #https://jsonplaceholder.typicode.com/comments/
#print(response.status_code)
#pprint(response.headers)
#pprint(response.json())

comment_to_update = None
for comment in all_comments:
    if comment['id'] == 6:
        comment["body"] = "New Body"
        comment_to_update = comment
print(comment_to_update['id'])
response = requests.put('https://jsonplaceholder.typicode.com/comments/'+ str(comment_to_update['íd']), comment_to_update)

print(response.json())
t = 1


