from urllib import request
import urllib
import json

def ItemSelect(cho,text):
    if cho=="1":
        language_from="en"
        language_to="zh"
    else:
        language_from="zh"
        language_to="en"
    # en为英文,zh为中文
    Url="http://fanyi.baidu.com/v2transapi"
    # 对应翻译地址的URL
    Data={"from":language_from,"to":language_to,"query":text,"transtype":"translang","simple_means_flag":"3"}
    # 对应的一些data
    return Data,Url

if __name__ == "__main__":
    # cho=input("1、英译中\n2、中译英\n")
    cho=2
    data={}
    ofile=open("in.txt","r",encoding="utf-8")
    ifile=open("out.txt","w")
    for line in ofile.readlines():
        nowstr=str(line).strip()
        if len(nowstr)>0:
            data,url=ItemSelect(cho,nowstr)
            newdata=urllib.parse.urlencode(data).encode("utf-8")
            # 用urlencode方法转换标准格式
            response=request.urlopen(url,newdata)
            # 传递url和转换格式的数据
            html=response.read().decode("utf-8")
            # 读取信息并解码
            resultmsg=json.loads(html)
            # 用json进行解析
            result=resultmsg['trans_result']['data'][0]['dst']
            # 得到最终的结果
            ifile.write(result)
        ifile.write("\n")
    ofile.close()
    ifile.close()
    
