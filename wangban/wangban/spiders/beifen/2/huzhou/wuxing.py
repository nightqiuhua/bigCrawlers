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
from scrapy.http import Request
SETTINGS = get_project_settings()
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'wuxing.json')

@singleton
class WuXingSpider(DIYBaseSpider):
    name = 'wuxing'
    start_urls = ['http://ggzy.wuxing.gov.cn/']
    source_website = '湖州市吴兴区公共资源交易网'
    specific_area = '吴兴区'
    source_url = 'http://ggzy.wuxing.gov.cn/'
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []

    def __init__(self,jsonfile = JSONFILE,pre_suf=None,post_suf= 'http://ggzy.wuxing.gov.cn/hzgov/openapi/info/ajaxpagelist.do?pagesize=15&channelid={}&pageno={}'):
        super().__init__()
        self.xp = Json2XPath(jsonfile).get_xpath()
        self.post_suf = post_suf
        self.pre_suf = pre_suf


    def generate_request(self,links_dict=None,spider=None):
        if links_dict['type'] == 'sub':
            link_key = links_dict['an_sub_url']
            return Request(link_key,meta=links_dict,callback=self.parse_sub_pageurls,errback=self.errorsave,dont_filter=True)
        if links_dict['type'] == 'column':
            return Request(links_dict['an_column_url'],meta=links_dict,callback=self.parse_urls_incolumn,errback=self.errorsave,dont_filter=True)
        if links_dict['type'] == 'content':
            return Request(links_dict['an_url'],meta=links_dict,callback=spider.parse,errback=self.errorsave,dont_filter=True)



    def parse_sub_pageurls(self,response):
        total_page,channelid = self.get_totalpage(response)
        pipe = self.redis_conn.pipeline(True)
        for page in range(0,int(total_page)+1):
            page_url = self.cre_page_url(response.meta['an_sub_url'],page,channelid)
            response.meta['type'] = 'column'
            response.meta['total_page'] = int(total_page)
            response.meta['an_column_url'] = page_url
            input_value = json.dumps(response.meta)
            pipe.lpush(self.check_queue,input_value)
            page_url = ' '
        pipe.execute()

    def cre_page_url(self,f_p_url,page,channelid=1):
        if page == 0:
            page = 1
        if page == -1:
            page_url = f_p_url
        else:
            page_url = self.post_suf.format(channelid,page)
        #print('page_url',page_url)
        return page_url

    def get_totalpage(self,response):
        total_page = 1
        try:
            response_str = response.body.decode('utf-8')
            total_page = re.findall(r'"pageTotal":(\d+)',response_str)[0]
            channelid = re.findall(r'"channelid":(\d+)',response_str)[0]
        except Exception as e:
            total_page = 1
            print('get_totalpage error_reason',e)
            print('url',response.url)
        #print('total_page',total_page)
        #print('channelid',channelid)
        total_page = self.set_totalpage(total_page)
        return total_page,channelid

    def get_elements(self,response):
#        elements = response.xpath(self.xp.column)
#        return elements
        data = json.loads(response.text)
        #print(data["infolist"])
        return data["infolist"]

    def get_elem_url(self,element,response=None):
        an_url = self.source_url
        try:
            an_url =  element['url']
        except Exception as e:
            print('get_elem_url error',e)
            print('url',response.url)
        #print('an_url',an_url)
        return an_url

    def get_an_title(self,element,response=None):
        an_title = 'NONE'
        try:
            an_title = element['title']
        except Exception as e:
            print('get_an_title error_reason',e)
            print('url',response.url)
            an_title = 'NONE'
        #print('an_title',an_title)
        return an_title

    def get_on_date(self,element,response=None):
        on_date = 'NONE'
        try:
            on_date = element['daytime']
        except Exception as e:
            print('get_on_date error_reason',e)
            print('url',response.url)
            on_date = 'NONE'
        #print('on_date',on_date)
        return on_date
