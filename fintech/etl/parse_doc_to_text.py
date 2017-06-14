# encoding=utf-8

import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + "/..")
import db
import commands
# from db import *
import json

   

def parse(hibor_doc):
    prefix = "/data/money/fintech/hibor_doc"
    doc_path = ("%06d" % hibor_doc.id)
    path = ("/").join([doc_path[i:i+2] for i in range(0, len(doc_path), 2)])
    file_path = prefix + "/" + path + ".pdf"
    content = commands.getoutput("java -jar -Dfile.encoding=utf-8 /home/spark/tabula-0.9.2-jar-with-dependencies.jar -p all -g %s " % file_path)
    # content = commands.getoutput("echo I Love You")
    # content = "java -jar -Dfile.encoding=utf-8 /home/spark/tabula-0.9.2-jar-with-dependencies.jar -p all -g " % file_path
    return content

def new_doctext(hibor_doc, content):
    return db.Doctext(hibor_doc_id=hibor_doc.id, content=content)


hibor_docs = db.session.query(db.HiborDoc).filter_by(data_status = "downloaded", filetype= ".pdf").all()
for hibor_doc in hibor_docs:
    hibor_doc.data_status = "parsed"
    content = parse(hibor_doc)
    doctext = new_doctext(hibor_doc, content)
    db.session.add(hibor_doc)
    db.session.add(doctext)
    db.session.commit()

