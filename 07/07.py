#! /usr/bin/python
from urllib import request
from PIL import Image
import re
url="http://www.pythonchallenge.com/pc/def/oxygen.png"
f=open("oxygen.png","wb")#注意要写入二进制流
f.write(request.urlopen(url).read())
f.close()

im=Image.open("oxygen.png")
data=im.convert("L").getdata()
print(list(data))
message = []
for i in range(3,608,7):
    message.append(chr(data[im.size[0]*50+i]))
result= ''.join(message)
print(type(result))
print(result)
pattern=re.compile("\[([\d\D]+)\]")
match=pattern.search(result)
result=match.group(1).split(',')
#print(type(result))

for i in result:
    print(chr(int(i)))


