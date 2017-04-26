#！ /usr/bin/python
import re
import zipfile as z
zf=z.ZipFile('channel.zip','r')#打开zip文件包channel.zip,   ZipFile是一个python类型，这里相当于构造了一个ZipFile对象
zipnames=zf.namelist()#ZipFile对象有方法，getinfo(),namelist(),open()
#print(zipnames)    #会看到这个zip压缩文件里面有很多xx.txt的文件
filename=zipnames[0]#第一个文件名
# print(i)       #i is the element of the zipnames list
#print(f.read())    #文件内容：Next nothing is xxxxx,提示我们要使用正则表达式查找数字，类似第四关
while(1):
    f = zf.open(filename)  # 从压缩包打开该文件
    content=f.read().decode()
    print(content)
    pattern=re.compile('[0-9]+')
    match=pattern.search(content)
    if match:
        num=match.group(0)
        filename=num+'.txt'
    else:
        break



