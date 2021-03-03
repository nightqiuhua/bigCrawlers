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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'chunan.json')


@singleton
class ChunAnSeleSpider(BaseSeleSpider):
    name = 'chunan'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'
        self.source_url = 'http://www.cajyzx.org.cn:8080/'


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
            on_date =  re.findall(r'\d+-\d+-\d+',on_date)[0]
        except Exception as e:
            print('get on date error',e)
            print(driver.current_url)
        if not on_date:
            on_date = 'NONE'
        return on_date

    def click_next_page(self,driver,page):
        try:
            driver.find_element_by_xpath('//img[@src="/chunanweb/images/page/nextn.gif"]').click()#点击翻页
            time.sleep(2)
        except Exception as e:
            driver.find_element_by_xpath('//img[@src="/chunanweb/images/page/nextn.gif"]').click()#点击翻页
            time.sleep(2)


@singleton
class ChunAnSpider(DIYBaseSpider):
    name = 'chunan'
    post_suf= '__page_{}'
    start_urls = ['http://www.cajyzx.org.cn:8080/']
    jsonfile = JSONFILE
    source_website = '杭州市淳安县公共资源交易网'
    specific_area = '淳安县'
    specific_sele_spider = ChunAnSeleSpider
    source_url = 'http://www.cajyzx.org.cn:8080/'
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []