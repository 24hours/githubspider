import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from githubspider.items import GithubspiderItem
from scrapy.http import Request
from githubspider.settings import ziparchieve

class GithubSpider(scrapy.Spider):
  name = 'github'
  allowed_domains = ['github.com']
  start_urls = ['https://github.com/search?p='+str(i)+ '&q=stars%3A%3E1&type=Repositories' for i in range(1,101)]

  def parse(self, response):
    for repo in response.css('h3.repo-list-name').xpath('a/@href'):
      github = GithubspiderItem()
      github['url'] =repo.extract()
      req = Request("http://www.github.com/"+github['url']+'/archive/master.zip', callback=self.archieve)

      req.meta['item'] = github    
      yield req

  def archieve(self, response):
    item = response.meta['item']
    item['file_name'] = item['url'].replace('/', '_') + '.zip'
    with open(ziparchieve+item['file_name'], 'wb') as f:
      f.write(response.body)
    return item
