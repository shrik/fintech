# -*- coding: utf-8 -*-
import scrapy
import zlib
import re
import cgi

class DownloadPaperSpider(scrapy.Spider):
    name = "DownloadPaper"
    allowed_domains = ["hibor.com.cn"]
    start_urls = ['http://www.hibor.com.cn/microns_2.html']

    # customized
    host = "http://www.hibor.com.cn"
    dologin_path = "/toplogin.asp?action=login"

    # acc = "prcc"
    # pwd = "gxzq201406"

    acc = "bitstyle11"
    pwd = "springs"

    index = 0
    page_urls = None
    cookiejar = None

    proxy = "http://115.29.38.207:16816"
    
# download URL: http://www.hibor.com.cn/webdownload.asp?uname=bitstyle11&did=2014647&degree=1&baogaotype=15&fromtype=21


    def parse(self, response):
        DownloadPaperSpider.generate_page_urls()
        yield self.login(callback=self.after_login)
        


    def login(self, callback=None):
        dologin_url = self.host + self.dologin_path
        return scrapy.FormRequest(dologin_url, 
                                 callback=callback,
                                 formdata={'name': self.acc, 'pwd': self.pwd, 'checkbox': 'on'},
                                 # meta={'cookiejar': 1 })#, 'proxy': self.proxy})
                                 meta={'cookiejar': 1 , 'proxy': self.proxy})

    @classmethod
    def generate_page_urls(cls):
        # f = open("./paper.csv","r")
        f = open("./hibor_0.csv","r")
        items = f.read().split("\n")
        items = list(filter(len, items))
        DownloadPaperSpider.page_urls = [(item.split(",")[0], item.split(",")[1].split("-")[-1]) for item in items]
        f.close()

    @classmethod
    def error(cls, url):
        with open("./error.log", 'a') as f:
            f.write(url + "\n")

    def get_url(self):
        return DownloadPaperSpider.page_urls[self.index][0]

    def get_date(self):
        return DownloadPaperSpider.page_urls[self.index][1]

    def after_login(self, response):
        self.cookiejar = response.meta['cookiejar']
        return self.scrape_page()

    def scrape_page(self):
        return scrapy.Request(self.host + self.get_url(), callback=self.get_download_url,
            # meta={'cookiejar': self.cookiejar}, #'proxy': self.proxy}, 
            meta={'cookiejar': self.cookiejar, 'proxy': self.proxy}, 
            errback=self.errback_httpbin)

#webdownload.asp?uname=bitstyle11&did=2014647&degree=1&baogaotype=15&fromtype=21
    def get_download_url(self, response):
        # print(response.body)
        # TODO if body equal delete/limit.html then exit
        # if response.body == b"delete/limit.html":
        #     raise "Limitation is reached."
        match = re.search(re.compile(r"(webdownload\.asp\?uname=bitstyle11&did=.+\d+)", re.MULTILINE), response.body.decode('gbk','ignore') )
        # match = re.search(re.compile(b"(webdownload\.asp\?uname=bitstyle11&did=.+?)'\n", re.MULTILINE), response.body )
        if match:
            download_path = match.group(0)
            return scrapy.Request(self.host +"/"+ download_path, callback=self.store_file,
                # meta={'cookiejar': response.meta['cookiejar']})#, 'proxy': self.proxy})
                meta={'cookiejar': response.meta['cookiejar'], 'proxy': self.proxy})
        else:
            print(response.body)
            DownloadPaperSpider.error(self.get_url())
            self.logger.error('Error on page %s', self.get_url())
            self.index+=1
            return self.scrape_page()

        

    def store_file(self, response):
        try:
            file_name = (cgi.parse_header(response.headers['Content-Disposition'].decode('gbk','ignore'))[1]['filename'])
            with open("/Users/yuchao/Downloads/fintech/0/%s" % file_name, 'wb') as f:
                f.write(zlib.decompress(response.body, 16+zlib.MAX_WBITS))
        except:
            print(response.headers)
            print(response.body)
            DownloadPaperSpider.error(self.get_url())
        print("%s downloaded" % self.index)
        self.index += 1
        return self.scrape_page()

    def errback_httpbin(self, failure):
        request = failure.request
        DownloadPaperSpider.error(self.get_url())
        self.logger.error('Error on page %s', self.get_url())
        self.index+=1
        return scrapy.scrape_page()

    


        


