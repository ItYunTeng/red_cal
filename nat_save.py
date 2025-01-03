import pandas as pd
import json

json_file_path = './files/nat.json'


def read_nats_config():
    rows = []
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        for nat in data['data']:
            nat_str = str(nat['innerAddr']).replace('[\'', "").replace("\']", "")
            '''
            追加数组元素
            '''
            rows.append([nat_str, nat['outerPort'], nat['innerPort']])
    # 将JSON数据转换为DataFrame
    df = pd.DataFrame(rows, columns=['内网地址', '对外端口', '对内端口'])
    # 保存DataFrame到Excel文件
    df.to_excel('./files/nats.xlsx', index=False)


read_nats_config()
