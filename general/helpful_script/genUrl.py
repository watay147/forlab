
def genUrl(l,outPath):
    f=open(outPath,'w')
    f.write("[\n")
    for i in l:
        f.write("\"http://guba.eastmoney.com/list,"+i+",f_1.html\",\n")
    f.write("]")

