# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from twisted.internet.threads import deferToThread
from scrapy.conf import settings
import pymysql
from sql_sen import all_sql_sentence
from scrapy import signals
import time
from wangban_utils.mongo_util import get_mongodb_conn
from wangban_utils.mysql_util import MySqlDBClass
from wangban_utils.mongo_util import MongodbClass
#from wangban_utils.logging_util import update_logging
from wangban_utils.redis_util import get_redis_conn
from wangban_utils.countitem import CountIitem
import json
import threading
lock = threading.Lock()



class BasePipeline(object):
    @classmethod
    def from_crawler(cls,crawler,*args,**kwargs):
        spider = cls()
        crawler.signals.connect(spider._spider_opened,signal= signals.spider_opened)
        return spider

    def process_item(self,item,spider):
        return deferToThread(self._process_item,item,spider)

    def _process_item(self,item,spider):
        raise NotImplementedError


class HangzhouPipeline(BasePipeline):
    def __init__(self):
        super().__init__()
        self.mongo_conn = MongodbClass()

    def _spider_opened(self,spider):
        self.mysql_instance = MySqlDBClass()
        self.mongo_instance = MongodbClass()
        self.mysql_instance.create_table('t_zhaobiao')
        self.redis_conn = get_redis_conn()
        self.counter = CountIitem()

    def _process_item(self, item, spider):
        data = dict(item)
        check_data = {"_id":data["an_url"],"gettime":data["crawling_date"],"touch_time":data["crawling_date"],'sitename':data["source_website"]}
        
        if spider.name == 'zhejiangsj':
            table_name = "t_notice_grab"
        else:
            table_name = 't_zhaobiao'

        try:
            lock.acquire()
            self.mongo_conn.insert_into_db(check_data,'check_collections')
            print('{} Sending data to mysql'.format(spider.name))
        except Exception as e:
            pass
        else:
            pass
        finally:
            lock.release()

        try:
            self.counter.incr(data['spider'])
        except Exception as e:
            pass
        return item



class WangBanPipeline(BasePipeline):
    def _spider_opened(self,spider):
        self.mongo_instance = MongodbClass()
        self.redis_conn = get_redis_conn()

    def __init__(self):
        self.duplicate_count = 0

    def _process_item(self, item, spider):
        #print('Processing item')
        data = dict(item)
        try:
            data['_id'] = data['an_url']
        except KeyError as e:
            return item
        try:
            self.mongo_instance.insert_into_db(data,spider.name)
        except Exception as e:
            data['an_content'] = None
            data['type'] = 'content'
            data = json.dumps({data['an_url']:data})
            self.redis_conn.rpush(spider.check_queue,data)
        #check_len = self.redis_conn.llen(spider.check_queue)
        #work_len = self.redis_conn.llen(spider.work_queue)
        #if not (check_len or work_len):
        #    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        #    print('{} {} has no more requests'.format(now_time,spider.name))
        return item