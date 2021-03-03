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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'dajiangdong.json')


@singleton
class DaJiangDongSeleSpider(SeleCommander):
    name = 'dajiangdong'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'

    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        try:
            total_page = driver.find_element_by_xpath(self.xp.total_page).text
            total_page = re.findall(r'/ (\d+) 页',total_page,re.I)[0]
            int(total_page)
        except Exception as e:
            total_page = '1'
            print('get total error',e)
            print(driver.current_url)
        #print('total_page',total_page)
        #self.refined_totalpage = 2
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
            if 'ProArticle' in driver.current_url:
                an_title = element.find_element_by_xpath(self.xp.an_title).get_attribute('title')
            if 'web_news' in driver.current_url:
                element_title = element.find_element_by_xpath(self.xp.an_title).text
                an_title = re.sub(r'\s+',r'\s',element_title)
        except Exception as e:
            print('get an title error',e)
            print(driver.current_url)
        if not an_title:
            an_title = 'NONE'
        return an_title

    def get_on_date(self,element,driver):
        on_date = 'NONE'
        try:
            if 'ProArticle' in driver.current_url:
                on_date = element.find_element_by_xpath(self.xp.on_date).text
                on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
            if 'web_news' in driver.current_url:
                on_date = element.find_element_by_xpath(self.xp.on_date_web_news).text
                on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
        except Exception as e:
            print('get_on_date error',e)
            print(driver.current_url)
            on_date = element.find_element_by_xpath(self.xp.on_date_web_news).text
            on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
        if not on_date:
            on_date = 'NONE'
        #print('on_date',on_date)
        return on_date

    def get_an_sub(self,an_sub,element,driver):
        return an_sub

    def get_an_county(self,element,driver):
        an_county = 'NONE'
        try:
            if 'ProArticle' in driver.current_url:
                an_county = element.find_element_by_xpath(self.xp.an_county).text
                num_enabled = re.findall(r'(\d+)',an_county)
                if len(num_enabled):
                    an_county = 'NONE'
        except Exception as e:
            print('an_county error',e)
            print(driver.current_url)
            an_county = 'NONE'
        if not an_county:
            an_county = 'NONE'
        #print('an_county',an_county)
        return an_county

    def get_elem_url(self,element,driver):
        element_url = 'http://xzspj.hzdjd.gov.cn:33898/'
        try:
            element_url = element.find_element_by_xpath(self.xp.an_url).get_attribute('href')
        except Exception as e:
            print('get element url error',e)
            print(driver.current_url)
        if not element_url:
            element_url = 'http://xzspj.hzdjd.gov.cn:33898/'
        #print('element_url',element_url)
        return element_url


    def click_next_page(self,driver,page):
        try:
            driver.find_element_by_xpath(self.xp.input_value).clear()
            driver.find_element_by_xpath(self.xp.input_value).send_keys('{}'.format(page+1))
            driver.find_element_by_xpath(self.xp.input_value).send_keys(Keys.ENTER)
            time.sleep(7)
        except Exception as e:
            print(driver.current_url)
            driver.find_element_by_xpath(self.xp.next_page).click()
            time.sleep(7)


class DaJiangDongSpider(RedisStaticSpider):
    name = 'dajiangdong'
    start_urls = ['http://www.yhggzy.com.cn/']
    source_url = 'http://www.yhggzy.com.cn/'
    jsonfile = JSONFILE
    source_website = '杭州市大江东产业集聚区公共资源交易网'
    specific_area = '大江东'
    specific_sele_spider = DaJiangDongSeleSpider
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []