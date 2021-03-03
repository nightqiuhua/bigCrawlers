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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'xiaoshan.json')

@singleton
class XiaoShanSeleSpider(BaseSeleSpider):
    name = 'xiaoshan'
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
            if 'Bulletin' in driver.current_url:
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
            if 'Bulletin' in driver.current_url:
                on_date = element.find_element_by_xpath(self.xp.on_date).text
                on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
            if 'web_news' in driver.current_url:
                on_date = element.find_element_by_xpath(self.xp.on_date_web_news).text
                on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
        except Exception as e:
            print('get_on_date error',e)
            print(driver.current_url)
        if not on_date:
            on_date = 'NONE'
        #print('on_date',on_date)
        return on_date

    def get_an_sub(self,an_sub,element,driver):
        an_sub = 'NONE'
        try:
            an_sub = element.find_element_by_xpath(self.xp.an_sub).text
        except Exception as e:
            print('an_sub error',e)
            print(driver.current_url)
        if not an_sub:
            an_sub = 'NONE'
        #print('an_sub',an_sub)
        return an_sub


    def get_elem_url(self,element,driver):
        element_url = 'http://www.xszbjyw.com/'
        try:
            if 'Bulletin' in driver.current_url:
                element_url = element.find_element_by_xpath(self.xp.an_url).get_attribute('href')
            if 'web_news' in driver.current_url:
                original_value = element.find_element_by_xpath(self.xp.an_url).get_attribute('onclick')
                news_bigclass = original_value.split('\'')[1]
                news_id = original_value.split('\'')[3]
                element_url = 'http://www.xszbjyw.com/web_news/WebFromList.aspx?' + 'news_bigclass='+news_bigclass+'&news_id='+news_id
        except Exception as e:
            print('get element url error',e)
            print(driver.current_url)
            an_sub = 'NONE'
        if not element_url:
            element_url = 'http://www.xszbjyw.com/'
        #print('element_url',element_url)
        return element_url

    def click_next_page(self,driver,page):
        try:
            if 'web_news' in driver.current_url:
                driver.find_element_by_xpath(self.xp.input_value_web_news).clear()#点击翻页
                driver.find_element_by_xpath(self.xp.input_value_web_news).send_keys('{}'.format(page+1))#点击翻页
                driver.find_element_by_xpath(self.xp.input_submit_web_news).click()
            if 'Bulletin' in driver.current_url:
                driver.find_element_by_xpath(self.xp.input_value).clear()#点击翻页
                driver.find_element_by_xpath(self.xp.input_value).send_keys('{}'.format(page+1))#点击翻页
                driver.find_element_by_xpath(self.xp.input_submit).click()
            time.sleep(7)
        except Exception as e:
            print(driver.current_url)
            print('click_next_page error',e)
            print('page',page)

@singleton
class XiaoShanSpider(DIYBaseSpider):
    name = 'xiaoshan'
    start_urls = ['http://www.xszbjyw.com/']
    source_url = 'http://www.xszbjyw.com/'
    jsonfile = JSONFILE
    source_website = '杭州市萧山区公共资源交易网'
    specific_area = '萧山区'
    specific_sele_spider = XiaoShanSeleSpider
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []
