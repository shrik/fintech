# encoding=utf-8
import sqlalchemy
import re
import datetime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, DateTime, Text, text, BigInteger

# TODO 促销价格等需要更复杂的逻辑
# TODO 选择套餐类型等

#证券公司、日期、行业、股票名称、买入、分析师、股票代码
#Advice 分为 买入、增持、持有、卖出 四个级别
class Procast(Base):
    __tablename__ = "procasts"
    id = Column(Integer, primary_key=True)
    hibor_doc_id = Column(String(20))
    stockname = Column(String(40))
    stockcode = Column(String(50))
    advise = Column(String(20))
    origin = Column(String(1000))
    


    
    def __repr__(self):
        return "<Procast(stockname='%s', advice='%s', id='%s')>" % (self.stockname, self.advice, self.id)


