# -*- coding: utf-8 -*-
import scrapy


import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
         'https//www.baidu.com/',
    ]

    host = "http://www.hibor.com.cn"
    dologin_path = "/toplogin.asp?action=login"
    acc = "bitstyle11"
    pwd = "springs"

    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
    

    def dologin(self):
        print 3
        post_text =( "name=%s&pwd=%s&tijiao.x=24&tijiao.y=14&tijiao=%%B5%%C7%%C2%%BC&checkbox=on" % (self.acc, self.pwd))
        dologin_url = self.host + self.dologin_path
        content_type = "application/x-www-form-urlencoded"
        scrapy.Request(dologin_url, method='POST', body=post_text, callback=self.parse_login_result)


    def parse_login_result(self, response):
        print 2
        print response.body
        print response.headers


    def parse(self, response):
        self.dologin()
        # for quote in response.css('div.quote'):
        #     yield {
        #         'text': quote.css('span.text::text').extract_first(),
        #         'author': quote.xpath('span/small/text()').extract_first(),
        #     }

        # next_page = response.css('li.next a::attr("href")').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)

# QuotesSpider().dologin()


class HiborSpider(scrapy.Spider):
    name = "hibor"
    allowed_domains = ["hibor.com.cn"]
    start_urls = ['http://hibor.com.cn/']

    def parse(self, response):
        pass
