# -*- coding: utf-8 -*-

# Scrapy settings for githubspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os 

BOT_NAME = 'githubspider'

SPIDER_MODULES = ['githubspider.spiders']
NEWSPIDER_MODULE = 'githubspider.spiders'

DOWNLOAD_DELAY = 2


ziparchieve = os.getenv("HOME")+ '/desktop/githubrepo/'
archieve = os.getenv("HOME")+ '/desktop/code_archive/'

if not os.path.exists(ziparchieve):
  os.makedirs(ziparchieve)

if not os.path.exists(archieve):
  os.makedirs(archieve)

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'githubspider (+http://www.yourdomain.com)'
ITEM_PIPELINES = {
  'githubspider.pipelines.ZipPipeline': 300,
  'githubspider.pipelines.CodePipeline': 800,
  'githubspider.pipelines.StorePipeline': 1000,
}