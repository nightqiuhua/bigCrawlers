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
SETTINGS = get_project_settings()
BASE_JSONFILE_PATH = SETTINGS['BASE_JSONFILE_PATH']
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'gongshu.json')

@singleton
class GongShuSeleSpider(BaseSeleSpider):
    name = 'gongshu'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'
        self.selecontent_enabled =True
        self.source_website = '杭州市拱墅区公共资源交易网'
        self.specific_area = '拱墅区'

    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        try:
            total_page = driver.find_element_by_xpath(self.xp.total_page).text
            int(total_page)
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
            on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
        except Exception as e:
            print('get on date error',e)
            print(driver.current_url)
        if not on_date:
            on_date = 'NONE'
        return on_date


    def get_elem_url(self,element,driver):
        element_url = 'http://zwgk.gongshu.gov.cn/public/home/'
        try:
            element_url = element.find_element_by_xpath(self.xp.an_url).get_attribute('href')
        except Exception as e:
            print('get element url error',e)
            print(driver.current_url)
        if not element_url:
            element_url = 'http://zwgk.gongshu.gov.cn/public/home/'
        return element_url

    def get_an_sub(self,an_sub,element,driver):
        an_sub = 'NONE'
        return an_sub

    def click_next_page(self,driver,page):
        try:
            driver.find_element_by_xpath('//input[@id="pagetext"]').clear()#点击翻页
            driver.find_element_by_xpath('//input[@id="pagetext"]').send_keys('{}'.format(page+1))#点击翻页
            driver.find_element_by_xpath('//button[@id="pagebutton"]').click()#点击翻页
            time.sleep(7)
        except Exception as e:
            print('click next_page error',e)
            print(driver.current_url)
            driver.find_element_by_link_text(self.xp.next_page).click()#点击翻页
            time.sleep(7)


@singleton
class GongShuSpider(DIYBaseSpider):
    name = 'gongshu'

    def parse(self,response):
        pass