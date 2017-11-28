from urllib import request
# 用于爬虫的包
response=request.urlopen("http://www.baidu.com/")
# 打开URL
print(response.geturl())
# 得到URL
print(response.info())
# 得到<meta>标记的信息
print(response.getcode())
# 得到http状态码,200表示成功
testhtml=response.read()
# 读取URL内的信息
testhtml=testhtml.decode('utf-8','ignore')
# 将信息转换为utf-8格式编码
print(str(testhtml))

ifile=open("testhtml.html",'w',encoding="utf-8")
# 注意一定要用uft-8编码打开
ifile.write(str(testhtml))
ifile.close()

# print(s1)

import re
# 用utf-8进行编码

ofile=open("testhtml.html","r",encoding="utf-8")
# 注意一定要用uft-8编码打开
for line in ofile.readlines():
    #print(str(line))
    if re.match(r'^.+<link.+>$',str(line)):
        print(line)
    # 得到所有的链接字段
ofile.close()

ofile=open("testhtml.html","r",encoding="utf-8")
for line in ofile.readlines():
    #print(str(line))
    if re.match('^[\.|#].+{.+}$',str(line)):
        print(line)
    # 得到所有的style
ofile.close()

ofile=open("testhtml.html","r",encoding="utf-8")
for line in ofile.readlines():
    #print(str(line))
    if re.match(r'^.+<meta.+>$',str(line)):
        print(line)
    # 得到所有的<meta>
ofile.close()