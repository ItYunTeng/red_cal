import requests
import json
import csv

url = 'http://oa.gmerit.com:8090/tic/core/log/tic_core_log_main/ticCoreLogMainIndex.do?method=list&isError=0&fdType=&fdAppType=5&fdEnviromentId=&q.funcName=ERP%E6%89%A3&q.s_raq=0.5145287110385586&pageno=1&rowsize=50&pagingtype=default'
# 将Cookie插入Headers请求头
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'LtpaToken=AAECAzY3MjE3Rjg5NjcyMjI4NDkxMDAwMDE5MPqrD7AoacAOFPhxXgXE7X++bsem; j_lang=zh-CN; SESSION=NDEzYjY1NDYtYTk1NS00ZGE0LWIxNzUtNjkxNGJiODFkNWQ3; JSESSIONID=4E91821D1B050B3F8B66047DEA2F48EE',
    'Host': 'oa.gmerit.com:8090',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

session = requests.Session()

response = session.get(url=url, headers=headers)
session.close()
# 获取响应结果
data = response.text
print(data)
jst = json.loads(data)['datas']
print(jst)
# 多行多列的列表定义
datas = [[0 for col in range(0)] for row in range(len(jst))]
for i, j in enumerate(jst):
    v = j[0]['value']
    print(v)
    datas[i].append(v)

with open('files/flow.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(datas)
