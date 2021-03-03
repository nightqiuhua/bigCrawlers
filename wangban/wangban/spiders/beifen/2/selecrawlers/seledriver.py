import __init__
import time
import json
from selenium import webdriver 
from spiders import all_sele_spider
from wangban_utils.redis_util import get_redis_conn
from scrapy.utils.project import get_project_settings
from selenium.webdriver.chrome.options import Options
from spiders.selecrawlers.selecommander import SeleCommander
SETTINGS = get_project_settings()

class SeleDriver:
    def __init__(self):
        self.chrome_options = Options()
        #self.chrome_options.add_argument('--headless')
        #self.driver = webdriver.Chrome(chrome_options=self.chrome_options,executable_path=SETTINGS['CHROME_PATH'])
        self.driver = webdriver.Chrome(SETTINGS['CHROME_PATH'])
        self.driver.set_window_size(500,500)
        self.redis_conn = get_redis_conn()
        #self.driver = webdriver.Chrome(self.chrome_path)
        self.count = 0

    def webbrowser_open(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print('open webbrowser error',e)

    def webbrowser_execute(self):
        working_spider = SeleCommander()
        while True:
            self.count +=1
            task = self.redis_conn.lpop(SETTINGS['SUB_SELE_TASKS'])
            if not task:
                break
            link_dict = json.loads(task.decode('utf-8').replace("'", "\""))
            try:
                crawlingspider = all_sele_spider[link_dict['name']]()
                working_spider.run(self.driver,link_dict,crawlingspider)
            except Exception as e:
                print('the spider is of error',e)

    def webbrowser_close(self):
        self.driver.quit()

if __name__ == '__main__':
    crawling_spider = SeleDriver()
    crawling_spider.webbrowser_execute()