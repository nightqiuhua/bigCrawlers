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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'luqiao.json')


class LuQiaoSpider(RedisStaticSpider):
    name = 'luqiao'
    start_urls = ['http://www.zsptztb.com.cn']
    source_website = '路桥区人民政府信息公开'
    specific_area = '路桥'
    source_url = 'http://www.luqiao.gov.cn/'
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []

    def __init__(self,jsonfile = JSONFILE):
        super().__init__()
        self.xp = Json2XPath(jsonfile).get_xpath()
        self.post_suf = '&CurrentPageIndex={}'


    def get_on_date(self,element,response=None):
        try:
            on_date = element.xpath(self.xp.on_date).extract()[0]
            on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
        except Exception as e:
            on_date = 'NONE'
            print('get on date error',e)
            print('url',response.url)
        return on_date


    def get_totalpage(self,response):
        try:
            total_page = response.xpath(self.xp.total_page).extract()[0]
        except Exception as e:
            print('get_totalpage error_reason',e)
            print('url',response.url)
            total_page = 1
        if not len(total_page):
            total_page = 1
        #print('total_page is ',total_page)
        total_page = self.set_totalpage(total_page)
        return total_page

    def get_elem_url(self,element,response=None):
        an_url = self.source_url
        try:
            elem_url = element.xpath(self.xp.an_url).extract()[0]
            elem_url = urljoin(self.source_url,elem_url)
        except Exception as e:
            print('get_elem_url error',e)
            print('url',response.url)
            elem_url = self.source_url
        if 'http' in elem_url:
            an_url = elem_url
        else:
            an_url =  urljoin(self.source_url,elem_url)
        return an_url

    def cre_page_url(self,f_p_url,page):
        if page == 0:
            page = 1
        page_url = f_p_url + self.post_suf.format(page)
        return page_url