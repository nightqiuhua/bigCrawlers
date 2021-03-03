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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'jianggan.json')

@singleton
class JiangGanSeleSpider(SeleCommander):
    name = 'jianggan'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'

    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        try:
            if 'col1365636' in driver.current_url:
                total_page = driver.find_element_by_xpath(self.xp.total_page_zab).text
                total_page = re.findall(r'(\d+)页',total_page)[0]
            else:
                total_page = driver.find_element_by_xpath(self.xp.total_page_zb).text
        except Exception as e:
            total_page = '1'
            print('get total error',e)
            print(driver.current_url)
        #print('total_page',total_page)
        total_page = self.set_totalpage(total_page)
        return total_page


    def presence_elements(self,driver):
        if 'col1365636' in driver.current_url:
            return self.xp.column_zab
        else:
            return self.xp.column_zb
        

    def get_elements(self,driver):
        try:
            if 'col1365636' in driver.current_url:
                elements = driver.find_elements_by_xpath(self.xp.column_zab)
            else:
                elements = driver.find_elements_by_xpath(self.xp.column_zb)
        except Exception as e:
            print('get_elements error',e)
            print(driver.current_url)
            elements = []
        return elements

    def get_an_title(self,element,driver):
        an_title = 'NONE'
        try:
            if 'col1365636' in driver.current_url:
                an_title = element.find_element_by_xpath(self.xp.an_title_zab).text
            else:
                an_title = element.find_element_by_xpath(self.xp.an_title_zb).text
            an_title = re.sub(r'\s+','',an_title)
        except Exception as e:
            print('get an title error',e)
            print(driver.current_url)
            an_title = 'NONE'
        return an_title

    def get_on_date(self,element,driver):
        on_date = 'NONE'
        try:
            if 'col1365636' in driver.current_url:
                on_date = element.find_element_by_xpath(self.xp.on_date_zab).get_attribute('href')
            else:
                on_date = element.find_element_by_xpath(self.xp.on_date_zb).get_attribute('href')
            on_date = re.findall(r'\d+/\d+/\d+',on_date)[0]
            on_date = re.sub('/','-',on_date)
        except Exception as e:
            print('get on date error',e)
            print(driver.current_url)
            on_date = 'NONE'
        return on_date

    def get_elem_url(self,element,driver):
        element_url = 'http://www.jianggan.gov.cn/'
        try:
            if 'col1365636' in driver.current_url:
                element_url = element.find_element_by_xpath(self.xp.an_url_zab).get_attribute('href')
            else:
                element_url = element.find_element_by_xpath(self.xp.an_url_zb).get_attribute('href')
        except Exception as e:
            print('get element url error',e)
            print(driver.current_url)
            element_url = 'http://www.jianggan.gov.cn/'
        return element_url

    def click_next_page(self,driver,page):
        try:
            if 'col1365636' in driver.current_url:
                driver.find_element_by_xpath('//select').click()
                time.sleep(0.5)
                driver.find_element_by_xpath('//option[@value="{}"]'.format((page-1)*15)).click()
                time.sleep(7)
            else:
                driver.find_element_by_xpath(self.xp.input_page).clear()#点击翻页
                driver.find_element_by_xpath(self.xp.input_page).send_keys('{}'.format(page+1))
                driver.find_element_by_xpath(self.xp.input_page).send_keys(Keys.ENTER)
            time.sleep(7)
        except Exception as e:
            print('click next page error',e)
            print(driver.current_url)
            time.sleep(7)


class JiangGanSpider(RedisStaticSpider):
    name = 'jianggan'
    start_urls = ['http://www.jianggan.gov.cn/']
    source_url = 'http://www.jianggan.gov.cn/'
    jsonfile = JSONFILE
    source_website = '杭州市江干区公共资源交易网'
    specific_area = '江干区'
    specific_sele_spider = JiangGanSeleSpider
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []
