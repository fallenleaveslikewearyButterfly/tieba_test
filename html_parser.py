import re

__author__ = "Liang"
__Date__ = 2017 / 8 / 17

from bs4 import BeautifulSoup as bs, BeautifulSoup


class html_parser(object):
    def parser(self, html_cont):
        if  html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        everytie = soup.find_all("li", class_=" j_thread_list clearfix")
        res_data = self._get_new_data(everytie)
        return res_data

    def _get_new_data(self, child):
        items=[]
        for j in child:
            Auth = j.find("span", class_=re.compile("tb_icon_author .*"))
            title = j.find("a", class_="j_th_tit ")
            item = {}
            try:
                item["Author"] = Auth.attrs["title"].replace("主题作者: ", "")
            except:
                print("Author")
                print(Auth)
            try:
                item["topic"] = title.attrs["title"]
            except:
                print("topic")
                print(title)
            try:
                item["link"] = "http://tieba.baidu.com" + title.attrs["href"]
            except:
                print("link")
                print(title)
            try:
                item["creattime"] = j.find("span", class_="pull-right is_show_create_time").get_text()
            except:
                print("creattime")
                print(j)
            try:
                item["lastreply"] = j.find("span", class_="threadlist_reply_date pull_right j_reply_data").get_text()
            except:
                print("lastreply")
                print(j)
            try:
                item["followee"] = j.find("span", class_="threadlist_rep_num center_text", title="回复").get_text()
            except:
                print("followee")
                print(j)
            try:
                item["authpage"] = "http://tieba.baidu.com/" + Auth.find("a", class_=re.compile("frs-author-name .*")).attrs["href"]
            except:
                print("authpage")
                print(Auth)
            items.append(item)
        return items
