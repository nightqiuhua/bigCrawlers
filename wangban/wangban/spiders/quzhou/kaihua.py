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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'kaihua.json')

@singleton
class KaiHuaSeleSpider(BaseSeleSpider):
    name = 'kaihua'
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
        #print('total_page',total_page)
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
            on_date = element.find_element_by_xpath(self.xp.on_date).get_attribute('href')
            on_date = re.findall(r'\d{4}/\d{1,2}/\d{1,2}',on_date)[0]
            on_date = re.sub(r'/','-',on_date)
            print('on_date 1',on_date)
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
            driver.find_element_by_xpath(self.xp.input_value).send_keys(Keys.ENTER)
            time.sleep(7)
        except Exception as e:
            print('click_next_page error',e)
            print(driver.current_url)
            driver.find_element_by_xpath(self.xp.next_page).click()
            time.sleep(7)

@singleton
class KaiHuaSpider(DIYBaseSpider):
    name = 'kaihua'
    post_suf= '__page_{}'
    start_urls = ['http://www.kaihua.gov.cn/']
    source_url = 'http://www.kaihua.gov.cn/'
    jsonfile = JSONFILE
    source_website = '开化县人民政府'
    specific_area = '开化县'
    specific_sele_spider = KaiHuaSeleSpider
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []


