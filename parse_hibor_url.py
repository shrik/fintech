
import json
import commands

start_index = 0

decrypt_program = "java -cp /Users/yuchaoma/Documents/eclipse_workspace/src/ HelloWorld"

with open("/Users/yuchaoma/Desktop/hibor/items_detail.txt.bak2", "r") as f:
    detail = f.read()
items = []
for d_item in detail.split("\n"):
    if d_item != "":
        items.append(json.loads(d_item))
index = start_index
while True:
    new_item = []
    item = items[index]['data']
    code = item['fileurl']
    ts = item['time']
    size = item.get('filesize','W')
    pages = item.get('filepages', 'M')
    cmd = "%s %s %s %s %s" % (decrypt_program, code, "'%s'" % ts, "'%s'" % size,   "'%s'" % pages)
    url =  commands.getstatusoutput(cmd)[1].strip()
    print(url)
    new_item.append(url)
    new_item.append(item['publish'].encode('utf-8'))
    new_item.append(item['author'].encode('utf-8'))
    new_item.append(item['title'].encode('utf-8'))
    with open("/Users/yuchaoma/Desktop/hibor/item_with_url.txt", "a") as f:
        f.write(",".join(new_item) + "\n")
    index += 1