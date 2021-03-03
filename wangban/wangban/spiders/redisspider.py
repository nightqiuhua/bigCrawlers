from scrapy import signals
from scrapy.exceptions import DontCloseSpider
from wangban_utils.redis_util import get_redis_conn
from scrapy.spiders import Spider
from items import HangzhouItem
import socket
from datetime import datetime
import os
from urllib.parse import urljoin
import json
import time
from wangban_utils.mongo_mysql_util import MongoDB_To_MySQL
from modify_func import all_modify_func
from wangban_utils.mongo_util import MongodbClass
from scrapy.utils.project import get_project_settings
from . import workers
SETTINGS = get_project_settings()


class RedisSpider(Spider):
    name = 'redisspider'

    def __init__(self):
        super().__init__()
        
        self.redis_conn = get_redis_conn()
        #self.to_mysql = MongoDB_To_MySQL(self.name)
        self.redis_batch_size = 100
        self.work_queue = SETTINGS['URLS_WORK_TASKS']
        self.check_queue = SETTINGS['URLS_CHECK_TASKS']
        #self.sche_updator = UpdateFilterClass(self.name)

        self.pre_suf = None
        self.workers = dict(workers)


    def start_requests(self):
        return self.next_requests()

    def schedule_to_works(self):
        found = 0
        while found < self.redis_batch_size:
            data = self.redis_conn.lpop(self.check_queue)
            if not data:
                break
            self.redis_conn.rpush(self.work_queue,data)
            found +=1


    @classmethod
    def from_crawler(cls,crawler,*args,**kwargs):
        spider = super().from_crawler(crawler,*args,**kwargs)
        crawler.signals.connect(spider._spider_opened,signal=signals.spider_opened)
        crawler.signals.connect(spider._spider_idle,signal=signals.spider_idle)
        #crawler.signals.connect(spider._spider_closed,signal=signals.spider_closed)
        return spider

    def _spider_opened(self,spider):
        pass

    def _spider_idle(self,spider):
        self.schedule_next_requests()
        raise DontCloseSpider

    def schedule_next_requests(self):
        for req in self.next_requests():
            self.crawler.engine.crawl(req, spider=self)


    #self.worker_spider 工作的爬虫 例如安吉的爬虫
    def next_requests(self):
        fetch_one = self.redis_conn.lpop
        found = 0
        #self.schedule_to_works()
        while found < self.redis_batch_size:
            data = fetch_one(self.work_queue)
            if not data:
                break 
            links_dict = json.loads(data.decode('utf-8'))
            worker_spider = self.workers[links_dict['name']]() # 根据link_url 指定 worker_spider,workers 包含所有的爬虫实例
            yield worker_spider.generate_request(links_dict=links_dict,spider= self)
            found += 1



    def parse(self,response):
        worker_spider = self.workers[response.meta['name']]()
        items = HangzhouItem()
        #print('response.url',response.url)
        try:
            items['url'] = response.url
            items['project'] = 'hangzhou'
            items['spider'] = worker_spider.name
            items['server'] = socket.gethostname()
            items['crawling_date'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            #primary fields 
            items['source_website'] = worker_spider.source_website
            items['website_area'] = worker_spider.specific_area
            items['specific_area'] = response.meta['an_county']
            items['an_type'] = response.meta['an_type']
            items['an_major'] = response.meta['an_major']
            items['an_sub'] = response.meta['an_sub']
            items['project_title']=worker_spider.an_title_parse(response)
            items['on_date'] = worker_spider.an_on_date_parse(response)
            items['an_title'] = worker_spider.an_title_parse(response)
            items['an_url'] = worker_spider.final_url(response)
            items['an_refer_url'] = response.meta['an_refer_url']
            items['crawling_number'] = '1'
            items['an_content'] = worker_spider.an_content(response)
            items['code'] = 'NONE'
        except Exception as e:
            print('parse error',response.url)
            print('parse error',e)
        else:
            return items



