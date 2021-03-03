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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'longyou_ajax.json')

@singleton
class LongYou_AjaxSeleSpider(SeleCommander):
    name = 'longyou_ajax'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'
        self.source_url ='http://www.kecheng.gov.cn/'


    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        try:
            total_page = driver.find_element_by_xpath(self.xp.total_page).text
        except Exception as e:
            total_page = '1'
            print('get total error',e)
            print(driver.current_url)
        print('total_page',total_page)
        total_page = self.set_totalpage(total_page)
        return total_page

    def get_an_title(self,element,driver):
        an_title = 'NONE'
        try:
            an_title = element.find_element_by_xpath(self.xp.an_title).text
            an_title = re.sub(r'\s+',r'\s',an_title)
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
            if 'Launch' in driver.current_url:
                on_date_xp = self.xp.on_date
            if 'Result' in driver.current_url:
                on_date_xp = self.xp.on_date_result
            on_date = element.find_element_by_xpath(on_date_xp).text
            on_date = re.findall(r'\d+-\d+-\d+',on_date)[0]
        except Exception as e:
            print('get on date error',e)
            print(driver.current_url)
            on_date = 'NONE'
        if not on_date:
            on_date = 'NONE'
        #print('on_date',on_date)
        return on_date

    def get_elem_url(self,element,driver):
        element_url = self.source_url
        try:
            element_url = element.find_element_by_xpath(self.xp.an_url).get_attribute('href')
        except Exception as e:
            print('get element url error',e)
            print(driver.current_url)
        if not element_url:
            element_url = self.source_url
        #print('element_url',element_url)
        return element_url

    def click_next_page(self,driver,page):
        try:
            driver.find_element_by_xpath(self.xp.input_value).clear()
            driver.find_element_by_xpath(self.xp.input_value).send_keys('{}'.format(page+1))
            driver.find_element_by_xpath(self.xp.input_button).click()
            time.sleep(10)
        except Exception as e:
            print('click_next_page error',e)
            print(driver.current_url)
            driver.find_element_by_xpath(self.xp.next_page).click()
            time.sleep(10)


class LongYouAjaxSpider(RedisStaticSpider):
    name = 'longyou_ajax'
    post_suf= '__page_{}'
    start_urls = ['http://www.kaihua.gov.cn/']
    source_url = 'http://www.kaihua.gov.cn/'
    jsonfile = JSONFILE
    source_website = '龙游公共资源交易中心'
    specific_area = '龙游'
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []

