import urllib
import urllib.request
import re
import os
import requests

#get web source code
def getHtml(url):
	req=urllib.request.Request(url)
	page = urllib.request.urlopen(req)
	html = page.read()
	f=open("text.txt","w")
	print(html,file=f)
	return html

#url = r'http://tieba.baidu.com/p/3205263090'
url = r'https://www.zhihu.com/question/30891697'
dirpath='a/'

proxy= {"http" : "http://127.0.0.1:1080", "https": "http://127.0.0.1:1080"}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

if not os.path.isdir(dirpath):
	os.mkdir(dirpath)
print("requesting url:",url)
html = getHtml(url)

#generate a pattern
reg=r'src="([.*\S]*\.jpg)"'
pattern = re.compile(reg)

#find pattern
imgurls=re.findall(pattern,str(html))

index=1001
for item in imgurls:
	if item.startswith('//'):
		item = 'http:'+item
	print("downloading:", item)
	
	filename = os.path.join(dirpath, str(index)+'.jpg')
	
	urllib.request.urlretrieve(item,filename)
	index +=1
