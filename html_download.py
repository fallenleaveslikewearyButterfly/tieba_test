import requests

__author__ = "Liang"
__Date__ = 2017 / 8 / 17

class html_downloader(object):
    def __init__(self):
        self.session = requests.session()

    def download(self, url):
        if url is None:
            return None
        headers = {
            "Host": "tieba.baidu.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        }
        resp = self.session.get(url=url,headers=headers)
        if resp.status_code != 200:
            return None
        resp.encoding = "utf-8"
        return resp.text