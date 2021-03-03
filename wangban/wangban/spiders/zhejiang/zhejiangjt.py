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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'zhejiangjt.json')

@singleton
class ZheJiangJTSeleSpider(BaseSeleSpider):
    name = 'zhejiangjt'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'

    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        try:
            total_page = driver.find_element_by_xpath('//span[@class="white_pgBtn white_pgNext"]').text
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
            an_title = element.find_element_by_xpath(self.xp.an_title).text
        except Exception as e:
            print('get an title error',e)
            print(driver.current_url)
        return an_title

    def get_on_date(self,element,driver):
        on_date = 'NONE'
        try:
            on_date =element.find_element_by_xpath('.//a').get_attribute('href')
            on_date = re.findall(r'\d{4}/\d{1,2}/\d{1,2}',on_date)[0]
            on_date = re.sub(r'/','-',on_date)
        except Exception as e:
            print('get_on_date error',e)
            print(driver.current_url)
        return on_date


    def get_elem_url(self,element,driver):
        element_url = 'http://jtyst.zj.gov.cn/'
        try:
            element_url = element.find_element_by_xpath('.//a').get_attribute('href')
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
            driver.find_element_by_xpath('//input[@title="页码"]').clear()
            driver.find_element_by_xpath('//input[@title="页码"]').send_keys('{}'.format(int(page)+1))
            driver.find_element_by_xpath('//input[@title="页码"]').send_keys(Keys.ENTER) 
            time.sleep(4)
        except Exception as e:
            print(driver.current_url)
            print('click_next_page error',e)
            print('page',page)

@singleton
class ZheJiangJTSpider(DIYBaseSpider):
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

    def an_title_parse(self,response):
        an_title =response.meta['an_title']
        try:
            an_title = response.xpath("//h4/text()").extract()[0]
            an_title = re.sub(r'\s+',r'\s',an_title)
        except Exception as e:
            an_title =response.meta['an_title']
        return an_title
