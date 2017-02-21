# -*- coding: utf-8 -*-
import scrapy
import zlib
import urllib
import json



class MobileHiborSpider(scrapy.Spider):
    # start_time = "2017-02-20 10:00:00"
    start_time = "2016-11-22 13:51:17"
    name = "MobileHibor"
    allowed_domains = ["hibor.com.cn"]

    # customized
    # host = "http://newsmag.hibor.com.cn"
    user_agent = "Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM919 Build/MXB48T)"

    # url_format = "http://newsmag.hibor.com.cn/GetJsonHandler.ashx?systype=android&btype=1&count=20&time=%s&uord=up&username=6WjXlV6WlTkWnTnV&stype=2"
    url_format = "http://newsmag.hibor.com.cn/MobilePhone/GetJsonHandler.ashx?systype=android&btype=1&count=20&time=%s&uord=up&username=6WjXlV6WlTkWnTnV&stype=2"


# http://newsmag.hibor.com.cn/MobilePhone/GetJsonHandler.ashx?systype=android&btype=1&count=20&time=2017-02-20+14%3A20%3A32&uord=up&username=6WjXlV6WlTkWnTnV&stype=2
# http://newsmag.hibor.com.cn/GetJsonHandler.ashx?systype=android&btype=1&count=20&time=2017-02-20+10%3A00%3A00&uord=up&username=6WjXlV6WlTkWnTnV&stype=2
    def start_requests(self):
        url = self.url_format %  urllib.quote_plus(self.start_time)
        return [scrapy.Request(url,callback=self.parse)]

    def parse(self, response):
        items = self.json_to_items(response.body)
        oldest_ts = self.get_oldest_ts(items)
        self.store(items)
        print("scraped %s" % oldest_ts)
        yield self.next_page(oldest_ts)

    def next_page(self, ts):
        url = self.url_format % urllib.quote_plus(ts)
        return scrapy.Request(url, callback=self.parse)

 #data = '{"status":0,"data":{"list":[{"id":"2018896","title":"开源证券-煤炭行业周报：电厂煤耗回升明显，国外焦煤价格跌幅加深-170220","time":"2017-02-20 14:20:29","icotype":".pdf","grade":"中性"},{"id":"2018895","title":"海通证券-新能源行业周报：持续聚焦钴价上涨受益品种-170220","time":"2017-02-20 14:19:28","icotype":".pdf","grade":"增持"},{"id":"2018887","title":"招商证券-军工行业事件点评：融资新规对军工板块的影响点评-170219","time":"2017-02-20 14:15:53","icotype":".pdf","grade":"推荐"},{"id":"2018886","title":"申万宏源-商业贸易行业周报：润泰回应确认电商巨头洽购大润发，实体零售迎双重利好-170220","time":"2017-02-20 14:15:29","icotype":".pdf","grade":"中性"},{"id":"2018883","title":"申万宏源-环保公用行业含新三板周报：能源局17年重在结构性改革，京津冀生态治理再度加码-170220","time":"2017-02-20 14:14:45","icotype":".pdf","grade":"看好"},{"id":"2018881","title":"申万宏源-传媒互联网行业周报：乐观看待教育资产证券化前景-170220","time":"2017-02-20 14:13:07","icotype":".pdf","grade":"中性"},{"id":"2018878","title":"招商证券-家电行业周观点17w07：估值的彼岸-170219","time":"2017-02-20 14:11:48","icotype":".pdf","grade":"推荐"},{"id":"2018876","title":"申万宏源-钢铁行业：广东省淘汰中频炉产能（第一批）点评，2017年淘汰中频炉已进入从严执行阶段，利好相应长材企业-170220","time":"2017-02-20 14:11:26","icotype":".pdf","grade":"看好"},{"id":"2018872","title":"渤海证券-计算机行业周报：再融资新规出台，行业将迎短期冲击-170220","time":"2017-02-20 14:09:47","icotype":".pdf","grade":"看好"},{"id":"2018871","title":"申万宏源-电力设备新能源周报：2017年能源工作指导意见发布，风电格局趋势向好-170220","time":"2017-02-20 14:09:25","icotype":".pdf","grade":"看好"},{"id":"2018867","title":"申万宏源-家电行业周报：1月空调内销继续高速反弹，养老金入市利好家电蓝筹-170220","time":"2017-02-20 14:08:31","icotype":".pdf","grade":"看好"},{"id":"2018866","title":"招商证券-计算机行业周报：融资新规，谷歌发布TensorFlow 1.0-170219","time":"2017-02-20 14:08:20","icotype":".pdf","grade":"推荐"},{"id":"2018865","title":"光大证券-有色金属行业周报：关注供需基本面，精选品种为主-170219","time":"2017-02-20 14:07:55","icotype":".pdf","grade":"买入"},{"id":"2018864","title":"中金公司-农业：农产品价格周报-170220","time":"2017-02-20 14:07:37","icotype":".pdf","grade":""},{"id":"2018858","title":"申万宏源-纺织服装行业周报：定增新规对纺服已有项目影响不大，未来更加回归基本面-170220","time":"2017-02-20 14:05:17","icotype":".pdf","grade":"看好"},{"id":"2018856","title":"申万宏源-交运一周天地汇：定增新规出台，物流快递板块未来融资部分受限-170220","time":"2017-02-20 14:04:31","icotype":".pdf","grade":"中性"},{"id":"2018852","title":"海通证券-文化传媒行业新三板传媒/互联网旅游一周观察：新三板市场规模趋稳，回归价值投资有助发展-170219","time":"2017-02-20 14:03:28","icotype":".pdf","grade":"增持"},{"id":"2018850","title":"招商证券-环保电力行业周报第69期：变相加息或利好PPP，继续推荐行业龙头东方园林-170219","time":"2017-02-20 14:03:26","icotype":".pdf","grade":"推荐"},{"id":"2018849","title":"申万宏源-定增新规对纺织服装行业的影响点评：存量影响小，对未来再融资规模和节奏起到约束-170220","time":"2017-02-20 14:03:20","icotype":".pdf","grade":"看好"},{"id":"2018846","title":"申万宏源-通信行业周报：除了700M和100G，还看217定增细则影响有多大？-170220","time":"2017-02-20 14:02:37","icotype":".pdf","grade":"看好"}]}}'

    def json_to_items(self, json_str):
        return json.loads(json_str)['data']['list']

    def get_oldest_ts(self,items):
        times = [item['time'] for item in items]
        times.sort()
        return times[0]

    def store(self, items):
        file_path = "/Users/yuchaoma/Desktop/hibor/items.txt"
        with open(file_path, "a") as f:
            for item in items:
                f.write(json.dumps(item)+"\n")



    # def parse_next_page(self, response):
    #     items = self.json_to_items(response.body)
    #     oldest_ts = self.get_oldest_ts(items)
    #     self.store(items)

    #     yield self.next_page(oldest_ts)

