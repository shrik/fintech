# encoding=utf-8
import sqlalchemy
import re
import datetime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, DateTime, Text, text, BigInteger

# TODO 促销价格等需要更复杂的逻辑
# TODO 选择套餐类型等
class HiborDoc(Base):
    __tablename__ = "hibor_docs"
    id = Column(Integer, primary_key=True)
    # doc_type = Column(String(20))
    # grade = Column(String(20))
    upload_time = Column(DateTime)
    hibor_doc_id = Column(String(20))
    title = Column(String(255))
    favoritetypeid = Column(Integer)
    filetype = Column(String(10))
    author = Column(String(100))
    publish_agent = Column(String(40))
    typetitle = Column(String(30))
    filesize = Column(BigInteger)
    filepages = Column(Integer)
    file_url_encoded = Column(String(255))
    PublishPower = Column(Integer) # What's this
    industryname = Column(String(40))
    stockname = Column(String(60))
    stockcode = Column(String(20))
    rating = Column(String(20))
    summary = Column(Text(65536))
    file_url = Column(String(255))
    data_status = Column(String(20)) # list \ detail \ file_url \ downloaded



    #{"icotype": ".pdf", "grade": "\u589e\u6301", "time": "2017-02-20 09:30:45", "id": "2018478", 
    #"title": "\u4e2d\u6cf0\u8bc1\u5238-\u94a2\u94c1\u884c\u4e1a\u5468\u62a5\uff1a\u65fa\u5b63\u542f\u52a8\u94a2\u4ef7\u4e0a\u6da8-170217"}

#{"data":{"id":"1874339","favoritetypeid":"1",
#"title":"渤海证券-节能环保行业周报：“十三五”工业绿色发展规划出炉，重点行业VOCs削减行动计划发布-160719",
# "time":"2016-07-21 08:57:40",
#"filetype":".pdf","author":"任宪功","publish":"渤海证券","typetitle":"行业分析","filesize":"757009",
#"filepages":"14","fileurl":"EE2701B9E1B2C1406CCDBEEF3899411F4DAF17D8C2228F0549A377715BDD886374987950E17F9348DE0EEBABCAD2361B9477406206377AAF506663D2C864C20D9F915B536907826A",
#"PublishPower":"11","industryname":"节能环保行业","stockname":"","stockcode":"","rating":"中性","summary":"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;投资要点：<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;市场表现<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;近5&nbsp;&nbsp;个交易日内，沪深300&nbsp;&nbsp;下跌0.76%；环保设备指数、水务指数、环保工程及服务指数则分别小幅上涨0.57%、0.53%和0.22%，板块表现好于大盘。<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;细分子行业个股涨跌幅均值方面，渤海节能环保板块各子行业板块涨跌互现，其中大气治理上涨2.04%，涨幅居首；工业节能和环境监测则小幅收跌。个股方面，东江环保、博世科等涨幅居前，南方汇通、迪森股份等则跌幅居前；与上周相似，个股的涨跌幅度均不大。估值方面，渤海节能环保板块市盈率(TTM，剔除负值)为&nbsp;&nbsp;35.91&nbsp;&nbsp;倍，环比上周基本持平，相对沪深300&nbsp;&nbsp;的估值溢价率则较上周略有增加。<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;行业动态<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1、&nbsp;&nbsp;工信部印发工业绿色发展规划&nbsp;&nbsp;提十大主要任务<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2、&nbsp;&nbsp;两部委联合印发《重点行业挥发性有机物削减行动计划》<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3、&nbsp;&nbsp;七组中央环保督察组就位&nbsp;&nbsp;开启督察模式<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4、&nbsp;&nbsp;中国十大流域水质报告：劣五类占比超一成&nbsp;&nbsp;海河流域重度污染<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5、&nbsp;&nbsp;内蒙古力推第三方治理和服务<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;公司信息<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6、&nbsp;&nbsp;铁汉生态：签订5&nbsp;&nbsp;亿元承包合同<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7、&nbsp;&nbsp;先河环保：中标近9&nbsp;&nbsp;千万元采购项目合同<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8、&nbsp;&nbsp;格林美：孙公司拟增资扩股&nbsp;&nbsp;计划生产可配置10&nbsp;&nbsp;万辆新能源汽车电池组<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9、&nbsp;&nbsp;高能环境：中标7.5&nbsp;&nbsp;亿元垃圾处理PPP&nbsp;&nbsp;项目<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;投资策略<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;近5&nbsp;&nbsp;个交易日，大盘冲高回落，小幅走低；环保板块逆势收红，但上涨幅度有限，部分前期走势相对较强的子板块则开始出现调整，板块反弹总体表现较为乏力。在经历近期的震荡回升之后，环保板块的估值压力也在逐步增大，若后续大盘走弱，板块回调风险则将加大。我们维持谨慎操作的观点，并继续维持行业“中性”的投资评级。在个股选择上，建议重点关注有业绩支撑的低估值个股，以及基本面良好、业绩有望持续高增长的个股。近日印发的《工业绿色发展规划（2016-2020&nbsp;&nbsp;年）》提出，&nbsp;&nbsp;我国将加快构建绿色制造体系，大力发展绿色制造业，促进工业绿色发展整体水平提升。同时，“规划”明确了到2020&nbsp;&nbsp;年工业绿色发展的目标及主要指标要求。“十三五”期间，工业节能、资源综合利用等行业领域，有望在政策的持续加码扶持下，实现加速发展，建议关注相关细分领域龙头。未来3&nbsp;&nbsp;年国家将在重点行业实施挥发性有机物削减行动计划，工业行业VOCs&nbsp;&nbsp;排放量在2015&nbsp;&nbsp;年基础上削减330万吨以上。重点行业挥发性有机物治理的加快推进，利好VOCs&nbsp;&nbsp;监测及治理行业发展，建议重点关注拥有相关核心技术、具备监测及治理产业链一体化优势的公司。此外，PPP&nbsp;&nbsp;模式推进力度加大，建议关注PPP&nbsp;&nbsp;订单落地及相关先行布局企业投资机会。本周股票池推荐：兴源环境、博世科、聚光科技和清新环境。<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;风险提示<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1）&nbsp;&nbsp;政策落实不及预期；2）行业竞争加剧；3）大盘系统性风险。<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><br>　　（如果觉得此报告不错，请点击右上角分享到朋友圈，支持作者写出更好的文章！）","uploaduser":"mystudy521","shareurl":"http://www.hibor.com.cn/ios/sharecenter.asp?id=1874339&t=1"
#,"shareimg":"http://www.hibor.com.cn/ios/images/share/hibor_yb.jpg","sharetitle":"节能环保行业周报：“十三五”工业绿色发展规划出炉，重点行业VOCs削减行动计划发布","sharecontent":"节能环保行业周报：“十三五”工业绿色发展规划出炉，重点行业VOCs削减行动计划发布 http://www.hibor.com.cn/ios/sharecenter.asp?id=1874339&t=1","isshowsharedialog":"1","isshowcomment":"1"}}


    
    def __repr__(self):
        return "<User(name='%s', id='%s')>" % (self.title, self.id)


