#！ /usr/bin/python
from urllib import request
import re
url="http://www.pythonchallenge.com/pc/def/equality.html"
a_request=request.Request(url)
response=request.urlopen(a_request)
content=response.read().decode()
#print(content)
pattern=re.compile("<!--\nk[\d\D]+")#match the comment(begin with <!--
text=pattern.search(content)
text=text.group(0)
#print(type(text))
print(text)
pattern=re.compile("[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]")#根据题目要查找的东西实际上是那个小写字母，所以把全部匹配的小写字母连起来就是内容了
pattern=re.compile("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]")#或者查找分组
match=pattern.findall(text)
print(match)

