#coding:utf-8
from urllib import request
import urllib
import re
import zlib
import os 

class Comic:
    def __init__(self,save):
        self.base_url = "http://comic.kukudm.com"
        self.base_comic_url = "http://comic.kukudm.com/comiclist/1733"
        self.save_path = save
        self.error_list = []
    
    def loadAllComic(self):
        html = self.getHtml(self.base_comic_url)
        # print (html)
        pattern = re.compile('<dl id=\'comiclistn\'>.*?</dl>')
        item = str(re.findall(pattern,html))
        pattern = re.compile('/comiclist/.*?htm', re.S)
        item = re.findall(pattern,item)
        self.pic_list = sorted(list(set(item)),key=item.index)
        self.pic_sum = len(self.pic_list)
        count = 0
        for x in self.pic_list:
            now_comic_url = self.base_url + str(x)
            html = self.getHtml(now_comic_url)
            if html==None:
                continue
            self.title, self.title_num, self.pages = self.getTitle(html)
            if self.title_num==0 or self.title_num==49 or self.title_num==52 or self.title_num==65 or self.title_num==75 or self.title_num==4 or self.title_num==5 or self.title_num==191 or self.title_num==179 or self.title_num==95 or self.title_num==84 or self.title_num==82 or self.title_num==159 or self.title_num==165 or self.title_num==172 or self.title_num==248 or self.title_num==252:
                count = 0
            now_comic_url = now_comic_url[:-5]
            print ("save "+self.title)
            for i in range(1,self.pages+1):
                html = self.getHtml(now_comic_url + str(i) + ".htm")
                if self.title_num==45 or self.title_num==53 or self.title_num==51 or self.title_num==66 or self.title_num==68 or self.title_num==69 or self.title_num==74 or self.title_num==177 or self.title_num==180 or self.title_num==94 or self.title_num==83 or self.title_num==81 or self.title_num==158 or self.title_num==164 or self.title_num==171 or self.title_num==246 or self.title_num==249:
                    print ("break")
                    count = 1
                if html==None:
                    continue
                self.now_pic_url = self.getPicUrl(html,count)
                flag = self.savePicture(i)
                if flag:
                    break
        ofile = open("errorlist.txt",'w')
        for x in self.error_list:
            ofile.write(str(x)+"\n")
        ofile.close()

    def getHtml(self,url):
        try:
            headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',
                    }
            req = request.Request(url=url,headers=headers)
            response = request.urlopen(req, timeout=15)
            data = response.read()
            # 将网页内容解压缩
            # decompressed_data = zlib.decompress(data, 16 + zlib.MAX_WBITS)
            # 网页编码格式为 gb2312
            html = data.decode('gb2312', 'ignore')
            return html
        except Exception as e:
            print (e)
            print ("open url: " + url + " failed.")
            return None

    def getPicUrl(self,html,count):
        try:
            base_url = "http://n.1whour.com/"
            pattern = re.compile('newkuku.*?jpg', re.S)
            items = re.findall(pattern, html)[0]
            if count>0:
                i = items.find("罪")
                j = items.find("/",i)
                items = items[:j] + "話" + items[j:]
            pic_url = base_url + items
            return pic_url
            # pic_url = self.base_url + items
            # pattern = re.compile('<img alt.*?src="(.*?)".*?/>', re.S)
            # image_url = re.search(pattern, html).groups()[0]
            # image_url = self.base_url + image_url
            # return image_url, pic_url
        except Exception as e:
            print (e)
            print ("Get picurl failed.")
            return None, None

    def getTitle(self,html):
        try:
            pattern = re.compile('>[七原罪|原罪].*?<', re.S)
            info = str(re.findall(pattern, html)[1])[1:-1]
            info = info.split("|")
            title = str(info[0]).replace(' ','')
            if title[0]=="原":
                title = "七" + title
            titlenum = re.sub("\D","",title)
            if titlenum!='':
                titlenum = int(titlenum)
            else:
                titlenum = 0
            pages = str(info[1]).replace(' ','')[1:-1]
            return title, titlenum, int(pages)
        except Exception as e:
            print (e)
            print ("Get title failed.")
            return None, None

    def savePicture(self,num):
        headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'
                }
        if self.title_num==171:
            i = self.now_pic_url.find("化")
            self.now_pic_url = self.now_pic_url[:i-1] + "漢化組" + self.now_pic_url[i+2:]
        nowurl = urllib.parse.quote(self.now_pic_url)
        nowurl = nowurl.replace("%3A",":")
        req = request.Request(url=nowurl,headers=headers)
        req.add_header('GET', nowurl)
        try:
            path = self.save_path + "/" + self.title
            print ("save picture url:" + nowurl)
            exists = os.path.exists(path)
            if not exists:
                print ("Creat document.")
                os.makedirs(path)
            else:
                print ("The document exists.")
                if self.pages <= len(os.listdir(path)):
                    print ("All the files exist.")
                    return True
            numstr = "0"
            if num<10:
                numstr += "00"
            elif num<100:
                numstr += "0"
            else:
                numstr=numstr
            numstr += str(num)
            path = path + "/" + numstr + ".jpg"
            if os.path.exists(path):
                print ("The file exists.")
            else:
                resp = request.urlopen(req, timeout=15)
                data = resp.read()
                fp = open(path, "wb")
                fp.write(data)
                fp.close()
                print ("save pic: finished.")
            return False
        except Exception as e:
            print (e)
            print ("save pic: " + nowurl + " failed.")
            self.error_list.append("Save " + self.title + " failed")
            return True