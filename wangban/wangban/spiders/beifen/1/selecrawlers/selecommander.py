# -*- coding: utf-8 -*-
import os
from selenium import webdriver
import time
from wangban_utils.Json2Xpath import Json2XPath,XPath
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import csv
import re
import time
import json
from wangban_utils.mongo_util import MongodbClass
from wangban_utils.mysql_util import MySqlDBClass
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
from wangban_utils.redis_util import get_redis_conn
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from scrapy.utils.project import get_project_settings
from wangban_utils.logging_util import update_logging
from modify_func import all_modify_func
SETTINGS = get_project_settings()

BASE_JSONFILE_PATH = SETTINGS['BASE_JSONFILE_PATH']

class SeleCrawler:
    def __init__(self,refined_totalpage=2):
        self.loss_urls = []
        self.refined_totalpage = refined_totalpage
        self.redis_conn = get_redis_conn()
        jsonfile = os.path.join(BASE_JSONFILE_PATH,'{}.json'.format(self.name))
        self.xp = Json2XPath(jsonfile).get_xpath()
        self.check_queue = SETTINGS['URLS_CHECK_TASKS']
        self.mongo_conn = MongodbClass()
        self.mysql_conn = MySqlDBClass()
        self.logging_actor = update_logging()
        self.func_moc = all_modify_func[self.name]

    def crawling_column(self,driver,link_dict):
        """抓取an_sub_url下的所有目录页信息
        参数 driver driver类
            link_dict 字典
        return  elements_list 列表 包含an_sub_url下的所有目录页信息
        """
        try:
            driver.get(link_dict['an_sub_url'])
            time.sleep(10)
            service_abled = self.service_able_check(driver)
            self.waiting_method(driver)
            while self.alert_accept(driver) == True:
                self.alert_accept(driver)
        except Exception as e:
            print('crawling_column error',e)
            raise e
        else:
            total_page=self.get_totalpage(driver)
            elements_list = self.column_elements(driver,link_dict,total_page)
        return elements_list



    def column_elements(self,driver,link_dict,total_page=1):
        #print('column_elements')
        #知道总页数，就能够确定需要点击的次数
        an_sub_origal = link_dict['an_sub']
        column_url = link_dict['an_sub_url']
        elements_list = []
        #2
        for i in range(1,int(total_page)+1):
            try:
                self.waiting_method(driver)
            except Exception as e:
                print('no element error',e)
                raise e
                #driver.get(column_url)
                #time.sleep(4)
                #self.click_next_page(driver,page=(i-1))
                #print('page',i)
            an_refer_url = column_url + self.post_suf.format(i)
            elements = self.get_elements(driver)
            for element_value_dict in self.get_element_dict(elements,driver,link_dict['an_sub'],an_sub_origal,an_refer_url,total_page):
                elements_list.append(element_value_dict)
            try:
                self.click_next_page(driver,page=i)
            except Exception as e:
                driver.get(column_url)
                time.sleep(4)
                #self.click_next_page(driver,page=(i-1))
            while self.alert_accept(driver) == True:
                self.alert_accept(driver)
        return elements_list

    def get_an_info(self,driver,content_task):
        an_url_key = content_task['an_url']
        try:
            driver.get(an_url_key)
            time.sleep(5)
        except Exception as e:
            raise e
        else:
            while self.alert_accept(driver) == True:
                self.alert_accept(driver)
            time.sleep(1)
            content_task['_id'] = an_url_key
            content_task['crawling_date'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            content_task['source_website'] = self.source_website
            content_task['website_area'] = self.specific_area
            content_task['specific_area'] = self.county_modify(content_task)
            content_task['project_title'] = content_task['an_title']
            
            an_content = self.get_content(driver)
            try:
                content = self.func_moc(an_content)
            except Exception as e:
                print('func_moc error')
                self.logging_actor.record_error_data(content_task,self.name)
                raise e
            content_task['an_content'] = content
            #print('working info_2')
            success_enabled = self.mongo_conn.insert_into_db(content_task,self.name)
            if success_enabled:
                self.logging_actor.write_data(content_task,self.name)
            try:
                check_data = {"_id":content_task["an_url"],"gettime":content_task["crawling_date"],"touch_time":content_task["crawling_date"]}
                self.mongo_conn.insert_into_db(check_data,'check_collections')
                self.mysql_conn.insert_into_db(content_task,'t_zhaobiao')
            except Exception as e:
                raise e
            self.logging_actor.record_data(content_task,self.name)
            ##print('success_enabled_111',success_enabled)

    def county_modify(self,item):
        return 'NONE'

    def get_content(self,driver):
        content = driver.find_element_by_xpath('//body').get_attribute('innerHTML')#获取网页html
        return content


    def get_element_dict(self,elements,driver,an_sub,an_sub_origal,an_refer_url,total_page):
        #print('get_element_dict')
        for element in elements:
            element_dict = {}
            element_dict['an_url']=self.get_elem_url(element,driver)
            element_dict['an_title'] = self.get_an_title(element,driver)
            element_dict['on_date'] = self.get_on_date(element,driver)
            element_dict['an_sub'] = self.get_an_sub(an_sub,element,driver)
            element_dict['an_sub_origal'] = an_sub_origal
            element_dict['an_refer_url'] = an_refer_url
            element_dict['an_refer_total_page'] = total_page
            element_dict['an_county'] = self.get_an_county(element,driver)
            element_dict['an_ref_page_items'] = len(elements)
            element_dict['type'] ='content'
            yield element_dict

    def waiting_method(self,driver):
        try:
            element = WebDriverWait(driver,15).until(   #until 也属于WebDriverWait,代表一直等待,直到某元素可见，
            #until_not与其相反，判断某个元素直到不存在
            EC.presence_of_element_located((By.XPATH,self.presence_elements(driver)))  #presence_of_element_located主要判断页面元素kw在页面中存在。
            )
        except Exception as e:
            print('waiting_method error',e)
            raise e
        #pass

    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        try:
            total_page = driver.find_element_by_xpath(self.xp.total_page).text
            total_page = re.findall(r'1 / (\d+)',total_page,re.I)[0]
            int(total_page)
        except ValueError:
           total_page = '1'
        total_page = self.set_totalpage(total_page)
        return total_page

    def service_able_check(self,driver):
        return True


    def set_totalpage(self,orignal):
        if int(orignal) > self.refined_totalpage:
            orignal = self.refined_totalpage
        return orignal


    def presence_elements(self,driver):
        return self.xp.column

    def get_elements(self,driver):
        try:
            elements = driver.find_elements_by_xpath(self.xp.column)
        except Exception as e:
            print('get_elements error',e)
            elements = []
        return elements

    def get_an_title(self,element,driver):
        an_title = 'NONE'
        try:
            an_title = element.find_element_by_xpath(self.xp.an_title).get_attribute('title')
        except Exception as e:
            print('get an title error',e)
        if not an_title:
            an_title = 'NONE'
        return an_title

    def get_on_date(self,element,driver):
        on_date = 'NONE'
        try:
            on_date = element.find_element_by_xpath(self.xp.on_date).text
        except Exception as e:
            print('get on date error',e)
        if not on_date:
            on_date = 'NONE'
        return on_date

    def get_an_sub(self,an_sub,element,driver):
        
        return an_sub

    def get_an_county(self,element,driver):
        an_county = 'NONE'
        return an_county

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
            driver.find_element_by_xpath(self.xp.next_page).click()#点击翻页
            time.sleep(7)
        except Exception as e:
            driver.find_element_by_xpath(self.xp.next_page).click()#点击翻页
            time.sleep(7)

#解决警告窗问题
    def alert_accept(self,driver):
        try:
          alert = driver.switch_to_alert()
          print("Aler text:" + alert.text)
          alert.accept()
          print("Alert detected, accept it")
          return True
        except UnexpectedAlertPresentException:
          return False
        except NoAlertPresentException:
          return False

class SeleCommander(SeleCrawler):
    def __init__(self):
        super().__init__()

    def run(self,driver,link_dict):
        pipe = self.redis_conn.pipeline(True)
        try:
            driver.delete_all_cookies()
            #for link_key,link_value in link_dict.items():
            if link_dict['type'] == 'sub':
                sele_func = self.run_sub_work
            if link_dict['type'] == 'column':
                sele_func = self.run_column_work
            if link_dict['type'] == 'content':
                self.run_an_content_work(driver,link_dict)
            else:
                for each_item in sele_func(driver,link_dict):
                    input_value = json.dumps(each_item)
                    pipe.lpush(self.check_queue,input_value)
                pipe.execute()
        except Exception as e:
            print('an error occur',e)
            raise e

    def run_sub_work(self,driver,link_dict):
        for an_info_item in self.spurncrawler(driver,link_dict):
            an_value = {'name':self.name}
            an_value.update(an_info_item)
            yield an_value

    def run_column_work(self,driver,column_task):
        driver.delete_all_cookies()
        #driver,cookies_dict = self.driver_add_cookies(driver)
        try:
            for an_url_key,an_url_column_value in self.spurncrawler(driver,column_task):
                an_url_column_value['type'] = 'content'
                an_url_column_value['name'] = self.name
                yield {an_url_key:an_url_column_value}
        except Exception as e:
            raise e 


    def run_an_content_work(self,driver,content_task):
        try:
            self.get_an_info(driver,content_task)
        except Exception as e:
            raise e
            

    def spurncrawler(self,driver,link_dict):
        an_info_list = self.crawling_column(driver,link_dict)
        for an_info in an_info_list:
            an_info['an_type'] = link_dict['an_type']
            an_info['an_major'] = link_dict['an_major']
            yield an_info