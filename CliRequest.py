import urllib.request
import requests
import http.client

# 第三种方式
url = "http://example.com"  # 替换为你要请求的URL

# 发送GET请求
response = urllib.request.urlopen(url)
data = response.read()  # 获取响应结果
print(data)

# 发送POST请求
data = b"param1=value1&param2=value2"  # 替换为你要发送的POST数据
response = urllib.request.urlopen(url, data)
data = response.read()  # 获取响应结果
print(data)
# 第二种方式
# 发送GET请求

# 定义cookie字典
cookies = {'key1': 'value1', 'key2': 'value2'}
session = requests.Session()
# 将Cookie插入Headers请求头
headers = {
    'User-Agent': 'Mozilla/5.0',
    'Cookie': 'your_cookie_here'
}
response = requests.get(url, cookies=cookies)
# response = session.get("https://www.example.com", headers=headers)
# session.close()
data = response.text  # 获取响应结果
print(data)

# 发送POST请求
data = {"param1": "value1", "param2": "value2"}  # 替换为你要发送的POST数据
response = requests.post(url, data=data)
data = response.text  # 获取响应结果
print(data)
# 第一种方式
url = "example.com"  # 替换为你要请求的URL
path = "/path/to/resource"  # 替换为你要请求的资源路径

# 发送GET请求
conn = http.client.HTTPSConnection(url)
conn.request("GET", path)
response = conn.getresponse()
data = response.read()  # 获取响应结果
print(data)

# 发送POST请求
conn = http.client.HTTPSConnection(url)
payload = "param1=value1&param2=value2"  # 替换为你要发送的POST数据
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
conn.request("POST", path, body=payload, headers=headers)
response = conn.getresponse()
data = response.read()  # 获取响应结果
print(data)
