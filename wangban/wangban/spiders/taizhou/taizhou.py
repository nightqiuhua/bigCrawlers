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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'taizhou.json')

@singleton
class TaiZhouSeleSpider(BaseSeleSpider):
    name = 'taizhou'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'
        self.source_url ='http://www.tzztb.com/'

    def spurncrawler(self,driver,link_dict):
        an_info_list = self.crawling_column(driver,link_dict)
        for an_info in an_info_list:
            an_info['an_type'] = link_dict['an_type']
            an_info['an_major'] = link_dict['an_major']
            an_info['an_county'] = link_dict['an_county']
            yield an_info

    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        try:
            total_page = driver.find_element_by_xpath(self.xp.total_page).text
            total_page = re.findall(r'/(\d+)',total_page)[0]
        except Exception as e:
            total_page = '1'
            print('get total error',e)
            print(driver.current_url)
        #print('total_page',total_page)
        #self.refined_totalpage = 2
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
            an_title = re.sub(r'\s+','',an_title)
        except Exception as e:
            print('get an title error',e)
            print(driver.current_url)
        #print('an_title',an_title)
        return an_title

    def get_on_date(self,element,driver):
        on_date = 'NONE'
        try:
            if 'loca=1&xiaoe=2&type=10' in driver.current_url or 'loca=1&xiaoe=2&type=11' in driver.current_url:
                on_date = element.find_element_by_xpath('./td[3]').text
            else:
                on_date = element.find_element_by_xpath(self.xp.on_date).text
        except Exception as e:
            print('get on date error',e)
            print(driver.current_url)
        #print('on_date',on_date)
        return on_date




    def get_elem_url(self,element,driver):
        element_url = self.source_url
        try:
            element_url = element.find_element_by_xpath(self.xp.an_url).get_attribute('href')
        except Exception as e:
            print('get element url error',e)
            print(driver.current_url)
        #print('element_url',element_url)
        return element_url

    def click_next_page(self,driver,page):
        try:
            driver.find_element_by_xpath('//select').click()
            time.sleep(0.5)
            driver.find_element_by_xpath('//option[@value="{}"]'.format(page)).click()
            time.sleep(7)
        except Exception as e:
            driver.find_element_by_link_text(self.xp.next_page).click()
            time.sleep(7)

@singleton
class TaiZhouSpider(DIYBaseSpider):
    name = 'taizhou'
    start_urls = ['http://www.tzztb.com/']
    source_website = '台州市公共资源交易网'
    specific_area = '台州'
    source_url = 'http://www.tzztb.com/'
    specific_sele_spider = TaiZhouSeleSpider
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []


    def an_title_parse(self,response):
        try:
            an_title = response.xpath('//h1/text()').extract()[0]
            an_title = re.sub(r'\s+',r'\s',an_title)
        except Exception as e:
            an_title =response.meta['an_title']
        return an_title

    def an_content(self,response):
        content = 'NONE'
        try:
            content = self.func_moc(response.text,response.url)
        except Exception as e:
            print(e)
            if response.url != self.source_url:
                return response.xpath('//body').extract()[0]
            else:
                raise e
        return content