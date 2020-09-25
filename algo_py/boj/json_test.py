'''
when using form
headers["Content-Type"] = "application/x-www-form-urlencoded"

if needed
headers["Authorization"] = "{종류} {token}"
'''

import requests
import json
from requests.structures import CaseInsensitiveDict


def GET(url, param=None):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = ""
    r = requests.get(url, headers=headers, params=param)
    print(r.status_code)
    # print(r.headers)
    try:
        print(r.json())
    except:
        print(r.text)
    # r.text, r.json(), r.content, r.encoding, etc..


def POST(url, data=None):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = ""
    data = dict()
    data['userId']=1
    data['id']=3
    data['title']='33'
    data['body']='test'
    r = requests.post(url, headers=headers, data=json.dumps(data))
    print(r.status_code)
    # print(r.headers)
    try:
        print(r.json())
    except:
        print(r.text)


POST("https://jsonplaceholder.typicode.com/posts")
#GET("https://jsonplaceholder.typicode.com/posts")
