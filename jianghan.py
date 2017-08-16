__author__ = "Liang"
__Date__ = 2017 / 8 / 16
import requests
from bs4 import BeautifulSoup as bs
headers={
"Host":"tieba.baidu.com",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
}
url="http://tieba.baidu.com/f"
data={"kw":"江汉大学",
    "ie":"utf-8",
    "pn":"50"
}

session=requests.session()
resp=session.get(url=url,params=data)
resp.encoding="utf-8"
print(resp.text)
# resp2=session.get(url=url,headers=headers,data=data)
# print(resp2.status_code)
# print(resp2.text)
