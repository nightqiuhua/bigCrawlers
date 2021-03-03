# -*- coding: utf-8 -*-
#import __init__
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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'zhejiangzfcg.json')

@singleton
class ZheJiangZFCGSeleSpider(BaseSeleSpider):
    name = 'zhejiangzfcg'

    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'
        self.selecontent_enabled =True
        self.source_website = '浙江政府采购网'
        self.specific_area = '浙江'


    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        total_page = self.set_totalpage(2)
        return total_page


    def column_elements(self,driver,link_dict,total_page=1):
        #print('column_elements')
        #知道总页数，就能够确定需要点击的次数
        an_sub_origal = link_dict['an_sub']
        column_url = link_dict['an_sub_url']
        elements_list = []
        for i in range(1,int(total_page)+1):
            #print('total_page',total_page,'crawling page',i,'url',driver.current_url)
            #if (i%30) == 0:
            #    driver.delete_all_cookies()
            #    time.sleep(300)
            try:
                self.waiting_method(driver)
            except Exception as e:
                print('no element error',e)
                driver.get(column_url)
                time.sleep(4)
                self.click_next_page(driver,page=(i-1))
                print('page',i)
                #break
            an_refer_url = column_url + self.post_suf.format(i)

            driver.find_element_by_xpath('//select[@id="changePageSize"]').click()
            time.sleep(0.5)
            driver.find_element_by_xpath('//select[@id="changePageSize"]//option[@value="100"]').click()
            time.sleep(1)

            try:
                #获区目录栏中的每个urls信息
                elements = self.get_elements(driver)
                for element_value_dict in self.get_element_dict(elements,driver,link_dict['an_sub'],an_sub_origal,an_refer_url,total_page):
                    elements_list.append(element_value_dict)
                try:
                    self.click_next_page(driver,page=i)
                except Exception as e:
                    driver.get(column_url)
                    time.sleep(4)
                    self.click_next_page(driver,page=(i-1))
                while self.alert_accept(driver) == True:
                    self.alert_accept(driver)
            except Exception as e:
                print('column_elements error_reason=',e)
                print('url=',driver.current_url)
                #将程序中出现错误的公告的url存入loss_urls列表中
                #self.loss_urls.append(an_sub)
                continue
        return elements_list

    def get_an_title(self,element,driver):
        an_title = 'NONE'
        try:
            an_title = element.find_element_by_xpath(self.xp.an_title).text
        except Exception as e:
            print('get an title error',e)
            print(driver.current_url)
        #print(an_title)
        return an_title

    def get_on_date(self,element,driver):
        on_date = 'NONE'
        try:
            on_date = element.find_element_by_xpath(self.xp.on_date).text
            on_date = re.findall(r'(\d+-\d+-\d+)',on_date)[0]
        except Exception as e:
            print('get on date error',e)
            print(driver.current_url)
        #print(on_date)
        return on_date


    def get_elem_url(self,element,driver):
        element_url = 'http://www.zjzfcg.gov.cn/'
        try:
            element_url = element.find_element_by_xpath(self.xp.an_url).get_attribute('href')
        except Exception as e:
            print('get element url error',e)
            print(driver.current_url)
        #print(element_url)
        return element_url

    def get_an_sub(self,an_sub,element,driver):
        an_sub = ''
        try:
            an_sub = element.find_element_by_xpath(self.xp.an_sub).text
        except Exception as e:
            print('get element url error',e)
            print(driver.current_url)
        return an_sub

    def get_an_county(self,element,driver):
        an_county = 'NONE'
        try:
            an_county = element.find_element_by_xpath(self.xp.an_county).text
        except Exception as e:
            print('get element url error',e)
            print(driver.current_url)
        #print(an_county)
        return an_county



    def click_next_page(self,driver,page):
        try:
            driver.find_element_by_xpath('//div[@class="paginationjs-go-input"]/input').clear()
            driver.find_element_by_xpath('//div[@class="paginationjs-go-input"]/input').send_keys('{}'.format(page+1))#点击翻页
            driver.find_element_by_xpath('//div[@class="paginationjs-go-button"]/input').click()
            time.sleep(7)
        except Exception as e:
            print('click next_page error',e)
            print(driver.current_url)


    def county_modify(self,item):
        item['an_county'] = item['an_county'].replace('[','').replace(']','').replace(item['an_sub'],'').replace('·','')
        return item['an_county']



    def get_content(self,driver):
        driver.switch_to_frame("detail_frame")
        response = driver.find_element_by_xpath('//div[@id="iframe_box"]').get_attribute('innerHTML')
        driver.switch_to.default_content()
        return response


@singleton
class ZheJiangZFCGSpider(DIYBaseSpider):
    name = 'zhejiangzfcg'
    def parse(self,response):
        pass