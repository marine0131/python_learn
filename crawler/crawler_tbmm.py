import urllib
import urllib.request
import re
import time

#get web source code
def getHtml(raw_url,page_index):
	url=raw_url+"?page="+str(page_index)
	req=urllib.request.Request(url)
	page = urllib.request.urlopen(req)
	html = page.read().decode('gbk')
	return html
	
	
html = getHtml('http://mm.taobao.com/json/request_top_list.htm',2)

#generate a pattern
pattern1='src="([.*\S]*\.jpg)"'
pattern2='<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>'

imagereg = re.compile(pattern2)

imgurls=re.findall(imagereg,str(html))

x=1001
for item in imgurls:
	print(item[0],item[1],item[2],item[3],item[4])
	#urllib.request.urlretrieve(imgurl,'/home/whj/Downloads/crawler/%s.jpg' % x)
	x+=1
