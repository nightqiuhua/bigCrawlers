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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'jiande.json')

@singleton
class JianDeSeleSpider(SeleCommander):
    name = 'jiande'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'

    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        try:
            total_page = driver.find_element_by_xpath(self.xp.total_page).text
            total_page = re.findall(r'1 / (\d+)',total_page,re.I)[0]
            int(total_page)
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
        if not an_title:
            an_title = 'NONE'
        return an_title

    def get_on_date(self,element,driver):
        on_date = 'NONE'
        try:
            on_date = element.find_element_by_xpath(self.xp.on_date).text
            on_date = re.findall(r'(\d+-\d+-\d+)',on_date)
            if not len(on_date):
                on_date = element.find_element_by_xpath(self.xp.on_date_2).text
                on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
            else:
                on_date = on_date[0]
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
        element_url = 'http://www.jdggzy.com/index.aspx'
        try:
            element_url = element.find_element_by_xpath(self.xp.an_url).get_attribute('href')
        except Exception as e:
            print('get element url error',e)
            print(driver.current_url)
        if not element_url:
            element_url = 'http://www.jdggzy.com/index.aspx'
        return element_url

    def click_next_page(self,driver,page):
        try:
            driver.find_element_by_xpath(self.xp.input_value_ProArticle).clear()#点击翻页
            driver.find_element_by_xpath(self.xp.input_value_ProArticle).send_keys('{}'.format(page+1))#点击翻页
            driver.find_element_by_xpath(self.xp.input_value_ProArticle).send_keys(Keys.ENTER)
            time.sleep(7)
        except Exception as e:
            print('click_next_page error',e)
            print(driver.current_url)
            driver.find_element_by_xpath(self.xp.next_page).click()
            time.sleep(7)



class JianDeSpider(RedisStaticSpider):
    name = 'jiande'
    start_urls = ['http://www.jdggzy.com/index.aspx']
    source_url = 'http://www.jdggzy.com/index.aspx'
    jsonfile = JSONFILE
    source_website = '杭州市建德区公共资源交易网'
    specific_area = '建德'
    specific_sele_spider = JianDeSeleSpider
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []

    def an_on_date_parse(self,response):
        an_on_date = response.meta['on_date']
        try:
            an_on_date = response.xpath('//span[@class="pubTime"]/text()').extract()[0]
            an_on_date = an_on_date.replace('/','-')
            an_on_date = re.findall(r'\d+-\d+-\d+',an_on_date)[0]
        except Exception as e:
            print('an_on_date_parse error',e)
            an_on_date = response.meta['on_date']
        return an_on_date

    def an_title_parse(self,response):
        an_title = response.meta['an_title']
        try:
            decide_element_1 = response.xpath('//span[@id="ctl00_ContentPlaceHolder1_DB_TenderName"]/text()').extract()
            decide_element_2 = response.xpath('//span[@id="ctl00_ContentPlaceHolder1_DB_Title"]/text()').extract()
            if not decide_element_1:
                answer_element = decide_element_2
            else:
                answer_element = decide_element_1
            if response.meta['an_title'] == 'NONE':
                an_title = answer_element[0]
                an_title = re.sub(r'\s+',r'\s',an_title)
        except Exception as e:
            an_title =response.meta['an_title']
        return an_title


