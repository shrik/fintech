
import json
import commands
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + "/..")
import db

start_index = 0

decrypt_program = "java -cp /Users/yuchaoma/Documents/eclipse_workspace/src/ HelloWorld"

while True:
    hibor_docs = db.session.query(db.HiborDoc).filter_by(data_status='detail').limit(100)
    if hibor_docs.count() > 0:
        for hibor_doc in hibor_docs:
            code = hibor_doc.file_url_encoded
            ts = hibor_doc.upload_time
            size = hibor_doc.filesize or 'W'
            pages = hibor_doc.filepages or 'M'
            cmd = "%s %s %s %s %s" % (decrypt_program, code, "'%s'" % ts, "'%s'" % size,   "'%s'" % pages)
            url =  commands.getstatusoutput(cmd)[1].strip()
            print(url)
            hibor_doc.file_url = url
            hibor_doc.data_status = 'file_url'
        db.session.commit()
    else:
        raise

    
    
