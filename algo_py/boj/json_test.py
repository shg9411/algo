'''
when using form
headers["Content-Type"] = "application/x-www-form-urlencoded"

if needed
headers["Authorization"] = "Bearer {token}"
'''

import requests
from requests.structures import CaseInsensitiveDict


def GET(url, param=None):
    # r.text, r.json(), etc..
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = "123"
    r = requests.get(url, headers=headers, params=param)
    print(r.status_code)
    print(r.headers)
    print(r.text)


def POST(url, data=None):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    r = requests.post(url, headers=headers, data=data)
    print(r.status_code)
    print(r.headers)
    print(r.text)


POST("https://httpbin.org/response-headers?freeform=as")
GET("https://httpbin.org/response-headers?freeform=d")
