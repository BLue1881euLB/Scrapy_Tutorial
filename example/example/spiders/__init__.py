# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from ..items import BookItem
from scrapy.linkextractors import LinkExtractor
class BookSpider(scrapy.Spider):

   name = "books"

   start_urls = ['http://books.toscrape.com/']

   def parse(self, response):
       for sel in response.css('article.product_pod'):

           book = BookItem()
           book['name'] = sel.xpath('./h3/a/@title').extract_first()
           book['price'] = sel.css('p.price_color::text').extract_first()
           yield book
       # next_url = response.css('ul.pager li.next a::attr(href)').extract_first()
       # if next_url:
       #     next_url = response.urljoin(next_url)
       #     yield scrapy.Request(next_url,callback=self.parse)
       #

       le = LinkExtractor(restrict_css="ul.pager li.next")
       links = le.extract_links(response)
       if links:
           next_url = links[0].url
           yield scrapy.Request(next_url,callback=self.parse)

