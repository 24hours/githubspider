# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.http import Request
import zipfile
from githubspider.items import CodeItem
from githubspider.settings import ziparchieve, archieve
import os , shutil

class ZipPipeline(object):
  def process_item(self, item, spider):
    z = zipfile.ZipFile(ziparchieve+item['file_name'])
    # req = Request("http://www.github.com"+item['url']+'/archieve/master.zip', callback=self.archieve)
    # req = Request("http://www.github.com", callback=self.archieve)
    for code in z.namelist():
      if code[-1] is not '/':
        code_file = CodeItem()
        z.extract(code)
        with open(code, 'rb') as f:
          code_file['code'] = f.read()

        code_file['ori_name'] = code
        code_file['name'] = code.split('/')[-1]
        code_file['type'] = code_file['name'].split('.')[-1]

        if not os.path.exists(archieve + '/' + code_file['type'] + '/'):
          os.makedirs(archieve + '/' + code_file['type'] + '/')
        with open(archieve + '/' + code_file['type'] + '/'+ code_file['ori_name'].replace('/', '_'), 'wb') as f:
          f.write(code_file['code'])

    shutil.rmtree(z.namelist()[0].split('/')[0])
    return item

class CodePipeline(object):
  def process_item(self, item, spider):
    return item

class StorePipeline(object):
  def process_item(self, item, spider):
    return item
