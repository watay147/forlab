# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import MySQLdb
import time
import re
def sendmail(msgcontent,to_addr="449339387@qq.com"):
    smtp_server="smtp.126.com"
    from_addr="finbigdata@126.com"
    password="iemxlrfnypsmozuu"
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = Header(u'爬虫异常提醒', 'utf-8').encode()
    txt = MIMEText(msgcontent, 'plain', 'utf-8')
    msg.attach(txt)
    server = smtplib.SMTP() # SMTP协议默认端口是25
    server.connect(smtp_server)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.close()
class DBPipeline(object):

    def open_spider(self, spider):
        self.storeFunc={'XMulItem':self.storeXMulItem,
			'XSinItem':self.storeXSinItem,
			'YMulItem':self.storeYMulItem,
			'YSinItem':self.storeYSinItem,
			'ZMulItem':self.storeZMulItem,
			'ZSinItem':self.storeZSinItem,
			}
        self.conn = MySQLdb.Connect( user='root',  db='guba',charset='utf8')
        self.cursor=self.conn.cursor() 
        self.crawldate=time.strftime("%Y-%m-%d",time.localtime())
        self.stockno=re.search(r',\d+',spider.start_urls[0]).group(0)[1:]

    def process_item(self, item, spider):
        
        if len(item)!=0:
            self.storeFunc[item.__class__.__name__](item)
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
        spider.browser.close()
        spider.f.close()
        print "finish!"

    def storeXMulItem(self,item):
        itemlist=zip(item['Xtitle'],item['Xarticleid'],item['Xstockno'],item['Xreply'],item['Xclick'])
        for instance in itemlist:
            instance=instance+(self.crawldate,)
            try:
                self.cursor.execute("insert ignore into `gubarticleupdate%s` (title,articleid,stockno,reply,click,crawldate) value ('%s',%s,'%s',%s,%s,'%s')"% ((self.stockno,)+instance))
            except Exception,e:
                sendmail(u'数据库错误:'+unicode(e)+unicode(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())))
                while True:
                    try:
                        self.conn = MySQLdb.Connect( user='root',  db='guba',charset='utf8')
                        break
                    except Exception,e:
                        time.sleep(2)
                        continue
                self.cursor=self.conn.cursor()
                self.cursor.execute("insert ignore into `gubarticleupdate%s` (title,articleid,stockno,reply,click,crawldate) value ('%s',%s,'%s',%s,%s,'%s')"% ((self.stockno,)+instance))

        self.conn.commit()
            
        
        




    def storeXSinItem(self,item):
        pass
        

    def storeYMulItem(self,item):
        itemlist=zip(item['YcommentAuthor'],item['YcommentDate'],item['YcommentContent'],item['YcommentAuthorid'],item['Yarticleid'])
        for instance in itemlist:
            try:
                self.cursor.execute("insert ignore into `reply%s` (commentAuthor,commentDate,commentContent,commentAuthorid,articleid) value ('%s','%s','%s',%s,%s)"% ((self.stockno,)+instance))
            except Exception,e:
                sendmail(u'数据库错误:'+unicode(e)+unicode(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())))
                while True:
                    try:
                        self.conn = MySQLdb.Connect( user='root',  db='guba',charset='utf8')
                        break
                    except Exception,e:
                        time.sleep(2)
                        continue
                self.cursor=self.conn.cursor()
                self.cursor.execute("insert ignore into `reply%s` (commentAuthor,commentDate,commentContent,commentAuthorid,articleid) value ('%s','%s','%s',%s,%s)"% ((self.stockno,)+instance))
        self.conn.commit()
      

    def storeYSinItem(self,item):
        instance=(item['Ytitle'],item['Yauthor'],item['Ystockno'],item['Ydate'],item['Ycontent'],item['Yarticleid'])
        try:
            self.cursor.execute("insert ignore into `article%s` (title,author,stockno,time,content,articleid) value ('%s','%s','%s','%s','%s',%s)"% ((self.stockno,)+instance))#insert ignore会自动避免重复插入
        except Exception,e:
            sendmail(u'数据库错误:'+unicode(e)+unicode(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())))
            while True:
                try:
                    self.conn = MySQLdb.Connect( user='root',  db='guba',charset='utf8')
                    break
                except Exception,e:
                    time.sleep(2)
                    continue
            self.cursor=self.conn.cursor()
            self.cursor.execute("insert ignore into `article%s` (title,author,stockno,time,content,articleid) value ('%s','%s','%s','%s','%s',%s)"% ((self.stockno,)+instance))
        self.conn.commit()
        

    def storeZMulItem(self,item):
        itemlist=zip(item['ZcommentAuthor'],item['ZcommentDate'],item['ZcommentContent'],item['ZcommentAuthorid'],item['Zarticleid'])
        for instance in itemlist:
            try:
                self.cursor.execute("insert ignore into `reply%s` (commentAuthor,commentDate,commentContent,commentAuthorid,articleid) value ('%s','%s','%s',%s,%s)"% (self.stockno,)+instance)
            except Exception,e:
                sendmail(u'数据库错误:'+unicode(e)+unicode(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())))
                while True:
                    try:
                        self.conn = MySQLdb.Connect( user='root',  db='guba',charset='utf8')
                        break
                    except Exception,e:
                        time.sleep(2)
                        continue
                self.cursor=self.conn.cursor()
                self.cursor.execute("insert ignore into `reply%s` (commentAuthor,commentDate,commentContent,commentAuthorid,articleid) value ('%s','%s','%s',%s,%s)"% (self.stockno,)+instance)
        
        self.conn.commit()
    

    def storeZSinItem(self,item):
        pass



