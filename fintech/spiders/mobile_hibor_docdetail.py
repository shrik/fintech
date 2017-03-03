# -*- coding: utf-8 -*-
import scrapy
import zlib
import urllib
import json


# https://rate.tmall.com/list_detail_rate.htm?itemId=44144124999&spuId=324629781&sellerId=876270265&order=3&currentPage=30&append=0&content=1
class MobileHiborDocdetailSpider(scrapy.Spider):
    
    name = "MobileHiborDocdetail"
    allowed_domains = ["hibor.com.cn"]

    # customized
    # host = "http://newsmag.hibor.com.cn"
    user_agent = "Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM919 Build/MXB48T)"

    # username sXrUdUiX 6W1UvWuYsTzVnWfUrQpO dTjXkWeU2XjXnTnV
    # acc & pwd & encode_uid:  hbmyca & myc123456 & kX5V2XxTeTeV
    # jy01264313 zx19880427  mXwUrRpOsQqOnRsRnMtQ
    uids = ['sXrUdUiX', '6W1UvWuYsTzVnWfUrQpO' , 'dTjXkWeU2XjXnTnV' , 'kX5V2XxTeTeV', 'mXwUrRpOsQqOnRsRnMtQ']

    url_format = "http://newsmag.hibor.com.cn/MobilePhone/DocDetailHandler.ashx?systype=android&btype=1&username=%s&id=%s"

    start_index = 18990 + 5000
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


    @classmethod
    def getUid(cls):
        uids = MobileHiborDocdetailSpider.uids
        index = MobileHiborDocdetailSpider.start_index%5
        return uids[index]

    def start_requests(self):
        item = MobileHiborDocdetailSpider.items()[MobileHiborDocdetailSpider.start_index]
        url = self.url_format % ( MobileHiborDocdetailSpider.getUid(), item['id'])
        return [scrapy.Request(url,callback=self.parse)]

    def parse(self, response):
        if MobileHiborDocdetailSpider.start_index > 18990 + 7500:
            return
        format_detail = self.format_detail(response.body)
        self.store(format_detail)
        print("scraped %s" % MobileHiborDocdetailSpider.start_index)
        MobileHiborDocdetailSpider.start_index += 1
        yield self.next_item(MobileHiborDocdetailSpider.start_index)

    def next_item(self, index):
        item = MobileHiborDocdetailSpider.items()[MobileHiborDocdetailSpider.start_index]
        url = self.url_format %  ( MobileHiborDocdetailSpider.getUid(), item['id'])
        return scrapy.Request(url, callback=self.parse)

    def format_detail(self, body):
        return body

    def store(self, item):
        file_path = "/Users/yuchaoma/Desktop/hibor/items_detail.txt"
        with open(file_path, "a") as f:
            f.write(item+"\n")
