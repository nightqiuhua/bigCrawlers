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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'jiangshan.json')


class JiangShanSpider(RedisStaticSpider):
    name = 'jiangshan'
    start_urls = ['http://www.jsztb.org/']
    source_website = '江山市公共资源交易中心'
    specific_area = '江山市'
    source_url = 'http://www.jsztb.org/'
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []

    def __init__(self,jsonfile = JSONFILE):
        super().__init__()
        self.xp = Json2XPath(jsonfile).get_xpath()
        self.post_suf = '?page={}'

    def cre_page_url(self,f_p_url,page):
        if page == 0:
            page = 1
        page_url = f_p_url+self.post_suf.format(page)
        #print('page_url',page_url)
        return page_url


    def get_totalpage(self,response):
        total_page = 1
        try:
            
            if 'nccq' in response.url:
                total_page = response.xpath(self.xp.total_page_nccq).extract()[0]
            else:
                total_page = response.xpath(self.xp.total_page).extract()
                #print('total_page',total_page)
                total_page = total_page[-1]
            print('total_page',total_page)
        except Exception as e:
            print('get_totalpage error_reason',e)
            print('response_url',response.url)
            total_page = 1
        #print('total_page is ',total_page)
        total_page = self.set_totalpage(total_page)
        return total_page


    def get_elements(self,response):
        try:
            if 'nccq' in response.url:
                elements = response.xpath(self.xp.column_nccq)
            else:
                elements = response.xpath(self.xp.column)
        except Exception as e:
            print('get_elements error',e)
            print('response_url',response.url)
        return elements

    def get_elem_url(self,element,response):
        an_url = self.source_url
        try:
            if 'nccq' in response.url:
                elem_url = element.xpath(self.xp.an_url_nccq).extract()[0]
                an_url = urljoin('http://www.jsztb.org/nccq/',elem_url)
            else:
                elem_url = element.xpath(self.xp.an_url).extract()[0]
                an_url = urljoin(self.source_url,elem_url)
        except Exception as e:
            print('get_elem_url error',e)
            print('response_url',response.url)
        return an_url

    def get_an_title(self,element,response=None):
        an_title = 'NONE'
        try:
            if 'nccq' in response.url:
                an_title = element.xpath(self.xp.an_title_nccq).extract()[0]
            else:
                an_title = element.xpath(self.xp.an_title).extract()[0]
        except Exception as e:
            print('response_url',response.url)
            an_title = 'NONE'
        return an_title

    def get_on_date(self,element,response=None):
        on_date = 'NONE'
        try:
            if 'nccq' in response.url:
                on_date = element.xpath(self.xp.on_date_nccq).extract()[0]
                on_date = re.findall(r'(\d+)年(\d+)月(\d+)日',on_date)[0]
                on_date = '-'.join(list(on_date))
            else:
                on_date = element.xpath(self.xp.on_date).extract()[0]
                on_date = re.sub('/','-',on_date)
        except Exception as e:
            print('response_url',response.url)
            on_date = 'NONE'
        return on_date

