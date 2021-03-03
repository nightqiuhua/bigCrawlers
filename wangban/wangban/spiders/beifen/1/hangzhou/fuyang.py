# -*- coding: utf-8 -*-
#import __init__
from spiders.redis_spider import RedisStaticSpider
import os
from wangban_utils.redis_util import get_redis_conn
from collections import defaultdict
from datetime import datetime
import os
from urllib.parse import urlparse
import re
import time
from wangban_utils.Json2Xpath import Json2XPath,XPath
from urllib.parse import urljoin
from scrapy.http import FormRequest
from scrapy.http import Request
from scrapy.utils.project import get_project_settings
import json
SETTINGS = get_project_settings()
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'fuyang.json')


class FuYangSpider(RedisStaticSpider):
    name = 'fuyang'
    start_urls = ['http://www.hzfyggzy.org.cn/']
    source_website = '杭州市富阳区公共资源交易网'
    specific_area = '富阳区'
    source_url = 'http://www.hzfyggzy.org.cn/'
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []
    def __init__(self,jsonfile = JSONFILE):
        super().__init__()
        self.xp = Json2XPath(jsonfile).get_xpath()
        self.post_suf = '&Paging={}'
        self.post_url ='http://www.hzfyggzy.org.cn/SecondPage/GetNotice'

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
                    yield Request(links_dict['an_url'],meta=links_dict,callback=self.parse,errback=self.errorsave,dont_filter=True)
                    found += 1
            except Exception as e:
                print('next_requests',e)



    def parse_sub_pageurls(self,response):
        #获取总页数信息，形成新的formdata
        total_page = self.get_totalpage(response)
        pipe = self.redis_conn.pipeline(True)
        for page in range(1,int(total_page)+1):
            response.meta['formdata']['page'] = str(page)
            response.meta['type'] = 'column'
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
            if response.meta['formdata']["afficheType"] in ['495','496']:
                an_url = 'http://www.hzfyggzy.org.cn/NewsShow/Home?id={}&ModuleID={}'.format(
                                    element["id"],response.meta['formdata']["afficheType"])
            else:
                if element.get("IsInner",'NONE') == 'NONE':
                    if element.get("LinkAddr",'NONE') == 'NONE':
                        an_url = 'http://www.hzfyggzy.org.cn/AfficheShow/Home?AfficheID={}&ModuleID={}'.format(
                                    element["ID"],response.meta['formdata']["afficheType"])
                    else:
                        an_url = 'http://www.hzfyggzy.org.cn/'+element["LinkAddr"]
                else:
                    an_url = 'http://www.hzfyggzy.org.cn/AfficheShow/Home?AfficheID={}&IsInner={}&ModuleID={}'.format(
                                                element["ID"],element["IsInner"],response.meta['formdata']["afficheType"])

        except Exception as e:
            print('get_elem_url error',e)
            print(response.meta['formdata'])
            an_url = self.source_url
        return an_url

    def get_an_title(self,element,response=None):
        an_title = 'NONE'
        try:
            if element.get("TenderName",None):
                an_title = element["TenderName"]
            else:
                an_title = element["title"]
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
        self.refined_totalpage =20
        total_page = self.set_totalpage(total_page)
        return total_page


    def an_on_date_parse(self,response):
        on_date = response.meta['on_date']
        if response.meta['an_type'] == "开标安排":
            on_date = response.xpath('//div[@class="AfficheTitle"]//text()').extract()
            on_date = ''.join(on_date)
            try:
                on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
            except Exception as e:
                pass
        return on_date
