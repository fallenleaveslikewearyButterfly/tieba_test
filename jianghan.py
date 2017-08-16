__author__ = "Liang"
__Date__ = 2017 / 8 / 16
import requests
import re
from bs4 import BeautifulSoup as bs
headers={
"Host":"tieba.baidu.com",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
}
url="http://tieba.baidu.com/f"
data={"kw":"江汉大学",
    "ie":"utf-8",
    "pn":"0"
}
session=requests.session()
resp=session.get(url=url,params=data)
resp.encoding="utf-8"
soup=bs(resp.text,'html.parser')
everytie=soup.find_all("li",class_=" j_thread_list clearfix")
#获取所有发帖者
output=open("result.txt","w",encoding="utf-8")
for j in everytie:
    Auth=j.find("span",class_=re.compile("tb_icon_author .*"))
    title=j.find("a",class_="j_th_tit ")
    creattime=j.find("span",class_="pull-right is_show_create_time").get_text()
    lstrpltm=j.find("span",class_="threadlist_reply_date pull_right j_reply_data").get_text()

    output.write(Auth.attrs["title"].replace("主题作者: ","")+","+title.attrs["title"]+","+"http://tieba.baidu.com"+title.attrs["href"]+","+creattime+","+lstrpltm+"\n")
output.close()

