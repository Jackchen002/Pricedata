import  requests
import json
import xlwt

url = "http://www.xinfadi.com.cn/getPriceData.html"

param = {
    "limit": 40,
    "current": 1,
    "pubDateStartTime": "2024/10/08",
    "pubDateEndTime": "2024/10/08",
    "prodPcatid": "",
    "prodCatid": "",
    "prodName": "",
}

def download_one_page():
    resp = requests.post(url = url, params = param)

    title = list(set([j for i in resp.json() for j in i]))
    book = xlwt.Workbook()
    sheet = book.add_sheet('Sheet1', cell_overwrite_ok=True)  # 添加一个sheet页
    for i in range(len(title)):  # 循环列
        sheet.write(0, i, title[i])  # 将title数组中的字段写入到0行i列中
    for i, it in enumerate(resp.json()):
        for j, k in enumerate(title):
            sheet.write(1 + i, j, it[k])
    book.save('Pricedata.xls')

    resp.close()


if __name__ == '__main__':
    download_one_page()