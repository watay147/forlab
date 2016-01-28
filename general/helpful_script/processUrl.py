import re
def e(p):
    return eval(open(p).read())

def getnum(l):
    return map(lambda x:re.search(r'\d+',x).group(0),l)

def getStockno(l):
    return map(lambda x:"%06d" % x,l)