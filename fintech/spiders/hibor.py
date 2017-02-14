# -*- coding: utf-8 -*-
import scrapy
import zlib

class HiborSpider(scrapy.Spider):
    name = "hibor"
    allowed_domains = ["hibor.com.cn"]
    start_urls = ['http://www.hibor.com.cn/microns_2.html']

    # customized
    host = "http://www.hibor.com.cn"
    dologin_path = "/toplogin.asp?action=login"
    acc = "bitstyle11"
    pwd = "springs"
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
    
# download URL: http://www.hibor.com.cn/webdownload.asp?uname=bitstyle11&did=2014647&degree=1&baogaotype=15&fromtype=21


    def parse(self, response):
        # yield self.login()
        for i in range(1,362):
            yield self.extract_listpage(i)
            print("page %s" % i)

    def extract_listpage(self, page_num):
        url = "http://www.hibor.com.cn/microns_2%s.html"
        if page_num < 2:
            url = url % ''
        else:
            url = url % ("_%s" % page_num)
        return scrapy.Request(url, callback=self.process_listpage)

    def process_listpage(self, response):
        data = ""
        for link in response.css("#tableList .tab_lta a"):
            href = link.xpath('.//@href').extract()[0]
            text = link.xpath('.//text()').extract()[0]
            data = data + href + "," + text + "\n"

        with open("./hibor.csv", 'a') as f:
            f.write(data)


    # def login(self):
    #     dologin_url = self.host + self.dologin_path
    #     return scrapy.FormRequest(dologin_url, 
    #                              callback=self.parse_login_result,
    #                              formdata={'name': self.acc, 'pwd': self.pwd, 'checkbox': 'on'},
    #                              meta={'cookiejar': 1})

    # def parse(self, response):
    #     dologin_url = self.host + self.dologin_path
    #     content_type = "application/x-www-form-urlencoded"
    #     yield scrapy.FormRequest(dologin_url, 
    #                              callback=self.parse_login_result,
    #                              formdata={'name': self.acc, 'pwd': self.pwd, 'checkbox': 'on'},
    #                              meta={'cookiejar': 1})

    # def parse_login_result(self, response):
    #     download_url = "http://www.hibor.com.cn/webdownload.asp?uname=bitstyle11&did=2014647&degree=1&baogaotype=15&fromtype=21"
    #     return scrapy.Request(download_url, meta={'cookiejar': response.meta['cookiejar']},
    #         callback=self.store_file)
        
    # def store_file(self, response):
    #     with open("/Users/yuchao/Downloads/xx.pdf", 'wb') as f:
    #         f.write(zlib.decompress(response.body, 16+zlib.MAX_WBITS))
    #         # f.write(response.body)
    #     print("file saved")


