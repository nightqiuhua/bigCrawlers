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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'xihuqu.json')


@singleton
class XiHuQuSeleSpider(BaseSeleSpider):
    name = 'xihuqu'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'

    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        try:
            total_page = driver.find_element_by_xpath(self.xp.total_page).text
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
        except Exception as e:
            print('get_on_date error',e)
            print(driver.current_url)
        if not on_date:
            on_date = 'NONE'
        #print('on_date',on_date)
        return on_date



    def get_elem_url(self,element,driver):
        element_url = 'http://www.hzxh.gov.cn/'
        try:
            element_url = element.find_element_by_xpath(self.xp.an_url).get_attribute('href')
        except Exception as e:
            print('get element url error',e)
            print(driver.current_url)
        if not element_url:
            element_url = 'http://www.hzxh.gov.cn/'
        #print('element_url',element_url)
        return element_url


    def click_next_page(self,driver,page):
        try:
            driver.find_element_by_xpath('//input[@class="default_pgCurrentPage"]').clear()#点击翻页
            driver.find_element_by_xpath('//input[@class="default_pgCurrentPage"]').send_keys('{}'.format(page+1))#点击翻页
            driver.find_element_by_xpath('//input[@class="default_pgCurrentPage"]').send_keys(Keys.ENTER) #点击翻页
            time.sleep(5)
        except Exception as e:
            print('click next_page error',e)
            print(driver.current_url)
            driver.find_element_by_link_text(self.xp.next_page).click()#点击翻页
            time.sleep(5)


@singleton
class XiHuQuSpider(DIYBaseSpider):
    name = 'xihuqu'
    start_urls = ['http://www.hzxh.gov.cn/']
    source_url = 'http://www.hzxh.gov.cn/'
    jsonfile = JSONFILE
    source_website = '杭州市西湖区公共资源交易网'
    specific_area = '西湖区'
    specific_sele_spider = XiHuQuSeleSpider
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []
