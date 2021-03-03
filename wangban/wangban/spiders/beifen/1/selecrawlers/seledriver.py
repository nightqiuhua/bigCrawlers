import __init__
from selenium import webdriver 
from spiders import all_sele_spider
from wangban_utils.redis_util import get_redis_conn
import json
from scrapy.utils.project import get_project_settings
import time
from selenium.webdriver.chrome.options import Options
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
        for link_dict in self.webbrowser_get_tasks():
            try:
                working_spider = all_sele_spider[link_dict['name']]
                working_spider.run(self.driver,link_dict)
            except Exception as e:
                print('the spider is of error',e)

    def webbrowser_get_tasks(self):
        while True:
            self.count +=1
            time.sleep(1)
            #print('count',self.count)
            #if (self.count % 30) == 0:
            #    time.sleep(300)
            task = self.redis_conn.lpop(SETTINGS['SUB_SELE_TASKS'])
            if not task:
                break
            task_link = json.loads(task.decode('utf-8').replace("'", "\""))
            task_tmp = json.dumps(task_link)
            #self.redis_conn.rpush('wangban:longyou:tmp',task_tmp)
            yield task_link

    def webbrowser_close(self):
        self.driver.quit()

if __name__ == '__main__':
    crawling_spider = SeleDriver()
    crawling_spider.webbrowser_execute()