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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'tiantai.json')


class TianTaiSpider(RedisStaticSpider):
    name = 'tiantai'
    start_urls = ['http://www.zsptztb.com.cn']
    source_website = '天台县公共资源交易网'
    specific_area = '天台'
    source_url = 'http://www.ttzbtbzx.gov.cn/'
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []

    def __init__(self,jsonfile = JSONFILE):
        super().__init__()
        self.xp = Json2XPath(jsonfile).get_xpath()
        self.post_suf = 'index_{}.htm'

    def get_totalpage(self,response):
        try:
            total_page = response.xpath(self.xp.total_page).extract()[0]
            total_page = re.findall(r'/(\d+)',total_page)[0]
        except Exception as e:
            print('get_totalpage error_reason',e)
            total_page = 1
            print('url',response.url)
        #print('total_page',total_page)
        total_page = self.set_totalpage(total_page)
        return total_page

    def get_on_date(self,element,response):
        on_date = 'NONE'
        try:
            on_date = element.xpath(self.xp.on_date).extract()[0]
            on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
        except Exception as e:
            on_date = 'NONE'
            print('get_on_date error',e)
            print('url',response.url)
        #print('on_data',on_date)
        return on_date

    def get_elem_url(self,element,response):
        try:
            url = element.xpath(self.xp.an_url).extract()[0]
            an_url = urljoin(self.source_url,url)
        except Exception as e:
            print('get_elem_url error',e)
            print('url',response.url)
        #print('an_url',an_url)
        return an_url

    def get_an_title(self,element,response):
        try:
            an_title = element.xpath(self.xp.an_title).extract()[0]
            an_title = re.sub('\s+',' ',an_title)
            an_title = re.sub('\n',' ',an_title)
        except Exception as e:
            an_title = 'NONE'
            print('get_an_title error',e)
            print('url',response.url)
        return an_title

    def cre_page_url(self,f_p_url,page):
        if page == 0:
            page = 1
        page_url = urljoin(f_p_url,self.post_suf.format(page))
        return page_url
