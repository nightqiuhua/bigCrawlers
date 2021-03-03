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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'qujiang.json')

@singleton
class QuJiangSpider(DIYBaseSpider):
    name = 'qujiang'
    start_urls = ['http://www.qjggzy.com/']
    source_website = '衢州市衢江区公共资源交易网'
    specific_area = '衢江区'
    source_url = 'http://www.qjggzy.com/'
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
            #
            total_page = response.xpath(self.xp.total_page).extract()[0]
            #print('total_page',total_page)
            total_page = re.findall(r'/(\d+)页',total_page)[0]
            #print('total_page',total_page)
        except Exception as e:
            print('get_totalpage error_reason',e)
            print('response_url',response.url)
            total_page = 1
        #print('total_page is ',total_page)
        total_page = self.set_totalpage(total_page)
        return total_page



