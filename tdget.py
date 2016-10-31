import urllib.request
import re
import time

while 1<2:
    try :
        response = urllib.request.urlopen("http://ag.cngold.org/bytd/")
        html = response.read()
        
        白银TD = re.search('JO_9754q2([\s\S]{10})',html.decode("utf8"),flags=0).group()

        白银TD = re.findall('\d\d\d\d\.\d\d',白银TD)

        #print(html.decode("utf8"))
        
        
        白银TD = float(白银TD[0])
        #溢价     = 白银延期 - 现货白银
       

        print(time.strftime('%H:%M',time.localtime(time.time())))
        #print("美元指数 =","%.3f"%美元指数)
        print("白银TD = ",白银TD)
        #print("伦敦金 =","%.3f"%伦敦金)
        #print("伦敦银 =","%.3f"%伦敦银)
        #print("BTC =",btc)
        #print("实时溢价 =",溢价)
        time.sleep(60)

    except :
        print("网络异常，将于100秒后重试")
        time.sleep(100)
