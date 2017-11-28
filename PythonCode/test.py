import urllib.request
import urllib.parse
import json
content=0
while True:
        content=input("请输入需要翻译的内容:")
        if content!='quit':
                url="http://fanyi.baidu.com/v2transapi"
                data={}
                data['from']='en'
                data['to']='zh'
                data['query']=content
                data['transtype']='translang'
                data['simple_means_flag']='3'
                data=urllib.parse.urlencode(data).encode("utf-8")
                response=urllib.request.urlopen(url,data)
                html=response.read().decode("utf-8")
                target=json.loads(html)
                tgt=target['trans_result']['data'][0]['dst']
                print("翻译的结果是：%s"% tgt)
        else:
                break