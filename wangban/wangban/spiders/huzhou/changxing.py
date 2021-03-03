
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
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'changxing.json')

@singleton
class ChangXingSeleSpider(BaseSeleSpider):
    name = 'changxing'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'
        self.source_url ='http://ggzy.zjcx.gov.cn:8081/cxweb/'


    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        try:
            total_page = driver.find_element_by_xpath(self.xp.total_page).text
            total_page = int(total_page)
        except Exception as e:
            total_page = '1'
            print('get total error',e)
            print(driver.current_url)
        #print('total_page',total_page)
        total_page = self.set_totalpage(total_page)
        return total_page

    def click_next_page(self,driver,page):
        try:
            driver.find_element_by_xpath('//img[@src="/cxweb/images/page/nextn.gif"]').click()#点击翻页
            time.sleep(4)
        except Exception as e:
            driver.find_element_by_xpath('//img[@src="/cxweb/images/page/nextn.gif"]').click()#点击翻页
            time.sleep(4)
        
@singleton
class ChangXingSpider(DIYBaseSpider):
    name = 'changxing'
    start_urls = ['http://ggzy.zjcx.gov.cn:8081/cxweb/']
    source_url = 'http://ggzy.zjcx.gov.cn:8081/cxweb/'
    jsonfile = JSONFILE
    source_website = '湖州市长兴县公共资源交易网'
    specific_area = '长兴'
    specific_sele_spider = ChangXingSeleSpider
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []


