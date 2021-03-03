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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'yuhang.json')


@singleton
class YuHangSeleSpider(BaseSeleSpider):
    name = 'yuhang'
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
                on_date = element.find_element_by_xpath(self.xp.on_date_web_news).text
                on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
                print(driver.current_url)
        if not on_date:
            on_date = 'NONE'
        #print('on_date',on_date)
        return on_date

    def get_an_sub(self,an_sub,element,driver):
        return an_sub

    def get_an_county(self,element,driver):
        an_county = 'NONE'
        try:
            an_county = element.find_element_by_xpath(self.xp.an_county).text
            an_county = re.sub(r'\s+',r'',an_county)
            if '0' in an_county:
                an_county = 'NONE'
        except Exception as e:
            print('an_county error',e)
            print(driver.current_url)
            an_county = 'NONE'
        return an_county

    def get_elem_url(self,element,driver):
        element_url = 'http://www.yhggzy.com.cn/'
        try:
            element_url = element.find_element_by_xpath(self.xp.an_url).get_attribute('href')
        except Exception as e:
            print('get element url error',e)
            print(driver.current_url)
        if not element_url:
            element_url = 'http://www.yhggzy.com.cn/'
        return element_url

    def click_next_page(self,driver,page):
        try:
            if 'ProArticle' in driver.current_url:
                self.xp.input_value = self.xp.input_value_ProArticle
            if 'web_news' in driver.current_url:
                self.xp.input_value = self.xp.input_value_web_news
            driver.find_element_by_xpath(self.xp.input_value).clear()#点击翻页
            driver.find_element_by_xpath(self.xp.input_value).send_keys('{}'.format(page+1))#点击翻页
            driver.find_element_by_xpath(self.xp.input_value).send_keys(Keys.ENTER)
            time.sleep(7)
        except Exception as e:
            print('click_next_page error',e)
            print(driver.current_url)
            driver.find_element_by_xpath(self.xp.next_page).click()#点击翻页
            time.sleep(7)


@singleton
class YuHangSpider(DIYBaseSpider):
    name = 'yuhang'
    start_urls = ['http://www.yhggzy.com.cn/']
    source_url = 'http://www.yhggzy.com.cn/'
    jsonfile = JSONFILE
    source_website = '杭州市余杭区公共资源交易网'
    specific_area = '余杭'
    specific_sele_spider = YuHangSeleSpider
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []


    def an_on_date_parse(self,response):
        on_date = response.meta['on_date']
        if response.meta['an_type'] == "招标安排":
            on_date = response.xpath('//span[@id="ctl00_ContentPlaceHolder1_DB_PublishStartTime"]//text()').extract()
            on_date = ''.join(on_date)
            try:
                on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
            except Exception as e:
                pass
        #print('on_date',on_date)
        return on_date