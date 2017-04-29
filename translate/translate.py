import requests
import sys
import json

youdao = 'http://fanyi.youdao.com/openapi.do'
payload = {'keyfrom': 'OnlineBookstore',
           'key': '610224539',
           'type': 'data',
		   'doctype': 'json',
		   'version': '1.1',
		   'q': 'hello world'
}

def translate(query_str):
    query_str = query_str.strip()
    if query_str:
        payload['q'] = query_str

    response = requests.get(youdao, params=payload)
    d = response.json()
    errorcode = d.get('errorCode', 0)
    if not errorcode:
        translation = d.get('translation', '')
        explains = d.get('basic', {}).get('explain', '')
        translation.extend(explains)
        return translation
    elif errorcode == 20:
        return 'Text too long!'
    elif errorcode == 40:
        return 'Language not support!'
    elif errorcode == 50:
        return 'Invalid key!'
    else:
        return 'Can not translate!'

def command_line_runner():
    query_str = sys.argv[1]
    trans = translate(query_str)
    for t in trans:
        print(t)
