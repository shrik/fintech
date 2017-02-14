# -*- coding: utf-8 -*-
import scrapy
import zlib
import re

class DownloadPaperSpider(scrapy.Spider):
    name = "DownloadPaper"
    allowed_domains = ["hibor.com.cn"]
    start_urls = ['http://www.hibor.com.cn/microns_2.html']

    # customized
    host = "http://www.hibor.com.cn"
    dologin_path = "/toplogin.asp?action=login"
    acc = "bitstyle11"
    pwd = "springs"

    index = 0
    page_urls = None
    cookiejar = None
    
# download URL: http://www.hibor.com.cn/webdownload.asp?uname=bitstyle11&did=2014647&degree=1&baogaotype=15&fromtype=21


    def parse(self, response):
        DownloadPaperSpider.generate_page_urls()
        yield self.login(callback=self.after_login)
        


    def login(self, callback=None):
        dologin_url = self.host + self.dologin_path
        return scrapy.FormRequest(dologin_url, 
                                 callback=callback,
                                 formdata={'name': self.acc, 'pwd': self.pwd, 'checkbox': 'on'},
                                 meta={'cookiejar': 1})

    def generate_page_urls():
        f = open("./paper.csv","r")
        items = f.read().split("\n")
        items = list(filter(len, items))
        DownloadPaperSpider.page_urls = [(item.split(",")[0], item.split(",")[1].split("-")[-1]) for item in items]
        f.close()

    def get_url(self):
        print(DownloadPaperSpider.page_urls) 
        return DownloadPaperSpider.page_urls[self.index][0]

    def get_date(self):
        return DownloadPaperSpider.page_urls[self.index][1]

    def after_login(self, response):
        self.cookiejar = response.meta['cookiejar']
        return self.scrape_page()

    def scrape_page(self):
        return scrapy.Request(self.host + self.get_url(), callback=self.get_download_url,
            meta={'cookiejar': self.cookiejar}, errback=self.errback_httpbin)

#webdownload.asp?uname=bitstyle11&did=2014647&degree=1&baogaotype=15&fromtype=21
    def get_download_url(self, response):
        print(response.body)
        download_url = re.search("webdownload.asp?uname=bitstyle11&did=.+", response.body )
        if download_url:
            return scrapy.Request(download_url, callback=store_file, meta={'cookiejar': response.meta['cookiejar']})
        else:
            self.logger.error('Error on index %s', response.request.url, self.index)
            self.index+=1
            return scrapy.scrape_page()

        

    def store_file(self, response):
        with open("/Users/yuchao/Downloads/%s.pdf" % self.index, 'wb') as f:
            f.write(zlib.decompress(response.body, 16+zlib.MAX_WBITS))
        print("%s downloaded" % self.index)
        self.index += 1
        return scrapy.scrape_page()

    def errback_httpbin(self, failure):
        request = failure.request
        self.logger.error('Error on page %s index %s', request.url, self.index)
        self.index+=1
        return scrapy.scrape_page()

    


        

