'''
    python          json
    
    dict            object
    list,tuple      array
    str             string
    int,float       number
    True            true
    False           false
    None            null
'''


import urllib.request
import urllib.parse
import json


def GET(param, header=None):
    if header:
        req = urllib.request.Request(param, headers=header)
    else:
        req = urllib.request.Request(param)
    data = urllib.request.urlopen(req).read().decode('utf-8')
    print(data)


def POST(param, data):
    data = urllib.parse.urlencode(data).encode()
    req = urllib.request.Reuqest(param, data=data)
    res = urllib.request.urlopen(req).read().decode('utf-8')


url = "http://api.welcome.kakao.com"
_data = GET(url)
