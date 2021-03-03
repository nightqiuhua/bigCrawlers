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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'yuhuan_ajax.json')

@singleton
class YuHuan_AjaxSeleSpider(SeleCommander):
    name = 'yuhuan_ajax'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'
        self.source_url ='https://www.yhjyzx.com/'


    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        try:
            total_page = driver.find_element_by_xpath(self.xp.total_page).get_attribute('data-page')
        except Exception as e:
            print('get total_page error',e)
            print(driver.current_url)
            total_page = '1'
        #print('total_page',total_page)
        total_page = self.set_totalpage(total_page)
        return total_page


    def presence_elements(self,driver):
        print('url',driver.current_url)
        if 'num=3' in driver.current_url:
            element = self.xp.column_gp
        else:
            element = self.xp.column
        return element

    def get_elements(self,driver):
        try:
            if 'num=3' in driver.current_url:
                elements = driver.find_elements_by_xpath(self.xp.column_gp)
            else:
                elements = driver.find_elements_by_xpath(self.xp.column)
        except Exception as e:
            print('get_elements error',e)
            print(driver.current_url)
            elements = []
        return elements

    def get_an_title(self,element,driver):
        an_title = 'NONE'
        try:
            if 'num=3' in driver.current_url:
                an_title = element.find_element_by_xpath(self.xp.an_title_gp).text
                an_title =re.sub(r'\s+',r'\s',an_title)
            else:
                an_title = element.find_element_by_xpath(self.xp.an_title).text
                an_title =re.sub(r'\s+',r'\s',an_title)
        except Exception as e:
            print('get an title error',e)
            print(driver.current_url)
        if not an_title:
            an_title = 'NONE'
        #print('an_title',an_title)
        return an_title

    def get_on_date(self,element,driver):
        on_date = 'NONE'
        #print('driver_sourece',driver.page_source)
        try:
            if 'num=3' in driver.current_url:
                on_date = element.find_element_by_xpath(self.xp.on_date_gp).get_attribute('data-time')
                on_date = re.findall(r'\d+/\d+/\d+',on_date)[0]
            else:
                on_date = element.find_element_by_xpath(self.xp.on_date).text
                on_date = re.findall(r'\d+/\d+/\d+',on_date)[0]
                on_date = re.sub('/','-',on_date)
        except Exception as e:
            print('get on date error',e)
            print(driver.current_url)
        if not on_date:
            on_date = 'NONE'
        #print('on_date',on_date)
        return on_date

    def get_elem_url(self,element,driver):
        element_url = self.source_url
        try:
            if 'num=3' in driver.current_url:
                element_url = element.find_element_by_xpath(self.xp.an_url_gp).get_attribute('href')
            else:
                element_url = element.find_element_by_xpath(self.xp.an_url).get_attribute('href')
        except Exception as e:
            print('get element url error',e)
            print(driver.current_url)
        if not element_url:
            element_url = self.source_url
        return element_url

    def click_next_page(self,driver,**kwgs):
        try:
            driver.find_element_by_link_text(self.xp.next_page).click()#点击翻页
            time.sleep(7)
        except Exception as e:
            print('click_next_page error',e)
            print(driver.current_url)
            driver.find_element_by_link_text(self.xp.next_page).click()#点击翻页
            time.sleep(7)


class YuHuan_AjaxSpider(RedisStaticSpider):
    name = 'yuhuan_ajax'
    post_suf= '__page_{}'
    start_urls = ['https://www.yhjyzx.com/']
    source_url = 'https://www.yhjyzx.com/'
    jsonfile = JSONFILE
    source_website = '台州市公共资源交易网'
    specific_area = '玉环'
    specific_sele_spider = YuHuan_AjaxSeleSpider
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []


