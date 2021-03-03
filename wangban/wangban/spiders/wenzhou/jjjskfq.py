# -*- coding: utf-8 -*-

import os
import time
import re
from scrapy.utils.project import get_project_settings
from spiders.selecrawlers.baseselespider import BaseSeleSpider
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from wangban_utils.single_mode import singleton
from spiders.basemodel import DIYBaseSpider
SETTINGS = get_project_settings()
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'jjjskfq.json')

@singleton
class JJJSKFQSeleSpider(BaseSeleSpider):
    name = 'jjjskfq'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'
        self.source_url ='http://new.wl.gov.cn/'

    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        try:
            total_page = driver.find_element_by_xpath(self.xp.total_page).text
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
            an_title = re.sub(r'\s+','',an_title)
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
            time.sleep(4)
        except Exception as e:
            driver.find_element_by_xpath(self.xp.next_page).click()
            time.sleep(4)

        
@singleton
class JJJSKFQSpider(DIYBaseSpider):
    name = 'jjjskfq'
    start_urls = ['http://www.wetdz.gov.cn/']
    source_website = '温州市经济技术开发区人民政府网'
    specific_area = '温州市经济技术开发区'
    source_url = 'http://www.wetdz.gov.cn/'
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []

