import urllib.request
import re
import time

def geturl(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

while 1:
    try :
        html = geturl("http://m.91jin.com/hq/lists.html")
    
        现货银 = re.search('现货银([\s\S]{200})',html.decode("utf8"),flags=0).group()
        #美元指数 = re.search('美元指数([\s\S]{203})',html.decode("utf8"),flags=0).group()
        伦敦金 = re.search('伦敦金([\s\S]{203})',html.decode("utf8"),flags=0).group()
        伦敦银 = re.search('伦敦银([\s\S]{203})',html.decode("utf8"),flags=0).group()
        #美元指数 = re.findall('\d\d.\d+',美元指数)
        现货银 = re.findall('\d\d\d\d',现货银)
        伦敦金   = re.findall('\d\d\d\d\.\d+',伦敦金)
        伦敦银   = re.findall('\d\d\.\d\d',伦敦银)

        现货银 = (int(现货银[0])+int(现货银[1]))/2
        伦敦金   = (float(伦敦金[0])+float(伦敦金[1]))/2
        伦敦银   = (float(伦敦银[0])+float(伦敦银[1]))/2
        try :
            html2 = geturl("http://hq.sinajs.cn/list=hf_AGTD")
            白银延期 = re.search('AGTD([\s\S]{10})',html2.decode("gbk"),flags=0).group()
            白银延期 = re.findall('\d\d\d\d\.\d\d',白银延期)
            白银延期 = float(白银延期[0])
            实时溢价 = 白银延期 - 现货银
        except :
            time.sleep(0.01)

        print(time.strftime('%H:%M',time.localtime(time.time())))

        try :
            print("白银延期 =","%.0f"%白银延期)
        except :
            time.sleep(0.01)

        print("现货白银 =","%.0f"%现货银)

        try :
            print("实时溢价 =","%.0f"%实时溢价)
        except :
            time.sleep(0.01)

        print("伦敦金银 =","%.2f"%伦敦金,end=" ")
        print("/","%.2f"%伦敦银)

        time.sleep(59)

    except :
    	print(time.strftime('%H:%M',time.localtime(time.time())))
    	print("网络异常，将于30秒后重试")
    	time.sleep(30)