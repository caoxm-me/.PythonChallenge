#！ /usr/bin/python
#从061.py运行结果我们注意到要"collect the comment",即搜集文件在zip的时候加入的注释信息
import re
import zipfile as z
zf=z.ZipFile('channel.zip','r')#打开zip文件包channel.zip,   ZipFile是一个python类型，这里相当于构造了一个ZipFile对象
filename='90052.txt'#从readme.txt中获知
comment_list=[]
while(1):
    f = zf.open(filename)  # 从压缩包打开该文件
    comment_list.append(zf.getinfo(filename).comment.decode())
    content=f.read().decode()
    print(content)
    pattern=re.compile('[0-9]+')
    match=pattern.search(content)
    if match:
        num=match.group(0)
        filename=num+'.txt'
    else:
        break
end=''
for i in comment_list:
    end+=i
    print(end)

