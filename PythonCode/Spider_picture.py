from urllib import request
import urllib
import re
import os


url="http://www.tsumino.com/Book/Info/36117/ningyou-yuugi-"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req=request.Request(url=url,headers=headers)
html=request.urlopen(req).read()
html=html.decode('utf-8')
r = re.compile('<img class="img-responsive reader-img".+')
r2= re.compile('<img.+')
allimg=r2.findall(html)
print(allimg)
picture_url_list = r.findall(html)  
os.mkdir('photos')
os.chdir(os.path.join(os.getcwd(), 'photos'))  
for i in range(len(picture_url_list)):  
    picture_name = str(i) + '.jpg'  
    try:  
        urllib.request.urlretrieve(picture_url_list[i], picture_name)  
        print("Success to download " + picture_url_list[i])  
    except:  
        print("Fail to download " + picture_url_list[i])  


