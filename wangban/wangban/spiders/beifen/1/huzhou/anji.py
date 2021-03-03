# -*- coding: utf-8 -*-
from spiders.redis_spider import RedisStaticSpider
from wangban_utils.redis_util import get_redis_conn
from collections import defaultdict
from datetime import datetime
import os
from urllib.parse import urlparse
import re
import time
from urllib.parse import urljoin
from scrapy.utils.project import get_project_settings
from wangban_utils.Json2Xpath import Json2XPath,XPath
import math
SETTINGS = get_project_settings()
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'anji.json')



class AnJiSpider(RedisStaticSpider):
    name = 'anji'
    post_suf= '__page_{}'
    start_urls = ['http://www.ajztb.com/']
    source_url = 'http://www.ajztb.com/'
    jsonfile = JSONFILE
    source_website = '湖州市安吉县公共资源交易网'
    specific_area = '安吉'
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []
    
    def __init__(self,jsonfile = JSONFILE):
        super().__init__()
        self.xp = Json2XPath(jsonfile).get_xpath()
        self.post_suf = '{}.html'
        

    def get_totalpage(self,response):
        try:
            pageSize = re.findall(r"pageSize: (\d+),",response.body.decode('utf-8'))[0]
            total = re.findall(r"total: (\d+),",response.body.decode('utf-8'))[0]
            total_page = math.ceil(int(total)/int(pageSize))
        except Exception as e:
            print('get_totalpage error_reason',e)
            print('url',response.url)
            total_page = 1
        #print('total_page is ',total_page)
        total_page = self.set_totalpage(total_page)
        return total_page

    def get_elem_url(self,element,response=None):
        an_url = self.source_url
        try:
            elem_url = element.xpath(self.xp.an_url).extract()[0]
            an_url = urljoin(self.source_url,elem_url)
        except Exception as e:
            print('get_elem_url error',e)
            print('url',response.url)
            an_url = self.source_url
        #print(an_url)
        return an_url

    def get_on_date(self,element,response=None):
        try:
            on_date = element.xpath(self.xp.on_date).extract()[0]
            on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
        except Exception as e:
            on_date = 'NONE'
            print('get on date error',e)
            print('url',response.url)
        #print(on_date)
        return on_date

    def get_an_title(self,element,response=None):
        an_title = 'NONE'
        try:
            an_title = element.xpath(self.xp.an_title).extract()[0]
            an_title = re.sub(r'\s+','',an_title)
        except Exception as e:
            print('get_an_title error',e)
            print('url',response.url)
        #print(an_title)
        return an_title

    def get_an_county(self,element,response):
        an_county = response.meta['an_sub']
        return an_county

    def cre_page_url(self,f_p_url,page):
        if page == 1:
            page = 'moreinfo'
        page_url = f_p_url.replace('moreinfo.html',self.post_suf.format(page))
        #print(page_url)
        return page_url