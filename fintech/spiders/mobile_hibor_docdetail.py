# -*- coding: utf-8 -*-
import scrapy
import zlib
import urllib
import json



class MobileHiborDocdetailSpider(scrapy.Spider):
    
    name = "MobileHiborDocdetail"
    allowed_domains = ["hibor.com.cn"]

    # customized
    # host = "http://newsmag.hibor.com.cn"
    user_agent = "Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM919 Build/MXB48T)"

    
    url_format = "http://newsmag.hibor.com.cn/MobilePhone/DocDetailHandler.ashx?systype=android&btype=1&username=6W1UvWuYsTzVnWfUrQpO&id=%s"

    start_index = 986
    items_to_crawl = []

    @classmethod
    def items(cls):
        if cls.items_to_crawl != []:
            return cls.items_to_crawl
        with open("/Users/yuchaoma/Desktop/hibor/items_for_scrawl.txt", "r") as f:
            items_txt = f.read()
        for item_txt in items_txt.split("\n"):
            if item_txt != "":
                cls.items_to_crawl.append(json.loads(item_txt))
        return cls.items_to_crawl


    def start_requests(self):
        item = MobileHiborDocdetailSpider.items()[MobileHiborDocdetailSpider.start_index]
        url = self.url_format %  item['id']
        return [scrapy.Request(url,callback=self.parse)]

    def parse(self, response):
        format_detail = self.format_detail(response.body)
        self.store(format_detail)
        print("scraped %s" % MobileHiborDocdetailSpider.start_index)
        MobileHiborDocdetailSpider.start_index += 1
        yield self.next_item(MobileHiborDocdetailSpider.start_index)

    def next_item(self, index):
        item = MobileHiborDocdetailSpider.items()[MobileHiborDocdetailSpider.start_index]
        url = self.url_format %  item['id']
        return scrapy.Request(url, callback=self.parse)

    def format_detail(self, body):
        return body

    def store(self, item):
        file_path = "/Users/yuchaoma/Desktop/hibor/items_detail.txt"
        with open(file_path, "a") as f:
            f.write(item+"\n")
