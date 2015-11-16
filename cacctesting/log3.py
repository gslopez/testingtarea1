from scrapy.spiders import CrawlSpider

class MySpider2(CrawlSpider):
  name = 'myspider2'
  __module__ = "not_this_one"
