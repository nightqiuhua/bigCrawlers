# -*- coding: utf-8 -*-
#import __init__
from spiders.selecrawlers.selecommander import SeleCommander
from wangban_utils.updatefilterfunc import UpdateFilterClass
from wangban_utils.Json2Xpath import Json2XPath,XPath
from wangban_utils.single_mode import singleton
from spiders.redis_spider import RedisStaticSpider
import os
from datetime import datetime
from urllib.parse import urlparse
import re
import time
from urllib.parse import urljoin
from scrapy.http import FormRequest
from scrapy.http import Request
from scrapy.utils.project import get_project_settings
import json
SETTINGS = get_project_settings()
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'hangzhou.json')


class HangZhouSpider(RedisStaticSpider):
    name = 'hangzhou'
    start_urls = ['http://www.hzctc.cn/']
    source_website = '杭州市公共资源交易网'
    specific_area = '杭州'
    source_url = 'http://www.hzctc.cn/'
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []
    def __init__(self,jsonfile = JSONFILE):
        super().__init__()
        self.xp = Json2XPath(jsonfile).get_xpath()
        self.post_suf = '&Paging={}'
        self.pre_suf = None
        self.post_url ='http://www.hzctc.cn/SecondPage/GetNotice'

    def next_requests(self):
        fetch_one = self.redis_conn.lpop
        found = 0
        #self.schedule_to_works()
        while found < self.redis_batch_size:
            data = fetch_one(self.work_queue)
            if not data:
                break 
            links_dict = json.loads(data.decode('utf-8'))
            try:
                if links_dict['type'] == 'sub':
                    formdata = links_dict['formdata']
                    yield FormRequest(self.post_url,meta=links_dict,formdata= formdata,callback=self.parse_sub_pageurls,errback=self.errorsave,dont_filter=True)
                if links_dict['type'] == 'column':
                    formdata = links_dict['formdata']
                    yield FormRequest(self.post_url,meta=links_dict,formdata=formdata,callback=self.parse_urls_incolumn,errback=self.errorsave,dont_filter=True)
                if links_dict['type'] == 'content':
                    if 'ModuleID=486' in links_dict['an_url']:
                        self.redis_conn.lpush(SETTINGS['SUB_SELE_TASKS'],data)
                        continue
                    yield Request(links_dict['an_url'],meta=links_dict,callback=self.parse,errback=self.errorsave,dont_filter=True)
                    
            except Exception as e:
                print('next_requests',e)



    def parse_sub_pageurls(self,response):
        #获取总页数信息，形成新的formdata
        total_page = self.get_totalpage(response)
        pipe = self.redis_conn.pipeline(True)
        for page in range(1,int(total_page)+1):
            response.meta['formdata']['page'] = str(page)
            response.meta['type'] = 'column'
            response.meta['an_column_url'] = ''
            input_value = json.dumps(response.meta)
            pipe.rpush(self.check_queue,input_value)
        pipe.execute()

    def get_rf_t_p(self,response):
        return 'NONE'


    def contents_modify(self,response):
        main_content = json.loads(response.body.decode('utf-8'))
        return main_content

    def get_elements(self,response):
        elements = response['rows']
        return elements

    def get_elem_url(self,element,response=None):
        an_url = self.source_url
        try:
            if response.meta['formdata']["afficheType"] == "486":
                an_url = 'http://www.hzctc.cn/OpenBidRecord/Index?id={}&tenderID={}&ModuleID={}'.format(
                                    element["ID"],element["TenderID"],response.meta['formdata']["afficheType"])
            else:
                an_url = 'http://www.hzctc.cn/AfficheShow/Home?AfficheID={}&IsInner={}&ModuleID={}'.format(
                                            element["ID"],element["IsInner"],response.meta['formdata']["afficheType"])
        except Exception as e:
            print('get_elem_url error',e)
            print(response.meta['formdata'])
            an_url = self.source_url
        #print(an_url)
        return an_url

    def get_an_title(self,element,response=None):
        an_title = 'NONE'
        try:
            an_title = element["TenderName"]
        except Exception as e:
            print('get an title error',e)
            print(response.meta['formdata'])
        #print('an_title',an_title)
        return an_title

    def get_on_date(self,element,response=None):
        try:
            on_date = element["PublishStartTime"]
            on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
        except Exception as e:
            on_date = 'NONE'
            print('get_on_date error',e)
            print(response.meta['formdata'])
        #print('on_date',on_date)
        return on_date


    def get_totalpage(self,response):
        try:
            content= json.loads(response.body.decode('utf-8'))
            total_page = content['total']
        except Exception as e:
            print('get_totalpage error_reason',e)
            print(response.meta['formdata'])
            total_page = 1
        #print('total_page is ',total_page)
        #print('total_page',total_page)
        self.refined_totalpage = 6
        total_page = self.set_totalpage(total_page)
        return total_page

    def get_an_county(self,element,response=None):
        an_county = 'NONE'
        try:
            an_county = element["CodeName"]
        except Exception as e:
            print('get_an_county error',e)
            print(response.meta['formdata'])
            an_county = 'NONE'
        #print('an_county',an_county)
        return an_county

@singleton
class HangZhouSeleSpider(SeleCommander):
    name = 'hangzhou'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'
        self.selecontent_enabled =True
        self.source_website = '杭州市公共资源交易网'
        self.specific_area = '杭州'