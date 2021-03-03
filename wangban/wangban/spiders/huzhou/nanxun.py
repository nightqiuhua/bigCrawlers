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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'nanxun.json')

@singleton
class NanXunSeleSpider(BaseSeleSpider):
    name = 'nanxun'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'
        self.source_url ='http://ggzy.nanxun.gov.cn'

    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        try:
            total_page = re.findall(r'"pageTotal":(\d+),',driver.page_source)[0]
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
            on_date = re.sub('/','-',on_date)
            on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
        except Exception as e:
            print('get on date error',e)
            print(driver.current_url)
        if not on_date:
            on_date = 'NONE'
        #print('on_date',on_date)
        return on_date


    def get_elem_url(self,elem,driver):
        element_url = self.source_url
        try:
            element_url = elem.find_element_by_xpath(self.xp.an_url).get_attribute('href')
        except Exception as e:
            print('get elem url error',e)
            print(driver.current_url)
        return element_url

    def click_next_page(self,driver,page):
        try:
            driver.find_element_by_xpath(self.xp.input_value).clear()
            driver.find_element_by_xpath(self.xp.input_value).send_keys('{}'.format(page+1))
            driver.find_element_by_link_text(self.xp.next_page).click()
            time.sleep(4)
        except Exception as e:
            print(driver.current_url)
            time.sleep(4)


@singleton
class NanXunSpider(DIYBaseSpider):
    name = 'nanxun'
    post_suf= '__page_{}'
    start_urls = ['http://ggzy.nanxun.gov.cn']
    source_url = 'http://ggzy.nanxun.gov.cn'
    jsonfile = JSONFILE
    source_website = '湖州市南浔区公共资源交易网'
    specific_area = '南浔'
    specific_sele_spider = NanXunSeleSpider
    links_tree = {}
    loss_urls = {}
    
    column_urls_pool = []
