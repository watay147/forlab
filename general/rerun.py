import os
import re
import MySQLdb
import datetime
from datetime import timedelta
import sys

nowDate=datetime.datetime.now().isoformat()[:10]

tarwebsites=eval(open('startlist.txt').read())
for index,i in enumerate(tarwebsites):
    f=open('start.txt','w')
    f.write(i)
    f.close()
    os.system("scrapy crawl general")

with open("conf/spiderConf.txt") as f:
    conf=eval(f.read())
    spider_tag=conf.get("spider_tag","GG_guba_1")
DB_NAME="stock_web_system"
con=MySQLdb.Connect( user='root',  db=DB_NAME,charset='utf8',host='222.29.97.233', port = 3306)
cur = con.cursor()
cur.execute("UPDATE spider_record SET "+spider_tag+"= 1 WHERE date = '%s'" % nowDate)
con.commit()
cur.close()
con.close()
sys.exit()

print "run finish"