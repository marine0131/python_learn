import re
from simple_crawler import Crawler, CrawlerCache

if __name__ == "__main__": 
    # Using SQLite as a cache to avoid pulling twice
    crawler = Crawler(CrawlerCache('crawler.db'))
    root_re = re.compile('^/$').match
    crawler.crawl('http://36kr.com/', no_cache=root_re)
    print(crawler.content['36kr.com'])
