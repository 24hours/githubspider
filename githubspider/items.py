# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy

class GithubspiderItem(scrapy.Item):
  # define the fields for your item here like:
  url = scrapy.Field()
  file_name = scrapy.Field()
    
class CodeItem(scrapy.Item):
  # define the fields for your item here like:
  ori_name = scrapy.Field()
  name = scrapy.Field()
  code = scrapy.Field()
  type = scrapy.Field()