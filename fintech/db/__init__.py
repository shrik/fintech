import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost/fintech?charset=utf8', echo=True)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

from hibor_doc import HiborDoc
from doctext import Doctext
