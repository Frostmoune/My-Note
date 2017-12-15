from urllib import request

headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
# 伪装成Chrome用户
req=request.Request("http://library.sysu.edu.cn/",headers=headers)
response=request.urlopen(req)
SYSUhtml=response.read()
SYSUhtml=SYSUhtml.decode('utf-8','ignore')

import re

more=re.compile(r'"(http://.*?)"',re.S)
# 网页链接的正则表达式
urllista=more.findall(SYSUhtml)
more=re.compile(r'"(\.\./.+?)"',re.S)
urllistb=[x for x in more.findall(SYSUhtml) if x[-3:]=='htm' or x[-2:]=='cn' or x[-3:]=='com']
# print(urllistb)
more=re.compile(r'"(\w+?/.+?)"',re.S)
urllistc=[x for x in more.findall(SYSUhtml) if x[-3:]=='htm' or x[-2:]=='cn' or x[-3:]=='com']
# print(urllistc)
more=re.compile(r'"(/.+?)"',re.S)
urllistd=[x for x in more.findall(SYSUhtml) if x[-3:]=='htm' or x[-2:]=='cn' or x[-3:]=='com']

ifile=open("SYSU_library.txt",'w',encoding="utf-8")
ifile.write(str(SYSUhtml))
ifile.close()

ifile=open("SYSY_library_all_href.txt","w",encoding="utf-8")
for x in urllista:
    ifile.write(x)
    ifile.write("\n")
for x in urllistb:
    ifile.write(x)
    ifile.write("\n")
for x in urllistc:
    ifile.write(x)
    ifile.write("\n")