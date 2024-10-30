import requests
import json

url = 'http://10.10.1.125/U9C/webapi/OA/OARcvReturn'
headers = {'Content-Type': 'application/json'}
session = requests.Session()

with open('files/data.json', 'r') as file:
    datas = json.load(file)
    for data in datas:
        response = session.post(url=url, data=data, headers=headers)
        # 获取响应结果
        data = response.text
        print(data)
