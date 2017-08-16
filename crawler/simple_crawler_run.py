import re
from simple_crawler import Crawler, CrawlerCache

if __name__ == "__main__": 
    # Using SQLite as a cache to avoid pulling twice
    crawler = Crawler(CrawlerCache('crawler.db')) #init a crawler object
    pattern = re.compile('^/$')#make regularity
    root_re = pattern.match #match
    crawler.crawl('http://36kr.com/subscribe?ktm_source=kaike_pclandingpage', no_cache=root_re)
    print(crawler.content['36kr.com'])
