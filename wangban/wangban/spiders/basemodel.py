from datetime import datetime
from scrapy.http import Request
from wangban_utils.redis_util import get_redis_conn
from scrapy.utils.project import get_project_settings
from modify_func import all_modify_func
import json
from urllib.parse import urljoin
SETTINGS = get_project_settings()

class DIYBaseSpider:
    def __init__(self):
        self.redis_conn = get_redis_conn()
        self.func_moc = all_modify_func[self.name]
        self.check_queue = SETTINGS['URLS_CHECK_TASKS']
        self.refined_totalpage = 2


    def generate_request(self,links_dict=None,spider=None):
        #print('type',links_dict['type'])
        if links_dict['type'] == 'sub':
            link_key = self.cre_page_url(links_dict['an_sub_url'],1)
            return Request(link_key,meta=links_dict,callback=self.parse_sub_pageurls,errback=self.errorsave,dont_filter=True)
        if links_dict['type'] == 'column':
            return Request(links_dict['an_column_url'],meta=links_dict,callback=self.parse_urls_incolumn,errback=self.errorsave,dont_filter=True)
        if links_dict['type'] == 'content':
            return Request(links_dict['an_url'],meta=links_dict,callback=spider.parse,errback=self.errorsave,dont_filter=True)


    def parse_sub_pageurls(self,response):
        total_page = self.get_totalpage(response)
        pipe = self.redis_conn.pipeline(True)
        for page in range(1,int(total_page)+1):
            page_url = self.cre_page_url(response.meta['an_sub_url'],page)
            response.meta['type'] = 'column'
            response.meta['total_page'] = int(total_page)
            response.meta['an_column_url'] = page_url
            input_value = json.dumps(response.meta)
            pipe.lpush(self.check_queue,input_value)
            page_url = ' '
        pipe.execute()

    def parse_urls_incolumn(self,response):
        pipe = self.redis_conn.pipeline(True)
        for element in self.get_percol_elements(response):
            an_value = {'an_major':response.meta['an_major'],
                        'an_type':response.meta['an_type'],'type':'content','name':response.meta['name']}
            an_value.update(element)
            input_value = json.dumps(an_value)
            pipe.lpush(self.check_queue,input_value)
        pipe.execute()

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
            element_dict['an_refer_total_page'] = self.get_rf_t_p(response)
            element_dict['an_county'] = self.get_an_county(element,response)
            element_dict['an_ref_page_items'] = len(elements)
            yield element_dict

    def errorsave(self,failure):
        pass

    def cre_page_url(self,f_p_url,page):
        if page == 0:
            page = 1
        if page == -1:
            page_url = urljoin(f_p_url,self.post_suf.format('1'))
        else:
            page_url = urljoin(f_p_url,self.post_suf.format(page))
        return page_url

    def contents_modify(self,response):
        return response

    def get_totalpage(self,response):
        total_page = 1
        try:
            total_page = response.xpath(self.xp.total_page).extract()[0]
        except Exception as e:
            print('get_totalpage error_reason',e)
            print('url',response.url)
            total_page = 1
        return total_page

    def get_elements(self,response):
        elements = []
        try:
            elements = response.xpath(self.xp.column)
        except Exception as e:
            print('get_elements error',e)
            elements = []
        return elements


    def get_rf_t_p(self,response):
        return response.meta['total_page']

    def get_elem_url(self,element,response=None):
        an_url = self.source_url
        try:
            elem_url = element.xpath(self.xp.an_url).extract()[0]
            an_url = urljoin(self.source_url,elem_url)
        except Exception as e:
            print('get_elem_url error',e)
            print('url',response.url)
            an_url = self.source_url
        #print('an_url',an_url)
        return an_url

    def get_an_title(self,element,response=None):
        an_title = 'NONE'
        try:
            an_title = element.xpath(self.xp.an_title).extract()[0]
        except Exception as e:
            print('get_an_title error',e)
            print('url',response.url)
        return an_title

    def get_on_date(self,element,response=None):
        on_date = 'NONE'
        try:
            on_date = element.xpath(self.xp.on_date).extract()[0]
        except Exception as e:
            print('get_on_date error',e)
            print('url',response.url)
            on_date = 'NONE'
        return on_date

    def get_an_sub(self,element,response):
        an_sub = response.meta['an_sub']
        return an_sub

    def get_an_county(self,element,response=None):
        an_county = 'NONE'
        return an_county


    def final_url(self,response):
        final_url = response.url
        return final_url

    def an_title_parse(self,response):
        an_title =response.meta['an_title']
        try:
            an_title = response.xpath(self.xp.an_text_title).extract()[0]
            an_title = re.sub(r'\s+',r'\s',an_title)
        except Exception as e:
            an_title =response.meta['an_title']
        return an_title

    def an_on_date_parse(self,response):
        return response.meta['on_date']

    def an_content(self,response):
        content = 'NONE'
        try:
            content = self.func_moc(response.text)
        except Exception as e:
            print(e)
            if response.url != self.source_url:
                return response.xpath('//body').extract()[0]
            else:
                raise e
        return content

    def set_totalpage(self,orignal):
        if int(orignal) > self.refined_totalpage:
            orignal = self.refined_totalpage
        return orignal