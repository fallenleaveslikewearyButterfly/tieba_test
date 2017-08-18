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
        cookie={"after_vcode":"7388f56a1ff97df1a82ddc2a4afe147c411d651b60be5b11f49a426e27db7c0132d5f5656d70840cef6b0e9621dfb31fb7a83a3062ecaa2da3ce3609a9062ec774a9cc90dfd1322d82b7b0546ceed3148c1ab9f3e7e3a3ea3bcdee1426ee4207a47b6da7e324fd4be562dde934959785394493c2d9a755b640d2e98514d775f7954653c2fcf750d4aa4522c435e0bc7477601e8e34d85e869b9772ad39dc162a"}
        self.session.cookies.update(cookie)
        resp = self.session.get(url=url,headers=headers)
        if resp.status_code != 200:
            return None
        resp.encoding = "utf-8"
        return resp.text