# -*- coding: utf-8 -*-
from spiders.redis_spider import RedisStaticSpider
import os
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
from scrapy.http import FormRequest
from scrapy.http import Request
from scrapy.utils.project import get_project_settings
import json
import requests
SETTINGS = get_project_settings()
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'jinhua_ajax.json')

class JinHhua_AjaxSpider(RedisStaticSpider):
    name = 'jinhua_ajax'
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
        self.post_suf = '&Paging={}'


    def next_requests(self):
        fetch_one = self.redis_conn.lpop
        found = 0
        while found < self.redis_batch_size:
            data = fetch_one(self.work_queue)
            found += 1
            if not data:
                break 
            links_dict = json.loads(data.decode('utf-8'))
            if links_dict['type'] == 'sub':
                formdata = {'pagesize': '10'}
                yield FormRequest(links_dict['an_sub_url'],meta=links_dict,formdata= formdata,callback=self.parse_sub_pageurls,errback=self.errorsave,dont_filter=True)
            if links_dict['type'] == 'column':
                formdata = links_dict['formdata']
                yield FormRequest(links_dict['an_column_url'],meta=links_dict,formdata=formdata,callback=self.parse_urls_incolumn,errback=self.errorsave,dont_filter=True)
            if links_dict['type'] == 'content':
                link_key = 'http://www.jhztb.gov.cn/platform/noticeController.do?getNotice'
                formdata = links_dict['formdata']
                yield FormRequest(link_key,meta=links_dict,formdata=formdata,callback=self.parse,errback=self.errorsave,dont_filter=True)
                



    def parse_sub_pageurls(self,response):
        #获取总页数信息，形成新的formdata
        total_page = self.get_totalpage(response)
        pipe = self.redis_conn.pipeline(True)
        for page in range(0,int(total_page)+1):
            response.meta['formdata']['pagesize'] = str(10)
            response.meta['type'] = 'column'
            page_url = self.cre_page_url(response.meta['an_sub_url'],page)
            response.meta['an_column_url'] = page_url
            input_value = json.dumps(response.meta)
            pipe.rpush(self.check_queue,input_value)
            page_url = ' '
        pipe.execute()

    def cre_page_url(self,f_p_url,page):
        page_url = re.sub('&page=0','&page={}'.format(page),f_p_url)
        #print(page_url)
        return page_url


    def get_percol_elements(self,response):
        main_contents = self.contents_modify(response)
        elements = self.get_elements(main_contents)
        for element in elements:
            element_dict = {}
            element_url = self.get_elem_url(element,response)
            if element_url == self.source_url:
                continue
            element_dict['an_url']= element_url
            element_dict['an_title'] = self.get_an_title(element,response)
            element_dict['on_date'] = self.get_on_date(element,response)
            element_dict['an_sub'] = self.get_an_sub(element,response)
            element_dict['an_sub_origal'] = response.meta['an_sub']
            element_dict['an_refer_url'] = response.url
            element_dict['an_nominal_url'] = self.get_an_nominal_url(element,response)
            element_dict['an_county'] = self.get_an_county(element,response)
            element_dict['an_ref_page_items'] = len(elements)
            element_dict['formdata'] = self.get_an_formdata(element,response)
            yield element_dict

    def contents_modify(self,response):
        main_content = json.loads(response.body.decode('utf-8'))
        return main_content

    def get_elements(self,response):
        elements = response['data']
        return elements

    def get_elem_url(self,element,response=None):
        an_url = self.source_url
        try:
            an_url = 'http://www.jhztb.gov.cn/platform/project/notice/notice.jsp?id=' + element['seq_id']
        except Exception as e:
            print('get_elem_url error',e)
            print(response.meta['formdata'])
            an_url = self.source_url
        #print(an_url)
        return an_url


    def get_an_nominal_url(self,element,repsonse=None):
        an_nominal_url = 'http://www.zjzfcg.gov.cn/'
        try:
            an_nominal_url = 'http://www.jhztb.gov.cn/platform/project/notice/notice.jsp?id=' + element['seq_id']
        except Exception as e:
            print('an_nominal_url error',e)
            print(response.meta['formdata'])
            an_url = self.source_url
        #print(an_nominal_url)
        return an_nominal_url


    def get_an_title(self,element,response=None):
        an_title = 'NONE'
        try:
            an_title = element["title"]
        except Exception as e:
            print('get an title error',e)
            print(response.meta['formdata'])
        #print('an_title',an_title)
        return an_title

    def get_on_date(self,element,response=None):
        try:
            on_date = element["send_time"]
            on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
        except Exception as e:
            on_date = 'NONE'
            print('get_on_date error',e)
            print(response.meta['formdata'])
        #print('on_date',on_date)
        return on_date

    def get_an_formdata(self,element,response=None):
        try:
            formdata = {}
            formdata = {'id':element['seq_id']}
        except Exception as e:
            on_date = 'NONE'
            print('get_on_date error',e)
            print(response.meta['formdata'])
        #print('on_date',on_date)
        return formdata


    def get_totalpage(self,response):
        try:
            content= json.loads(response.body.decode('utf-8'))
            total_page = content['pageCount']
        except Exception as e:
            print('get_totalpage error_reason',e)
            print(response.meta['formdata'])
            total_page = 1
        #print('total_page is ',total_page)
        #print('total_page',total_page)
        total_page = self.set_totalpage(total_page)
        return total_page

    def get_an_county(self,element,response=None):
        an_county = 'NONE'
        try:
            an_county = element["sypa_name"]
        except Exception as e:
            print('get_an_county error',e)
            print(response.meta['formdata'])
            an_county = 'NONE'
        #print('an_county',an_county)
        return an_county

    def final_url(self,response):
        final_url = response.meta['an_nominal_url']
        return final_url




    def an_content(self,response):
        content = json.loads(response.body.decode('utf-8'))
        file = self.get_downloadfile(content)

        try:
            final_content = content['announcement']
        except Exception as e:
            if response.url != self.source_url:
                item_result = dict(items)
                self.info_instance.record_error_data(item_result,self.name)
            raise e
        if len(file):
            final_content = final_content + file
        return final_content

    def get_downloadfile(self,content):
        m = content['seqId']
        post_url = 'http://www.jhztb.gov.cn/platform/noticeController.do?getAttachList'
        formdata = {'atta_owerguid':m}
        HEADERS =  {#'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                 'User-Agent': 'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI 6 Build/NMF26X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',

            }
        try:
            json_data = requests.post(post_url,formdata,headers=HEADERS)
        except Exception as e:
            raise e
        data = json.loads(json_data.text)
        html = ''
        try:
            for item in data["data"]:
                href = 'http://www.jhztb.gov.cn/platform/' + item['atta_path']
                html = html +'<a href="{}" >{}</a>'.format(href,item['atta_name'])
        except Exception as e:
            return None

        return html
