import urllib.request
import re
import time
import socket

def geturl(url):
	timeout = 3
	socket.setdefaulttimeout(timeout)
	response = urllib.request.urlopen(url)
	html = response.read()
	return html

while 1:
	print(time.strftime('%H:%M',time.localtime(time.time())))
	#数据获取部分


	try :
		html = geturl("http://m.91jin.com/hq/lists.html")
		
		silver = re.search('现货银([\s\S]{200})',html.decode("utf8"),flags=0).group()
		xau = re.search('伦敦金([\s\S]{200})',html.decode("utf8"),flags=0).group()
		xag = re.search('伦敦银([\s\S]{200})',html.decode("utf8"),flags=0).group()

		silver = re.findall('\d\d\d\d',silver)
		xau = re.findall('\d+\.\d+',xau)
		xag = re.findall('\d+\.\d+',xag)

		silver = (int(silver[0])+int(silver[1]))/2
		xau = (float(xau[0])+float(xau[1]))/2
		xag = (float(xag[0])+float(xag[1]))/2

		status_91jin = 1
	except :
		'''
		try :
			html = geturl("https://www.91guoxin.com/ajax/gethq?callback=jQuery17208165182760740075_1478135156291&code=LSAG15&dec=4&_=1478135156373")
			silver = re.search('sell([\s\S]{8})',html.decode("gbk"),flags=0).group()
			silver = re.findall('\d\d\d\d',silver)
			silver = float(silver[0])
			status_91jin = 1
		except :
			status_91jin = 0
			'''
		status_91jin = 0

	try :
		html3 = geturl("http://hq.sinajs.cn/?_=1477967082802/&list=hf_XAU")
		xau = re.search('XAU([\s\S]{20})',html3.decode("gbk"),flags=0).group()
		xau = re.findall('\d+\.\d+',xau)
		xau = float(xau[0])
		status_sinaxau = 1
	except :
		status_sinaxau = 0
	try :
		html4 = geturl("http://hq.sinajs.cn/?_=1477967353119/&list=hf_XAG")
		xag = re.search('XAG([\s\S]{20})',html4.decode("gbk"),flags=0).group()
		xag = re.findall('\d+\.\d+',xag)
		xag = float(xag[0])
		status_sinaxag = 1
	except :
		status_sinaxag = 0

	try :
		html2 = geturl("http://hq.sinajs.cn/list=hf_AGTD")
		agtd = re.search('AGTD([\s\S]{10})',html2.decode("gbk"),flags=0).group()
		agtd = re.findall('\d\d\d\d\.\d\d',agtd)
		agtd = float(agtd[0])
		status_sinaagtd = 1
	except :
		status_sinaagtd = 0

	try :
		html5 = geturl("http://hq.sinajs.cn/rn=1477903719956list=DINIW")
		usdx = re.search('DINIW([\s\S]{40})',html5.decode("gbk"),flags=0).group()
		usdx = re.findall('\d+\.\d+',usdx)
		usdx = float(usdx[0])
		status_sinausdx = 1
	except :
		status_sinausdx = 0

	#输出部分
	#print(time.strftime('%H:%M',time.localtime(time.time())))
	if status_sinaagtd==1 :
		print("AGTD   ","%.0f"%agtd)
	else :
		print("AGTD异常")

	if status_91jin==1 :
		print("Silver ","%.0f"%silver)
	if status_sinaagtd==1 and status_91jin==1 :
		minus = agtd - silver
		print("Minus  ","%.0f"%minus)
	if status_91jin==1 :
		print("XAUAG  ","%.2f"%xau,end=" / ")
		print("%.3f"%xag)
	elif status_sinaxau==1 and status_sinaxag==1 :
		print("COMEX  ","%.2f"%xau,end=" / ")
		print("%.3f"%xag)
	elif status_sinaxau==1 :
		print("COMEX  ","%.2f"%xau)
	elif status_sinaxag==1 :
		print("COMEX  ","%.3f"%xag)
	if status_sinausdx==1 :
		print("USDX   ","%.4f"%usdx)

	time.sleep(57)
