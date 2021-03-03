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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'ninghai_ajax.json')

@singleton
class NingHai_AjaxSeleSpider(BaseSeleSpider):
    name = 'ninghai_ajax'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'
        self.source_url ='http://www.nhztb.gov.cn:8030/'


    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        try:
            total_page = driver.find_element_by_xpath(self.xp.total_page).get_attribute('data-page')
        except Exception as e:
            total_page = '1'
            print('get total error',e)
            print(driver.current_url)
        #print('total_page',total_page)
        total_page = self.set_totalpage(total_page)
        return total_page


    def presence_elements(self,driver):
        #print('url',driver.current_url)
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
            elements = []
            print(driver.current_url)
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

    def click_next_page(self,driver,page):
        try:
            driver.find_element_by_xpath(self.xp.input_page).clear()#点击翻页
            driver.find_element_by_xpath(self.xp.input_page).send_keys('{}'.format(page+1))#点击翻页
            driver.find_element_by_xpath(self.xp.input_button).click()
            time.sleep(4)
        except Exception as e:
            driver.find_element_by_link_text(self.xp.next_page).click()#点击翻页
            time.sleep(4)

@singleton
class NingHai_AjaxSpider(DIYBaseSpider):
    name = 'ninghai_ajax'
    post_suf= '__page_{}'
    start_urls = ['http://www.nhztb.gov.cn:8030/']
    source_url = 'http://www.nhztb.gov.cn:8030/'
    jsonfile = JSONFILE
    source_website = '宁波市宁海县公共资源交易网'
    specific_area = '宁海县'
    specific_sele_spider = NingHai_AjaxSeleSpider
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []
