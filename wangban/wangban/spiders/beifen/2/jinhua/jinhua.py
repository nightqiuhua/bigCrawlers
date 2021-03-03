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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'jinhua.json')

@singleton
class JinHuaSpider(DIYBaseSpider):
    name = 'jinhua'
    start_urls = ['http://www.jhztb.gov.cn/']
    source_website = '金华市公共资源交易网'
    specific_area = '金华'
    source_url = 'http://www.jhztb.gov.cn/'
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []

    def __init__(self,jsonfile = JSONFILE):
        super().__init__()
        self.xp = Json2XPath(jsonfile).get_xpath()
        self.post_suf = 'index_{}.htm'

    def get_elements(self,response):
        if '01' in response.url:
            elements = response.xpath('//ul[@class="ny_right_list clearfix"]/li')
        else:
            elements = response.xpath(self.xp.column)
        return elements

    def get_totalpage(self,response):
        try:
            if '01' in response.url:
                total_page = re.findall(r'countPage =(.*);',response.text)[0]
                total_page = re.sub(r'\s+','',total_page)
            else:
                total_page = response.xpath(self.xp.total_page).extract()[0]
                total_page = re.findall(r'/(\d+)',total_page)[0]
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
            if '01' in response.url:
                elem_url = element.xpath('./span[1]/a/@href').extract()[0]
                an_url = urljoin(response.url,elem_url)
            else:
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
            if '01' in response.url:
                on_date = element.xpath('./span[@class="date"]/text()').extract()[0]
                on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
            else:
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
            if '01' in response.url:
                an_title = element.xpath('./span[1]/a/@title').extract()[0]
                an_title = re.sub(r'\s+','',an_title)
            else:
                an_title = element.xpath(self.xp.an_title).extract()[0]
                an_title = re.sub(r'\s+','',an_title)
        except Exception as e:
            print('get_an_title error',e)
            print('url',response.url)
            an_title = 'NONE'
        #print(an_title)
        return an_title

    def cre_page_url(self,f_p_url,page):
        if page == 0:
            page = 1
        if '01' in f_p_url:
            page_url = urljoin(f_p_url,'index_{}.html'.format(page))
        else:
            page_url = urljoin(f_p_url,self.post_suf.format(page))
        #print(page_url)
        return page_url

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