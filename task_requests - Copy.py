# fetch all comments per post and save to files with structure:
# 'post_{id}.json' (id should be changed according to post). Each file
# should contains all comments for post with {id}

# set "body" of comment to "" empty string, if "email" contains ".com"
# send post request to the API

# delete comment with "id"=233

# send put request to create new comment for post with "id"=3. You can choose
# any values for rest parameters

# push code to repository

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
    if ids_dict.get(comment['id']) == 8:
        del ids_dict[comment['id']]
# print(ids_dict.items())

# for k, v in ids_dict.items():
#    f = open(str(k)+'.json', 'w+')
#    f.write(str(v))
#    f.close()
