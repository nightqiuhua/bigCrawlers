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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'zhejiang.json')
AREA_BASE = {
'杭州':['杭州','上城','下城','江干','拱墅','西湖','滨江','萧山','余杭','富阳','临安','桐庐','淳安','建德'],
'宁波':['宁波','海曙','江北','北仑','镇海','鄞州','奉化','余姚','慈溪','象山','宁海','国家高新区','大榭开发区','杭州湾新区','保税区'],
'温州':['温州','鹿城','龙湾','瓯海','洞头','瑞安','乐清','永嘉','平阳','苍南','文成','泰顺',],
'绍兴':['越城','柯桥','上虞','新昌','嵊州','诸暨'],
'金华':['婺城','金东','兰溪','义乌','东阳','永康','浦江','武义','磐安',],
'嘉兴':['嘉兴','南湖','秀洲','嘉善','海盐','海宁','平湖','桐乡',],
'湖州':['湖州','吴兴','南浔','德清','长兴','安吉',],
'衢州':['衢州','柯城','衢江','龙游','江山','常山','开化',],
'舟山':['定海','普陀','岱山','嵊泗',],
'台州':['椒江','黄岩','路桥','临海','温岭','玉环','天台','仙居','三门',],
}

@singleton
class ZheJiangSpider(DIYBaseSpider):
    name = 'zhejiang'
    start_urls = ['http://new.zmctc.com/zjgcjy/']
    source_website = '浙江省公共资源交易网'
    specific_area = '浙江'
    source_url = 'http://new.zmctc.com/'
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []
    def __init__(self,jsonfile = JSONFILE,pre_suf=None,post_suf= '?Paging={}'):
        super().__init__()
        self.xp = Json2XPath(jsonfile).get_xpath()
        self.post_suf = post_suf
        self.pre_suf = pre_suf

    def get_totalpage(self,response):
        try:
            total_page = response.xpath(self.xp.total_page).extract()[0]
            total_page = re.findall(r'/(\d+)',total_page)[0]
        except Exception as e:
            print('get_totalpage error_reason',e)
            print('url',response.url)
            total_page = 1
        #print('total_page is ',total_page)
        total_page = self.set_totalpage(total_page)
        return total_page

    def get_elem_url(self,element,response=None):
        an_url = self.source_url
        try:
            elem_url = element.xpath(self.xp.an_url).extract()[0]
            an_url = urljoin(self.source_url,elem_url)
        except Exception as e:
            print('get_elem_url error',e)
            print('url',response.url)
            an_url = self.source_url
        #print(an_url)
        return an_url

    def get_on_date(self,element,response=None):
        try:
            on_date = element.xpath(self.xp.on_date).extract()[0]
            on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
        except Exception as e:
            on_date = 'NONE'
            print('get on date error',e)
            print('url',response.url)
        #print(on_date)
        return on_date

    def get_an_title(self,element,response=None):
        an_title = 'NONE'
        try:
            an_title = element.xpath(self.xp.an_title).extract()[0]
        except Exception as e:
            print('get_an_title error',e)
            print('url',response.url)
        #print(an_title)
        return an_title

    def get_an_county(self,element,response=None):
        an_title = 'NONE'
        try:
            an_title = element.xpath(self.xp.an_title).extract()[0]
        except Exception as e:
            print('get_an_title error',e)
            print('url',response.url)
            an_title = 'NONE'
        if an_title == 'NONE':
            an_county = '省本级'
        else:
            result_list = {}
            for key,value_list in AREA_BASE.items():
                for area in value_list:
                    result = re.search(area,an_title)
                    if not result:
                        continue
                    else:
                        result_list[key]=result.span()[0]
                        break
            if not len(result_list):
                an_county = '省本级'
            else:
                an_county = min(result_list,key=lambda x:result_list[x])
        return an_county

    def cre_page_url(self,f_p_url,page):
        if page == 0:
            page = 1
        page_url = f_p_url + self.post_suf.format(page)
        return page_url