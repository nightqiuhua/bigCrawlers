# -*- coding: utf-8 -*-
import json
from spiders.selecrawlers.selecommander import SeleCommander
from spiders.redis_spider import RedisStaticSpider
from wangban_utils.redis_util import get_redis_conn
from collections import defaultdict
import socket
from datetime import datetime
import os
from items import HangzhouItem
import time
import re
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
from wangban_utils.redis_util import get_redis_conn
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from wangban_utils.Json2Xpath import Json2XPath,XPath
from selenium.webdriver.common.keys import Keys
from scrapy.utils.project import get_project_settings
from wangban_utils.single_mode import singleton
SETTINGS = get_project_settings()
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'longyou.json')

class LongYouSeleSpider(SeleCommander):
    name = 'longyou'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'
        self.source_url ='http://www.lyxztb.com/'

    def run(self,driver,link_dict):
        pipe = self.redis_conn.pipeline(True)
        try:
            driver.delete_all_cookies()
            for link_key,link_value in link_dict.items():
                if link_value['type'] == 'sub':
                    sele_func = self.run_sub_work
                if link_value['type'] == 'column':
                    sele_func = self.run_column_work
                if link_value['type'] == 'content':
                    self.run_an_content_work(driver,link_dict)
                    continue
                for each_item in sele_func(driver,link_dict):
                    input_value = json.dumps(each_item)
                    pipe.rpush(self.check_queue,input_value)
                pipe.execute()
        except Exception as e:
            print('an error occur',e)
            raise e

    def run_sub_work(self,driver,link_dict):
        for an_url_key,an_url_sub_value in self.an_sub_item_generator(driver,link_dict):
            an_value = {'name':self.name}
            an_value.update(an_url_sub_value)
            yield {an_url_key:an_value}



    def an_sub_item_generator(self,driver,column_task):
        for sub_url,sub_value in column_task.items():
            total_page = self.get_totalpage(driver,sub_url)
            print('total_page',total_page)
            sub_value['type'] = 'column'
            for page in range(1,int(total_page)+1):
                column_url = self.cre_page_url(sub_url,page)
                print('column_url',column_url)
                yield column_url,sub_value

    def spurncrawler(self,driver,link_dict):
        for column_url,column_url_value in link_dict.items():
            try:
                an_urls_dict = self.crawling_column(driver,column_url,column_url_value["an_sub"])
                for an_url_key,an_url_value in self.an_url_generator(an_urls_dict):
                    an_url_value['an_type'] = column_url_value['an_type']
                    an_url_value['an_major'] = column_url_value['an_major']
                    yield an_url_key,an_url_value
            except Exception as e:
                input_value = json.dumps(link_dict)
                self.redis_conn.rpush(SETTINGS['SUB_SELE_TASKS'],input_value)


    def crawling_column(self,driver,column_url,an_sub):
        an_urls_dict = {}
        an_urls_dict[an_sub] = []
        try:
            driver.get(column_url)
            time.sleep(10)
            self.waiting_method(driver)
            while self.alert_accept(driver) == True:
                self.alert_accept(driver)
        except Exception as e:
            print('crawling_column error',e)
            #self.loss_urls.append(column_url)
            raise e
        else:
            #total_page=self.get_totalpage(driver,column_url)
            elements_list = self.column_elements(driver,column_url,an_sub)
            an_urls_dict[an_sub].extend(elements_list)
            time.sleep(5)
        return an_urls_dict


    def get_totalpage(self,driver,sub_url):
        #获取总页数，没有总页数，设置总页数为1
        try:
            driver.get(sub_url)
            time.sleep(3)
            total_page = driver.find_element_by_link_text(self.xp.total_page).get_attribute('href')
            total_page = re.findall(r'page=(\d+)',total_page)[0]
            print('total_page',total_page)
        except Exception as e:
            print('get_totalpage error_reason',e)
            print('response_url',driver.current_url)
            total_page = 1
        print('total_page is ',total_page)
        total_page = self.set_totalpage(total_page)
        #print('source_code',driver.find_element_by_xpath("//*").get_attribute("outerHTML"))
        return total_page

    def cre_page_url(self,f_p_url,page):
        if page == 0:
            page = 1
        page_url = f_p_url + '&page={}'.format(page)
        #print('cre_page_url',page_url)
        return page_url

    def column_elements(self,driver,column_url,an_sub,total_page=1):
        #知道总页数，就能够确定需要点击的次数
        elements_list = []
        an_sub_origal = an_sub
        an_refer_url = column_url
        try:
            #获区目录栏中的每个urls信息
            elements = self.get_elements(driver)
            for element_value_dict in self.get_element_dict(elements,driver,an_sub,an_sub_origal,an_refer_url,total_page):
                elements_list.append(element_value_dict)
        except Exception as e:
            print('column_elements error_reason=',e)
            print('url=',driver.current_url)
        return elements_list


    def get_an_title(self,element,driver):
        an_title = 'NONE'
        try:
            an_title = element.find_element_by_xpath(self.xp.an_title).text
            an_title = re.sub('\s+','',an_title)
        except Exception as e:
            print('get an title error',e)
        if not an_title:
            an_title = 'NONE'
        return an_title

    def get_on_date(self,element,driver):
        on_date = 'NONE'
        try:
            on_date = element.find_element_by_xpath('.//*').get_attribute("outerHTML")
            on_date = re.findall(r'\d+-\d+-\d+',on_date)[0]
            print('on_date',on_date)
        except Exception as e:
            print('get on date error',e)
        if not on_date:
            on_date = 'NONE'
        return on_date


    def get_elem_url(self,elem,driver):
        element_url = self.source_url
        try:
            element_url = elem.find_element_by_xpath(self.xp.an_url).get_attribute('href')
        except Exception as e:
            print('get elem url error',e)
        if not element_url:
            element_url = self.source_url
        return element_url

    def click_next_page(self,driver,**kwgs):
        try:
            driver.find_element_by_link_text(self.xp.next_page).click()#点击翻页
            time.sleep(15)
        except Exception as e:
            driver.find_element_by_link_text(self.xp.next_page).click()#点击翻页
            time.sleep(15)


class LongYouSpider(RedisStaticSpider):
    name = 'longyou'

    def parse(self,response):
        pass







