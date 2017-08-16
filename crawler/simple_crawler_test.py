import sqlite3  
import urllib  
from html.parser import HTMLParser
from urllib.parse import urlparse
import urllib.request

def crawl(url, no_cache=None):
    u_parse = urlparse(url)#url parse, get scheme,netloc,path,param,query,fragment
    domain = u_parse.netloc#the main website,ie:url='http://www.baidu.com/index.php?username=guol' netloc='www.baidu.com'
    content={}
    content[domain] = {}
    scheme = u_parse.scheme#scheme = 'http'or'https'...
    no_cache = no_cache
    print('scheme:',u_parse.scheme)
    print('netloc:',u_parse.netloc)
    print('path:',u_parse.path)
    #self._crawl([u_parse.path], self.depth)

crawl("http://36kr.com/subscribe?ktm_source=kaike_pclandingpage")
