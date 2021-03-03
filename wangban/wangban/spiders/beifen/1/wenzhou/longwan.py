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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'longwan.json')


class LongWanSpider(RedisStaticSpider):
    name = 'longwan'
    start_urls = ['http://61.164.128.8:6081/']
    source_website = '温州市龙湾区公共资源交易网'
    specific_area = '龙湾区'
    source_url = 'http://61.164.128.8:6081/'
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
            total_page = response.xpath(self.xp.total_page).extract()[0]
            #print('total_page',total_page)
            total_page = re.findall(r'/(\d+)页',total_page)[0]
        except Exception as e:
            print('get_totalpage error_reason',e)
            print('url',response.url)
            total_page = 1
        if not len(total_page):
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