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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'dinghaiqu.json')

@singleton
class DingHaiQuSpider(DIYBaseSpider):
    name = 'dinghaiqu'
    start_urls = ['http://www.zsptztb.com.cn']
    source_website = '舟山市定海区公共资源交易网'
    specific_area = '定海区'
    source_url = 'http://www.dhggzy.cn/'
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []

    def __init__(self,jsonfile = JSONFILE):
        super().__init__()
        self.xp = Json2XPath(jsonfile).get_xpath()
        self.post_suf = '?Paging={}'

    def get_on_date(self,element,response=None):
        on_date = 'NONE'
        try:
            on_date = element.xpath(self.xp.on_date).extract()[0]
            on_date = re.findall(r'\d+-\d+-\d+',on_date)[0]
        except Exception as e:
            print('get date error',e)
            print('url',response.url)
            on_date = 'NONE'
        #print('on_date',on_date)
        return on_date

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

    def get_elem_url(self,element,response=None):
        an_url = self.source_url
        try:
            elem_url = element.xpath(self.xp.an_url).extract()[0]
            an_url = self.source_url + elem_url
        except Exception as e:
            print('get_elem_url error',e)
            print('url',response.url)
        return an_url
