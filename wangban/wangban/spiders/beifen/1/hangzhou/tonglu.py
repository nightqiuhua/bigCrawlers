# -*- coding: utf-8 -*-
from spiders.selecrawlers.selecommander import SeleCommander
from spiders.redis_spider import RedisStaticSpider
import os
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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'tonglu.json')

@singleton
class TongLuSeleSpider(SeleCommander):
    name = 'tonglu'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'


    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        try:
            total_page = driver.find_element_by_xpath(self.xp.total_page).text
            int(total_page)
        except Exception as e:
            total_page = '1'
            print('get total error',e)
            print(driver.current_url)
        #print('total_page',total_page)
        total_page = self.set_totalpage(total_page)
        return total_page


    def presence_elements(self,driver):
        if 'Bulletin' in driver.current_url:
            pre_elem = self.xp.column
        if 'EnterHonestInfoList' in driver.current_url:
            pre_elem = self.xp.column
        if 'qypbt' in driver.current_url:
            pre_elem = self.xp.column_qypbt
        if 'gysxx' in driver.current_url:
            pre_elem = self.xp.column_AfficheList
        if 'AfficheList' in driver.current_url:
            pre_elem = self.xp.column_AfficheList
        return pre_elem

    def get_elements(self,driver):
        try:
            if 'Bulletin' in driver.current_url:
                elements = driver.find_elements_by_xpath(self.xp.column)
            if 'EnterHonestInfoList' in driver.current_url:
                elements = driver.find_elements_by_xpath(self.xp.column)
            if 'qypbt' in driver.current_url:
                elements = driver.find_elements_by_xpath(self.xp.column_qypbt)
            if 'gysxx' in driver.current_url:
                elements = driver.find_elements_by_xpath(self.xp.column_AfficheList)
            if 'AfficheList' in driver.current_url:
                elements = driver.find_elements_by_xpath(self.xp.column_AfficheList)
        except Exception as e:
            print('get_elements error',e)
            print(driver.current_url)
            elements = []
        return elements

    def get_an_title(self,element,driver):
        an_title = 'NONE'
        try:
            if 'Bulletin' in driver.current_url:
                if 'Bulletin1' in driver.current_url:
                    an_title = element.find_element_by_xpath(self.xp.an_title_Bulletin1).text
                    an_title = re.sub(r'\s+',r'\s',an_title)
                else:
                    an_title = element.find_element_by_xpath(self.xp.an_title).get_attribute('title')
            if 'EnterHonestInfoList' in driver.current_url:
                    an_title = element.find_element_by_xpath(self.xp.an_title_Bulletin1).text
                    an_title = re.sub(r'\s+',r'\s',an_title)
            if 'qypbt' in driver.current_url:
                an_title = element.find_element_by_xpath(self.xp.an_title_qypbt).text
                an_title = re.sub(r'\s+',r'\s',an_title)
            if 'gysxx' in driver.current_url:
                an_title = element.find_element_by_xpath(self.xp.an_title_AfficheList).get_attribute('title')
            if 'AfficheList' in driver.current_url:
                an_title = element.find_element_by_xpath(self.xp.an_title_AfficheList).get_attribute('title')
        except Exception as e:
            print('get an title error',e)
            print(driver.current_url)
        if not an_title:
            an_title = 'NONE'
        return an_title

    def get_on_date(self,element,driver):
        on_date = 'NONE'
        try:
            if 'Bulletin' in driver.current_url:
                on_date = element.find_element_by_xpath(self.xp.on_date).text
            if 'qypbt' in driver.current_url:
                on_date = element.find_element_by_xpath(self.xp.on_date_qypbt).text
            if 'gysxx' in driver.current_url:
                on_date = element.find_element_by_xpath(self.xp.on_date_AfficheList).text
                on_date = re.findall(r'(\d+/\d+/\d+)',on_date)[0]
            if 'AfficheList' in driver.current_url:
                on_date = element.find_element_by_xpath(self.xp.on_date_AfficheList).text
            if 'EnterHonestInfoList' in driver.current_url:
                on_date = element.find_element_by_xpath(self.xp.on_date_EnterHonestInfoList).text
            on_date = re.sub(r'\s+',r'\s',on_date)
        except Exception as e:
            print('get on date error',e)
            print(driver.current_url)
        if not on_date:
            on_date = 'NONE'
        return on_date

    def get_elem_url(self,element,driver):
        element_url = 'http://www.tlztb.com.cn'
        try:
            if 'Bulletin' in driver.current_url:
                if 'Bulletin1' in driver.current_url:
                    element_url = element.find_element_by_xpath(self.xp.an_url_Bulletin1).get_attribute('href')
                else:
                    element_url = element.find_element_by_xpath(self.xp.an_url).get_attribute('href')
            if 'EnterHonestInfoList' in driver.current_url:
                element_url = element.find_element_by_xpath(self.xp.an_url_Bulletin1).get_attribute('href')
            if 'qypbt' in driver.current_url:
                element_url = element.find_element_by_xpath(self.xp.an_url_qypbt).get_attribute('href')
            if 'gysxx' in driver.current_url:
                element_url = element.find_element_by_xpath(self.xp.an_url_AfficheList).get_attribute('href')
            if 'AfficheList' in driver.current_url:
                element_url = element.find_element_by_xpath(self.xp.an_url_AfficheList).get_attribute('href')
        except Exception as e:
            print('get element url error',e)
            print(driver.current_url)
        if not element_url:
            element_url = 'http://www.tlztb.com.cn'
        return element_url

    def click_next_page(self,driver,page):
        try:
            driver.find_element_by_link_text(self.xp.next_page).click()
            time.sleep(7)
        except Exception as e:
            print('click next page error',e)
            print(driver.current_url)
            driver.find_element_by_link_text(self.xp.next_page).click()#点击翻页
            time.sleep(7)

class TongLuSpider(RedisStaticSpider):
    name = 'tonglu'
    post_suf= '__page_{}'
    start_urls = ['http://www.tlztb.com.cn']
    jsonfile = JSONFILE
    source_url = 'http://www.tlztb.com.cn'
    source_website = '杭州市桐庐县公共资源交易网'
    specific_area = '桐庐'
    specific_sele_spider = TongLuSeleSpider
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []




