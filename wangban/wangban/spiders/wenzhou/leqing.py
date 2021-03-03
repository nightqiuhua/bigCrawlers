# -*- coding: utf-8 -*-
import os
from datetime import datetime
import os
from urllib.parse import urlparse
import re
import time
from wangban_utils.Json2Xpath import Json2XPath,XPath
from wangban_utils.single_mode import singleton
from urllib.parse import urljoin
from scrapy.utils.project import get_project_settings
from spiders.basemodel import DIYBaseSpider
SETTINGS = get_project_settings()
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'leqing.json')

@singleton
class LeQingSpider(DIYBaseSpider):
    name = 'leqing'
    start_urls = ['http://ztb.yueqing.gov.cn/']
    source_website = '温州市乐清市公共资源交易网'
    specific_area = '乐清'
    source_url = 'http://ztb.yueqing.gov.cn/yqweb/'
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []

    def __init__(self,jsonfile = JSONFILE):
        super().__init__()
        self.xp = Json2XPath(jsonfile).get_xpath()
        self.post_suf = '&Paging={}'


    def cre_page_url(self,f_p_url,page):
        if page == 0:
            page = 1
        page_url = f_p_url+self.post_suf.format(page)
        return page_url


    def get_on_date(self,element,response=None):
        try:
            on_date = element.xpath(self.xp.on_date).extract()[0]
            on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
        except Exception as e:
            on_date = 'NONE'
            print('get_on_date error',e)
            print('url',response.url)
        #print('on_date',on_date)
        return on_date


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

    def get_elem_url(self,element,response=None):
        an_url = self.source_url
        try:
            url = element.xpath(self.xp.an_url).extract()[0]
            url = re.findall('(/InfoDeta.*)',url)[0]
            an_url = self.source_url + url
        except Exception as e:
            print('get_elem_url error',e)
            print('url',response.url)
            an_url = self.source_url
        return an_url

    def get_an_title(self,element,response=None):
        an_title = 'NONE'
        try:
            an_title = element.xpath(self.xp.an_title).extract()[0]
            an_title = re.sub(r'\s+',r'\s',an_title)
        except Exception as e:
            print('get an title error',e)
            print('error url',response.url)
        return an_title

    def an_title_parse(self,response):
        an_title =response.meta['an_title']
        try:
            an_title = response.xpath('//h2/text()').extract()
            an_title = ''.join(an_title)
        except Exception as e:
            an_title =response.meta['an_title']
        return an_title