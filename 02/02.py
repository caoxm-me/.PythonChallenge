#！/usr/bin/python
#首先，按提示爬了网页数据再说
from urllib import request
import re
import string
#import numpy as np
response=request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
content=response.read().decode()
print(content)
#print(content)     #内容中有大篇幅注释，提示信息在内
pattern=re.compile("<!--\n%[\d\D]+")#match the comment(begin with <!--
text=pattern.search(content)
print(text.group(0))
#print(text.group(0))   #返回匹配对象text中记录的完全匹配的字符串，除此之外该对象中还有很多关于匹配结果的信息
#上面已经看出来，text.group(0)内容就是页面源码下面很长的一串注释，接下来要从中寻找rare character
dic={}
for x in text.group(0):
    if x not in dic:
        dic[x] = 1
    else:
        dic[x] += 1
print(dic)
#print([x for x in dic.keys()if dic[x]<np.mean(list((dic.values())))])#rare characters 怎么理解
#print(string.ascii_lowercase)
print(list(string.ascii_lowercase))
print([x for x in dic if (dic[x]==1 and x in list(string.ascii_lowercase))])







