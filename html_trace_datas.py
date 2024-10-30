import urllib.request as ur
from bs4 import BeautifulSoup
import json
import csv

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'LtpaToken=AAECAzY3MjE3Rjg5NjcyMjI4NDkxMDAwMDE5MPqrD7AoacAOFPhxXgXE7X++bsem; j_lang=zh-CN; SESSION=NDEzYjY1NDYtYTk1NS00ZGE0LWIxNzUtNjkxNGJiODFkNWQ3; JSESSIONID=4E91821D1B050B3F8B66047DEA2F48EE',
    'Host': 'oa.gmerit.com:8090',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

req_url = 'http://oa.gmerit.com:8090/tic/core/log/tic_core_log_main/ticCoreLogMain.do?method=view&fdId='


def get_datas(url_page):
    req = ur.Request(url=url_page, headers=headers)
    page = ur.urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')
    print(soup)
    table = soup.find('table', attrs={'class', 'tb_normal'})
    if table is None:
        raise ValueError("文档不存在")

    results = table.find_all('tr')

    rows = [['dataBody']]
    for i in range(len(results)):
        if i == 6:
            tr = results[i]
            data = tr.find_all('td')
            if len(data) == 0:
                continue
            data_body = data[1].getText()

            rows.append([data_body])
            print(rows)

    data = rows[1]
    jst = json.dumps(data).replace('\\r', '').replace('\\n', '').replace('\\t', '').replace(' ', '')
    jdata = json.loads(json.loads(jst)[0])['body']
    print(jdata)
    return jdata


def write_data_json(datas):
    with open("files/data.json", "w", encoding='utf-8') as json_file:
        json.dump(datas, json_file, ensure_ascii=False)


def data_save():
    re_datas = []
    with open('files/flow.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        # 遍历每一行数据
        for row in reader:
            # 处理每一行数据
            fd_id = row.pop(0)
            page_url = req_url + fd_id
            print(page_url)

            try:
                re_data = get_datas(page_url)
            except ValueError as e:
                print(e)
                continue
            else:
                re_datas.append(re_data)

    write_data_json(re_datas)


if __name__ == '__main__':
    data_save()
