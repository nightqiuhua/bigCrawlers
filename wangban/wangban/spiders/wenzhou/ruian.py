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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'ruian.json')

@singleton
class RuiAnSeleSpider(BaseSeleSpider):
    name = 'ruian'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'
        self.source_url = 'http://www.raztb.com/'


    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        try:
            total_page = driver.find_element_by_xpath(self.xp.total_page).text
            total_page = int(total_page)
        except Exception as e:
            print('get_totalpage error_reason',e)
            print('url',driver.current_url)
            total_page = 1
        #print('total_page',total_page)
        total_page = self.set_totalpage(total_page)
        return total_page



    def get_an_title(self,element,driver):
        an_title = 'NONE'
        try:
            an_title = element.find_element_by_xpath(self.xp.an_title).get_attribute('title')
        except Exception as e:
            print('get an title error',e)
            print('url',driver.current_url)
        if not an_title:
            an_title = 'NONE'
        return an_title

    def get_on_date(self,element,driver):
        on_date = 'NONE'
        try:
            on_date = element.find_element_by_xpath(self.xp.on_date).text
            on_date =  re.findall(r'\d+-\d+-\d+',on_date)[0]
        except Exception as e:
            print('get on date error',e)
            print('url',driver.current_url)
        if not on_date:
            on_date = 'NONE'
        return on_date

    def click_next_page(self,driver,**kwgs):
        try:
            driver.find_element_by_xpath(self.xp.next_page).click()#点击翻页
            time.sleep(7)
        except Exception as e:
            print('click_next_page',e)
            print('url',driver.current_url)
            driver.find_element_by_xpath(self.xp.next_page).click()#点击翻页
            time.sleep(7)


@singleton
class RuiAnSpider(DIYBaseSpider):
    name = 'ruian'
    post_suf= '__page_{}'
    start_urls = ['http://www.raztb.com/']
    jsonfile = JSONFILE
    source_website = '温州市瑞安市公共资源交易网'
    specific_area = '瑞安市'
    specific_sele_spider = RuiAnSeleSpider
    source_url = 'http://www.raztb.com/'
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []
