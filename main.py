import requests

url = "http://www.xinfadi.com.cn/getPriceData.html"

param = {
    "limit": 100,
    "current": 1,
    "pubDateStartTime": "2024/10/08",
    "pubDateEndTime": "2024/10/08",
    "prodPcatid": "",
    "prodCatid": "",
    "prodName": "",
}

def download_one_page():
    resp = requests.post(url = url, params = param)
    print(resp.json())
    resp.close()


if __name__ == '__main__':
    download_one_page()
