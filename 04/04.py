#! /usr/bin/python
from urllib import request
import re
import string
url_var=""
while 1:
    url="http://www.pythonchallenge.com/pc/def/linkedlist.php"+url_var
    print(url)
    a_request=request.Request(url)
    response=request.urlopen(a_request)
    content=response.read().decode()
    print(content)
    pattern=re.compile('[\D]([\d]{4,})')
    match=pattern.findall(content)
    if match:
        url_var="?nothing="+str(match[0])
        print(url_var)
        #print(url)
    else:
        break

