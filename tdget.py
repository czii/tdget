import urllib.request
import re
import time

def geturl(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

while 1:
	print(time.strftime('%H:%M',time.localtime(time.time())))
	#数据获取部分
	try :
		html = geturl("http://m.91jin.com/hq/lists.html")
		现货银 = re.search('现货银([\s\S]{200})',html.decode("utf8"),flags=0).group()
		伦敦金 = re.search('伦敦金([\s\S]{200})',html.decode("utf8"),flags=0).group()
		伦敦银 = re.search('伦敦银([\s\S]{200})',html.decode("utf8"),flags=0).group()

		现货银 = re.findall('\d\d\d\d',现货银)
		伦敦金 = re.findall('\d+\.\d+',伦敦金)
		伦敦银 = re.findall('\d+\.\d+',伦敦银)

		现货银 = (int(现货银[0])+int(现货银[1]))/2
		伦敦金 = (float(伦敦金[0])+float(伦敦金[1]))/2
		伦敦银 = (float(伦敦银[0])+float(伦敦银[1]))/2
	except :
		print("91jin网络异常")
		time.sleep(0.01)
		try :
			html3 = geturl("http://hq.sinajs.cn/?_=1477967082802/&list=hf_XAU")
			伦敦金 = re.search('XAU([\s\S]{20})',html3.decode("gbk"),flags=0).group()
			伦敦金 = re.findall('\d+\.\d+',伦敦金)
			伦敦金 = float(伦敦金[0])
		except :
			print("sina_XAU异常")
			time.sleep(0.01)
		try :
			html4 = geturl("http://hq.sinajs.cn/?_=1477967353119/&list=hf_XAG")
			伦敦银 = re.search('XAG([\s\S]{20})',html4.decode("gbk"),flags=0).group()
			伦敦银 = re.findall('\d+\.\d+',伦敦银)
			伦敦银 = float(伦敦银[0])
		except :
			print("sina_XAG异常")
			time.sleep(0.01)

	try :
		html2 = geturl("http://hq.sinajs.cn/list=hf_AGTD")
		白银延期 = re.search('AGTD([\s\S]{10})',html2.decode("gbk"),flags=0).group()
		白银延期 = re.findall('\d\d\d\d\.\d\d',白银延期)
		白银延期 = float(白银延期[0])
	except :
		print("sina_AGTD网络异常")
		time.sleep(0.01)

	try :
		html5 = geturl("http://hq.sinajs.cn/rn=1477903719956list=DINIW")
		美元指数 = re.search('DINIW([\s\S]{40})',html5.decode("gbk"),flags=0).group()
		美元指数 = re.findall('\d+\.\d+',美元指数)
		美元指数 = float(美元指数[0])
	except :
		print("sina_USD异常")
		time.sleep(0.01)

	#输出部分
	#print(time.strftime('%H:%M',time.localtime(time.time())))
	try :
		print("白银延期 =","%.0f"%白银延期)
	except :
		time.sleep(0.01)
	try :
		print("现货白银 =","%.0f"%现货银)
	except :
		time.sleep(0.01)
	try :
		实时溢价 = 白银延期 - 现货银
		print("实时溢价 =","%.0f"%实时溢价)
	except :
		time.sleep(0.01)
	try :
		print("伦敦金银 =","%.2f"%伦敦金,end=" / ")
		print("%.3f"%伦敦银)
	except :
		try :
			print("伦敦银 =","%.3f"%伦敦银)
		except :
			time.sleep(0.01)
	try :
		print("美元指数 =","%.4f"%美元指数)
	except :
		time.sleep(0.01)

	time.sleep(59)
