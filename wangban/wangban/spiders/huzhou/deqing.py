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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'deqing.json')

@singleton
class DeQingSpider(DIYBaseSpider):
    name = 'deqing'
    start_urls = ['http://www.dqztb.gov.cn/']
    source_website = '湖州市德清县公共资源交易网'
    specific_area = '德清县'
    source_url = 'http://www.dqztb.gov.cn/'
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []

    def __init__(self,jsonfile = JSONFILE):
        super().__init__()
        self.xp = Json2XPath(jsonfile).get_xpath()
        self.post_suf = 'index_{}.htm'
        self.pre_suf = None

    def cre_page_url(self,f_p_url,page):
        if page == 0:
            page = 1
        page_url = urljoin(f_p_url,self.post_suf.format(page))
        return page_url


    def get_totalpage(self,response):
        total_page = 1
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

    def get_elements(self,response):
        elements = response.xpath(self.xp.column)
        return elements

    def get_elem_url(self,element,response):
        an_url = self.source_url
        try:
            elem_url = element.xpath(self.xp.an_url).extract()[0]
            an_url = urljoin(self.source_url,elem_url)
        except Exception as e:
            print('get_elem_url error',e)
            print('url',response.url)
        #print('an_url',an_url)
        return an_url

    def get_an_title(self,element,response):
        an_title = 'NONE'
        try:
            an_title = element.xpath(self.xp.an_title).extract()[0]
        except Exception as e:
            an_title = 'NONE'
            print('get an title error',e)
            print('url',response.url)
        return an_title

    def get_on_date(self,element,response):
        on_date = 'NONE'
        try:
            on_date = element.xpath(self.xp.on_date).extract()[0]
            on_date = re.findall(r'\d+-\d+-\d+',on_date)[0]
        except Exception as e:
            on_date = 'NONE'
            print('get on date error',e)
            print('url',response.url)
        #print('on_date',on_date)
        return on_date

    def get_an_sub(self,element,response):
        an_sub = response.meta['an_sub']
        try:
            if len(element.xpath(self.xp.an_sub).extract()):
                an_sub = element.xpath(self.xp.an_sub).extract()[0]
        except Exception as e:
            an_sub = response.meta['an_sub']
            print('get an sub error',e)
            print('url',response.url)
        if an_sub == 'NULL':
            an_sub = 'NONE'
        return an_sub

    def an_content(self,response):
        content = 'NONE'
        try:
            content = self.func_moc(response.text,response.url)
        except Exception as e:
            print(e)
            if response.url != self.source_url:
                return response.xpath('//body').extract()[0]
            else:
                raise e
        return content