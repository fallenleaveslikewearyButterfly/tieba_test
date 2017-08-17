__author__ = "Liang"
__Date__ = 2017 / 8 / 16
import data_outputer,html_download,html_parser,url_manager
class spider_main(object):
    def __init__(self):
        self.url_manager=url_manager.url_manager()
        self.output=data_outputer.data_outputer()
        self.download=html_download.html_downloader()
        self.paser=html_parser.html_parser()
    def craw(self):
        self.url_manager.add_new_urls()
        count=1
        while self.url_manager.has_new_url():
            new_url=self.url_manager.get_new_url()
            print("正在爬取 %d:%s" % (count, new_url))
            html_content= self.download.download(new_url)
            html_content=html_content.replace("<!--","")
            html_content = html_content.replace("-->", "")
            new_data= self.paser.parser(html_content)
            for j in new_data:
                self.output.insert(j)
            count=count+1


if __name__=="__main__":
    spider=spider_main()
    spider.craw()