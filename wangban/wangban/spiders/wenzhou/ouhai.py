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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'ouhai.json')

@singleton
class OuHaiSpider(DIYBaseSpider):
    name = 'ouhai'
    start_urls = ['http://ohztb.ouhai.gov.cn/']
    source_website = '温州市瓯海区公共资源交易网'
    specific_area = '瓯海区'
    source_url = 'http://ohztb.ouhai.gov.cn/'
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []

    def __init__(self,jsonfile = JSONFILE):
        super().__init__()
        self.xp = Json2XPath(jsonfile).get_xpath()
        self.post_suf = 'index_{}.htm'


    def get_totalpage(self,response):
        total_page = 1
        try:
            #print('response_url',response.url)
            total_page = response.xpath(self.xp.total_page).extract()
            #print('total_page',total_page)
            total_page = total_page[-1]
            #print('total_page',total_page)
        except Exception as e:
            print('get_totalpage error_reason',e)
            print('url',response.url)
            total_page = 1
        #print('total_page is ',total_page)
        total_page = self.set_totalpage(total_page)
        return total_page

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



