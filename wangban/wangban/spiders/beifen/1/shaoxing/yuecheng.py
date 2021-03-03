# -*- coding: utf-8 -*-

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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'yuecheng.json')

@singleton
class YueChengSeleSpider(SeleCommander):
    name = 'yuecheng'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'
        self.source_url ='http://www.sxyc.gov.cn'

    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        try:
            total_page = driver.find_element_by_xpath(self.xp.total_page).get_attribute('href')
            total_page = re.findall(r'\d+',total_page)[-1]
        except Exception as e:
            total_page = '1'
            print('get total error',e)
            print(driver.current_url)
        #print('total_page',total_page)
        #self.refined_totalpage = 2
        total_page = self.set_totalpage(total_page)
        #print('total_page',total_page)
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
        if not an_title:
            an_title = 'NONE'
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
        if not on_date:
            on_date = 'NONE'
        return on_date

    def get_an_sub(self,an_sub,element,driver):
        return an_sub

    def get_an_county(self,element,driver):
        an_county = 'NONE'
        return an_county

    def get_elem_url(self,element,driver):
        element_url = self.source_url
        try:
            element_url = element.find_element_by_xpath(self.xp.an_url).get_attribute('href')
        except Exception as e:
            print('get element url error',e)
            print(driver.current_url)
        if not element_url:
            element_url = self.source_url
        return element_url

    def click_next_page(self,driver,page):
        try:
            driver.find_element_by_xpath(self.xp.input_page).clear()
            driver.find_element_by_xpath(self.xp.input_page).send_keys('{}'.format(page+1))
            driver.find_element_by_xpath(self.xp.input_page).send_keys(Keys.ENTER)
            time.sleep(7)
        except Exception as e:
            driver.find_element_by_xpath(self.xp.next_page).click()
            time.sleep(7)

        
    
class YueChengSpider(RedisStaticSpider):
    name = 'yuecheng'
    start_urls = ['http://www.sxyc.gov.cn']
    source_website = '绍兴市越城区公共资源交易网'
    specific_area = '越城'
    source_url = 'http://www.sxyc.gov.cn'
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []

