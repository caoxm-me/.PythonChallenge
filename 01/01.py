#! /usr/bin/python
import string
str1="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp." \
    " bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle." \
    " sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
intab=string.ascii_lowercase
outtab=(intab+'ab')[2:]
transtab=str.maketrans(intab,outtab)#建立字符转换映射表
str2=str1.translate(transtab)
print(str2)
url1="http://www.pythonchallenge.com/pc/def/map.html"
url2=url1.translate(transtab)
print(url2)


