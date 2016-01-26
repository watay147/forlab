import MySQLdb
import pandas as pd
import re
conn = MySQLdb.Connect( user='root',  db='guba',charset='utf8')
cursor=conn.cursor()
l=[
]
countNum=0
f=open('dbCount.log','w')
nonf=open('nonDb.log','w')
for index,i in enumerate(l):
    print index
    stockno=re.search(r',\d+',i).group(0)[1:]
    cursor.execute("select count(*) from `article%s`" % (stockno,))
    results=cursor.fetchall()
    if results[0][0]==0:
        nonf.write(stockno+',\n')
        nonf.flush()
    countNum+=results[0][0]
    f.write("count:"+str(countNum)+'\n')
    f.flush()
    print "count:"+str(countNum)
cursor.close()
conn.close()
f.close()
nonf.close()
