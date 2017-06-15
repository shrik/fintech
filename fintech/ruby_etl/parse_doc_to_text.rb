# encoding=utf-8

require "./db.rb"

   

def parse(hibor_doc)
    prefix = "/data/money/fintech/hibor_doc"
    doc_path = ("%06d" % hibor_doc.id)
    path = []
    (0..5).step(2).each do |s|
        path << doc_path[s..(s+2)] 
    end
    path = path.join("/")
    file_path = prefix + "/" + path + ".pdf"
    content = %x|java -jar -Dfile.encoding=utf-8 /home/spark/tabula-0.9.2-jar-with-dependencies.jar -p all -g #{file_path}|
    # content = commands.getoutput("echo I Love You")
    # content = "java -jar -Dfile.encoding=utf-8 /home/spark/tabula-0.9.2-jar-with-dependencies.jar -p all -g " % file_path
    return content
end

def new_doctext(hibor_doc, content)
    Doctext.new(hibor_doc_id: hibor_doc.id, content: content)
end


hibor_docs =  HiborDoc.where(data_status: "downloaded", filetype: ".pdf").all
hibor_docs.each do |hibor_doc|
    hibor_doc.data_status = "parsed"
    content = parse(hibor_doc)
    doctext = new_doctext(hibor_doc, content)
    hibor_doc.save!
    doctext.save!
end

