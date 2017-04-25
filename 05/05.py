#！ /usr/bin/python
import urllib.request
import pickle
url="http://www.pythonchallenge.com/pc/def/banner.p"
a_request=urllib.request.Request(url)
response=urllib.request.urlopen(a_request)
content=response.read()#这里不要decode了，从服务器返回的数据是二进制流，也符合pickle的规则，下面要对二进制对象反序列化
#print(content)
#print(type(content))
#file=open("p.pk","wb")#pickle 要求以二进制写入文件    wb!!!!!!!
#pickle.dump(content,file,0)
banner=pickle.loads(content)
print(banner)#对网页中的字符串反序列化
print('\n'.join([''.join([j[0]*j[1] for j in i]) for i in banner]))#理解列表生成式：外层列表是[[j[0]*j[1] for j in i] for i in banner]
                                                                             #外层列表的元素是[j[0]*j[1] for j in i]，该元素又是一个列表生成式，即列表
                                                                             #内层列表是[j[0]*j[1] for j in i]
                                                                             #内层列表元素是j[0]*j[1]
                                                                             #现在以内层元素为分隔符，把'white space'join为一个字符串，该字符串做内层列表元素
                                                                             #然后以内层列表为分隔符，把'\n'join为一个字符串输出
#用for迭代表达为：
for i in banner:
    for j in i:
        print(j[0]*j[1] ,end='')
        #print('')
    print('')                 #这种方法要注意的问题是内层循环print不应该输出换行，print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
                              #由print定义，看出只要把默认值参数end='\n'换下来就行了



