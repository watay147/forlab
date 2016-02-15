import MySQLdb
import re
conn = MySQLdb.Connect( user='root',  db='guba',charset='utf8')
cursor=conn.cursor()

with open("1-28lib.txt") as f:
	l=eval(f.read())
f=open('crawledDate.log','w')
for index,i in enumerate(l):
    print index
    num=re.search(r',\d+',i).group(0)[1:]
    
    cursor.execute("CREATE INDEX TimeIndex on `article%s`(time);" % (num,))
    cursor.execute("CREATE INDEX TimeIndex on `reply%s`(commentDate);" % (num,))
    conn.commit()
    cursor.execute("select max(time) from `article%s`" % (num,))
    results=cursor.fetchall()
    f.write("\""+num+"\":\""+str(results[0][0])+"\",\n")
    f.flush()
cursor.close()
conn.close()
f.close()

