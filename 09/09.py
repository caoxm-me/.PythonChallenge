#! /usr/bin/python
import re
from PIL import Image
file = open('good.html')
message = re.findall('(<!--[^-]+-->)', file.read(), re.S)[1]  
file.close()
first = re.findall('(\d+)',re.findall('first:(.+)second',message,re.S)[0],re.S)
second = re.findall('(\d+)',re.findall('second:(.+)>',message,re.S)[0],re.S)
print(first,"\n",second)
all = first + second  #连接了两个list
print(all)
im = Image.open('good.jpg')
im2 = Image.new(im.mode, im.size)
for x in range(0,len(all),2):  
    im2.putpixel((int(all[x]),int(all[x+1])),(255,255,255,255))  
im2.show()