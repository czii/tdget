import urllib.request
import re
import time

while 1:
    try :
        response = urllib.request.urlopen("http://m.91jin.com/hq/lists.html")
        html = response.read()
        
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
            response2 = urllib.request.urlopen("http://hq.sinajs.cn/list=hf_AGTD")
            html2 = response2.read()
            白银延期 = re.search('AGTD([\s\S]{10})',html2.decode("gbk"),flags=0).group()
            白银延期 = re.findall('\d\d\d\d\.\d\d',白银延期)
            白银延期 = float(白银延期[0])
            实时溢价 = 白银延期 - 现货银
        except :
            time.sleep(3)


        print(time.strftime('%H:%M',time.localtime(time.time())))
        try:
            print("AGTD =","%.0f"%白银延期)
        except:
            time.sleep(1)
        print("现货 =","%.0f"%现货银)
        try:
            print("溢价 =","%.0f"%实时溢价)
        except:
            time.sleep(1)
        print("伦敦 =","%.2f"%伦敦金, end='')
        print(" /","%.2f"%伦敦银)
        #print("BTC =",btc)


        time.sleep(60)

    except :
    	print(time.strftime('%H:%M',time.localtime(time.time())))
    	print("网络异常，将于20秒后重试")
    	time.sleep(20)
