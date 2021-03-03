# -*- coding: utf-8 -*-
#import __init__
from spiders.selecrawlers.selecommander import SeleCommander
from spiders.redis_spider import RedisStaticSpider
from wangban_utils.redis_util import get_redis_conn
from collections import defaultdict
import socket
from datetime import datetime
import os
from items import HangzhouItem
import time
import re
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
from wangban_utils.redis_util import get_redis_conn
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from wangban_utils.Json2Xpath import Json2XPath,XPath
from scrapy.utils.project import get_project_settings
from selenium.webdriver.common.keys import Keys
from wangban_utils.single_mode import singleton
SETTINGS = get_project_settings()
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'zhejiangsj.json')

@singleton
class ZheJiangSJSeleSpider(SeleCommander):
    name = 'zhejiangsj'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'
        self.source_url ='http://sjt.zj.gov.cn/'

    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        try:
            total_page = driver.find_element_by_xpath(self.xp.total_page).text
        except Exception as e:
            total_page = '1'
            print('get total error',e)
            print(driver.current_url)
        #print('total_page',total_page)
        total_page = self.set_totalpage(total_page)
        return total_page

    def presence_elements(self,driver):
        return self.xp.column

    def get_elements(self,driver):
        try:
            elements = driver.find_elements_by_xpath(self.xp.column)
        except Exception as e:
            print('get_elements error',e)
            print(driver.current_url)
            elements = []
        return elements

    def get_an_title(self,element,driver):
        an_title = 'NONE'
        try:
            an_title = element.find_element_by_xpath(self.xp.an_title).get_attribute('title')
        except Exception as e:
            print('get an title error',e)
            print(driver.current_url)
        return an_title



    def get_on_date(self,element,driver):
        on_date = 'NONE'
        try:
            on_date = element.find_element_by_xpath(self.xp.on_date).get_attribute('href')
            on_date = re.findall(r'\d{4}/\d{1,2}/\d{1,2}',on_date)[0]
            on_date = re.sub(r'/','-',on_date)
        except Exception as e:
            print('get on date error',e)
            print(driver.current_url)
        #print('on_date',on_date)
        return on_date


    def get_elem_url(self,elem,driver):
        element_url = self.source_url
        try:
            element_url = elem.find_element_by_xpath(self.xp.an_url).get_attribute('href')
        except Exception as e:
            print('get elem url error',e)
            print(driver.current_url)
        #print(element_url)
        return element_url

    def get_an_county(self,element,driver):
        an_county = '浙江'
        return an_county


    def click_next_page(self,driver,page):
        try:
            driver.find_element_by_xpath(self.xp.input_value).clear()
            driver.find_element_by_xpath(self.xp.input_value).send_keys('{}'.format(page+1))
            driver.find_element_by_xpath(self.xp.input_value).send_keys(Keys.ENTER) 
            time.sleep(7)
        except Exception as e:
            print(driver.current_url)
            time.sleep(7)



class ZheJiangSJSpider(RedisStaticSpider):
    name = 'zhejiangsj'
    post_suf= '__page_{}'
    start_urls = ['http://sjt.zj.gov.cn/']
    source_website = '浙江省审计厅官网'
    source_url = 'http://sjt.zj.gov.cn/'
    specific_area = '浙江'
    jsonfile = JSONFILE
    specific_sele_spider = ZheJiangSJSeleSpider
    links_tree = {}
    loss_urls = {}
    count = 0
    column_urls_pool = []


    def parse(self,response):
        items = HangzhouItem()
        self.count += 1
        try:
            items['url'] = response.url
            items['project'] = 'hangzhou'
            items['spider'] = self.name
            items['server'] = socket.gethostname()
            items['crawling_date'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            #primary fields 
            items['source_website'] = self.source_website
            items['website_area'] = self.specific_area
            items['specific_area'] = response.meta['an_county']
            items['an_type'] = response.meta['an_type']
            items['an_major'] = response.meta['an_major']
            items['an_sub'] = response.meta['an_sub']
            items['project_title']=self.an_title_parse(response)
            items['on_date'] = self.an_on_date_parse(response)
            items['an_title'] = self.an_title_parse(response)
            items['an_url'] = self.final_url(response)
            items['an_refer_url'] = response.meta['an_refer_url']
            items['crawling_number'] = '1'
            items['an_content'] = self.an_content(response)
            items['code'] = self.count
        except Exception as e:
            print('parse error',response.url)
            print('parse error',e)
        else:
            return items