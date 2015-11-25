import os
import re
tarwebsites=eval(open('startlist.txt').read())
for index,i in enumerate(tarwebsites):
    f=open('start.txt','w')
    f.write(i)
    f.close()
    os.system("scrapy crawl general")



print "run finish"