# -*- coding: utf-8 -*-
#import __init__
from spiders.redis_spider import RedisStaticSpider
from wangban_utils.redis_util import get_redis_conn
from collections import defaultdict
import socket
from datetime import datetime
import os
from urllib.parse import urlparse
import re
import time
from wangban_utils.Json2Xpath import Json2XPath,XPath
from urllib.parse import urljoin
from scrapy.utils.project import get_project_settings
SETTINGS = get_project_settings()
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'daxiekaifaqu.json')


class DaXieKaiFaQuSpider(RedisStaticSpider):
    name = 'daxiekaifaqu'
    start_urls = ['http://daxie.bidding.gov.cn/']
    source_website = '宁波市大榭开发区公共资源交易网'
    specific_area = '大榭开发区'
    source_url = 'http://daxie.bidding.gov.cn/'
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []

    def __init__(self,jsonfile = JSONFILE):
        super().__init__()
        self.xp = Json2XPath(jsonfile).get_xpath()
        self.post_suf = 'index_{}'

    def get_totalpage(self,response):
        try:
            total_page = response.xpath(self.xp.total_page).extract()[0]
            #print(response.xpath(self.xp.total_page).extract())
            total_page = re.findall(r'/(\d+)页',total_page)[0]
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
        except Exception as e:
            print('get_an_title error',e)
            print('url',response.url)
        #print(an_title)
        return an_title

    def cre_page_url(self,f_p_url,page):
        if page == 0:
            page = 1
        page_url = f_p_url.replace('index',self.post_suf.format(page))
        #print('page_url',page_url)
        return page_url