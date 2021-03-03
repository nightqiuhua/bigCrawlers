
from spiders.selecrawlers.selecommander import SeleCommander
from spiders.redis_spider import RedisStaticSpider
import os
from wangban_utils.redis_util import get_redis_conn
from collections import defaultdict
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
from scrapy.utils.project import get_project_settings
from selenium.webdriver.common.keys import Keys
from wangban_utils.single_mode import singleton
SETTINGS = get_project_settings()
JSONFILE = os.path.join(SETTINGS['BASE_JSONFILE_PATH'],'changxing.json')

@singleton
class ChangXingSeleSpider(SeleCommander):
    name = 'changxing'
    def __init__(self):
        super().__init__()
        self.post_suf = '__page_{}'
        self.source_url ='http://www.cxztb.gov.cn:8081/'


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
        

class ChangXingSpider(RedisStaticSpider):
    name = 'changxing'
    start_urls = ['http://www.cxztb.gov.cn:8081/cxweb/']
    source_url = 'http://www.cxztb.gov.cn:8081/'
    jsonfile = JSONFILE
    source_website = '湖州市长兴县公共资源交易网'
    specific_area = '长兴'
    specific_sele_spider = ChangXingSeleSpider
    links_tree = {}
    loss_urls = {}
    column_urls_pool = []


