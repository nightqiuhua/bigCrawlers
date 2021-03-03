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
from wangban_utils.updatefilterfunc import UpdateFilterClass
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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'zhejiangjt.json')

@singleton
class ZheJiangJTSeleSpider(SeleCommander):
    name = 'zhejiangjt'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'

    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        try:
            total_page = driver.find_element_by_link_text(self.xp.total_page).get_attribute('onclick')
            total_page = re.findall(r'\d+',total_page)[0]
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
            on_date = element.find_element_by_xpath(self.xp.on_date).text
            on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
        except Exception as e:
            print('get_on_date error',e)
            print(driver.current_url)
        #print('on_date',on_date)
        return on_date


    def get_elem_url(self,element,driver):
        element_url = 'http://jtyst.zj.gov.cn/'
        try:
            element_url = element.find_element_by_xpath(self.xp.an_url).get_attribute('href')
        except Exception as e:
            print('get element url error',e)
            print(driver.current_url)
        #print('element_url',element_url)
        return element_url

    def get_an_county(self,element,driver):
        an_county = '省本级'
        return an_county

    def click_next_page(self,driver,page):
        try:
            driver.find_element_by_link_text(self.xp.next_page).click()
            time.sleep(7)
        except Exception as e:
            print(driver.current_url)
            print('click_next_page error',e)
            print('page',page)


class ZheJiangJTSpider(RedisStaticSpider):
    name = 'zhejiangjt'
    start_urls = ['http://jtyst.zj.gov.cn/']
    source_url = 'http://jtyst.zj.gov.cn/'
    jsonfile = JSONFILE
    source_website = '浙江交通'
    specific_area = '浙江省'
    #specific_sele_spider = XiaoShanSeleSpider
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []

