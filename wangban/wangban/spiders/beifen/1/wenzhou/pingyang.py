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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'pingyang.json')


class PingYangSpider(RedisStaticSpider):
    name = 'pingyang'
    start_urls = ['http://www.tsztb.cn/TPFront/']
    source_website = '温州市平阳县公共资源交易网'
    specific_area = '平阳'
    source_url = 'http://www.pyztb.com'
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []

    def __init__(self,jsonfile = JSONFILE):
        super().__init__()
        self.xp = Json2XPath(jsonfile).get_xpath()
        self.post_suf = '?Paging={}'

    def cre_page_url(self,f_p_url,page):
        if page == 0:
            page = 1
        if 'ShowInfo' in f_p_url:
            page_url = f_p_url+'&Paging={}'.format(page)
        else:
            page_url = urljoin(f_p_url,self.post_suf.format(page))
        return page_url



    def get_totalpage(self,response):
        try:
            total_page = response.xpath(self.xp.total_page).extract()[0]
            total_page = re.findall(r'/(\d+)',total_page)[0]
        except Exception as e:
            print('get_totalpage error_reason',e)
            print('url',response.url)
            total_page = 1
        if not len(total_page):
            total_page = 1
        #print('total_page is ',total_page)
        total_page = self.set_totalpage(total_page)
        return total_page

    def get_elem_url(self,element,response):
        an_url = self.source_url
        try:
            an_url = self.source_url +element.xpath(self.xp.an_url).extract()[0]
        except Exception as e:
            print('get_elem_url error',e)
            print('url',response.url)
            an_url = self.source_url
        return an_url

    def get_on_date(self,element,response=None):
        on_date = 'NONE'
        try:
            on_date = element.xpath(self.xp.on_date).extract()[0]
            on_date = on_date.replace('.','-')
        except Exception as e:
            print('get_on_date error',e)
            print('url',response.url)
            on_date = 'NONE'
        return on_date