# encoding=utf-8
import sqlalchemy
import re
import datetime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, DateTime, Text, text, BigInteger

class Doctext(Base):
    __tablename__ = "doctext"
    id = Column(Integer, primary_key=True)
    hibor_doc_id = Column(String(20))
    content = Column(Text())
    


    
    def __repr__(self):
        return "<Doctext(id='%s')>" % (self.id)


