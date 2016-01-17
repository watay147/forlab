import MySQLdb
import pandas as pd
import re
conn = MySQLdb.Connect( user='root',  db='guba',charset='utf8')
cursor=conn.cursor()
l=[
"http://guba.eastmoney.com/list,300292,f_1.html",
"http://guba.eastmoney.com/list,300293,f_1.html",
"http://guba.eastmoney.com/list,300294,f_1.html",
"http://guba.eastmoney.com/list,300295,f_1.html",
"http://guba.eastmoney.com/list,300296,f_1.html",
"http://guba.eastmoney.com/list,300297,f_1.html",
"http://guba.eastmoney.com/list,300298,f_1.html",
"http://guba.eastmoney.com/list,300299,f_1.html",
"http://guba.eastmoney.com/list,300300,f_1.html",
"http://guba.eastmoney.com/list,300302,f_1.html",
"http://guba.eastmoney.com/list,300303,f_1.html",
"http://guba.eastmoney.com/list,300304,f_1.html",
"http://guba.eastmoney.com/list,300305,f_1.html",
"http://guba.eastmoney.com/list,300306,f_1.html",
"http://guba.eastmoney.com/list,300307,f_1.html",
"http://guba.eastmoney.com/list,300308,f_1.html",
"http://guba.eastmoney.com/list,300309,f_1.html",
"http://guba.eastmoney.com/list,300310,f_1.html",
"http://guba.eastmoney.com/list,300311,f_1.html",
"http://guba.eastmoney.com/list,300312,f_1.html",
"http://guba.eastmoney.com/list,300313,f_1.html",
"http://guba.eastmoney.com/list,300314,f_1.html",
"http://guba.eastmoney.com/list,300315,f_1.html",
"http://guba.eastmoney.com/list,300316,f_1.html",
"http://guba.eastmoney.com/list,300317,f_1.html",
"http://guba.eastmoney.com/list,300318,f_1.html",
"http://guba.eastmoney.com/list,300319,f_1.html",
"http://guba.eastmoney.com/list,300320,f_1.html",
"http://guba.eastmoney.com/list,300321,f_1.html",
"http://guba.eastmoney.com/list,300322,f_1.html",
"http://guba.eastmoney.com/list,300323,f_1.html",
"http://guba.eastmoney.com/list,300324,f_1.html",
"http://guba.eastmoney.com/list,300325,f_1.html",
"http://guba.eastmoney.com/list,300326,f_1.html",
"http://guba.eastmoney.com/list,300327,f_1.html",
"http://guba.eastmoney.com/list,300328,f_1.html",
"http://guba.eastmoney.com/list,300329,f_1.html",
"http://guba.eastmoney.com/list,300330,f_1.html",
"http://guba.eastmoney.com/list,300331,f_1.html",
"http://guba.eastmoney.com/list,300332,f_1.html",
"http://guba.eastmoney.com/list,300333,f_1.html",
"http://guba.eastmoney.com/list,300334,f_1.html",
"http://guba.eastmoney.com/list,300335,f_1.html",
"http://guba.eastmoney.com/list,300336,f_1.html",
"http://guba.eastmoney.com/list,300337,f_1.html",
"http://guba.eastmoney.com/list,300338,f_1.html",
"http://guba.eastmoney.com/list,300339,f_1.html",
"http://guba.eastmoney.com/list,300340,f_1.html",
"http://guba.eastmoney.com/list,300341,f_1.html",
"http://guba.eastmoney.com/list,300342,f_1.html",]
countNum=0
for index,i in enumerate(l):
    print index
    num=re.search(r',\d+',i).group(0)[1:]
    cursor.execute("select count(*) from `article%s`" % (num,))
    results=cursor.fetchall()
    countNum+=results[0][0]
    print "count:"+str(countNum)
cursor.close()
conn.close()
