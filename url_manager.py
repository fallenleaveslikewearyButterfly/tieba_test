__author__ = "Liang"
__Date__ = 2017 / 8 / 17


class url_manager(object):
    def __init__(self):
        self.new_urls=[]
        self.old_urls=[]

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.append(url)

    def add_new_urls(self):
        for x in range(50,100001)[::-50]:
            url="http://tieba.baidu.com/f?kw=%E6%B1%9F%E6%B1%89%E5%A4%A7%E5%AD%A6&ie=utf-8&pn="+str(x)
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        return new_url
