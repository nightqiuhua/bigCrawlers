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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'wencheng.json')

@singleton
class WenChengSpider(DIYBaseSpider):
    name = 'wencheng'
    start_urls = ['http://www.zsptztb.com.cn']
    source_website = '温州市文成县公共资源交易网'
    specific_area = '文成'
    source_url = 'http://www.wczbtb.com/wzcms/'
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
            total_page = response.xpath(self.xp.total_page).extract()
            total_page = ''.join(total_page)
            total_page = re.findall(r'/(\d+)页',total_page)[0]
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