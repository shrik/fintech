# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + "/..")
import db

import scrapy
import zlib
import re
import cgi

class DownloadFile(scrapy.Spider):
    name = "DownloadFile"
    allowed_domains = ["hibor.com.cn"]
    hibor_doc = None

    # proxy = "http://115.29.38.207:16816"
    def start_requests(self):
        return [scrapy.Request("http://www.hibor.com.cn", callback=self.parse)]

    def parse(self, response):
        # self.hibor_doc = db.session.query(db.HiborDoc).filter_by(data_status="file_url").first()
        yield self.save_doc(None)
        
    def save_doc(self, response):
        if response is None:
            self.hibor_doc = db.session.query(db.HiborDoc).filter_by(data_status="file_url").first()
            return scrapy.Request(self.hibor_doc.file_url, callback=self.save_doc)
        try:
            # directory = "/data/money/fintech/hibor_doc"
            suffix = self.hibor_doc.filetype
            directory = "/Users/yuchaoma/Downloads"
            id_path = ("%06d" % self.hibor_doc.id)
            path = ("/").join([id_path[i:i+2] for i in range(0, len(id_path), 2)])
            file_dir = directory + "/" + path[0:5]
            if not os.path.exists(file_dir):
                os.makedirs(file_dir)
            with open( "%s/%s%s" % (directory, path, suffix) , 'wb') as f:
                # f.write(zlib.decompress(response.body, 16+zlib.MAX_WBITS))
                f.write(response.body)
            self.hibor_doc.data_status = "downloaded"
            db.session.commit()
        except:
            print("Error ID is %s" % self.hibor_doc.id)
            self.hibor_doc.data_status = "error dl"
            self.session.commit()
        #     self.log_error(self.hibor_doc, response)

        self.hibor_doc = db.session.query(db.HiborDoc).filter_by(data_status="file_url").first()
        return scrapy.Request(self.hibor_doc.file_url, callback=self.save_doc)


    def log_error(self, hibor_doc, response):
        print(response.headers)
        print(response.body)