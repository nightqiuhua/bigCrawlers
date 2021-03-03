# -*- coding: utf-8 -*-
#实时调度模块将一个tasks的url放入缓存数据库的队列中，spider从队列中提取url并开始爬取,
#spider返回一个招投标列表，实时调度模块检查招投标列表中每一个
#招投标的日期，以此来判断是否要抓取该数据。实时调度模块再判断是否满足终止调度条件
#
#先判断有没有需要抓取的数据，如果有把数据抓完，再判断是否满足终止条件
#如果没有，直接判断是否满足终止条件
#1.从任务库中提取urls(type:sub)
#2.将urls(type:sub)存入spider的工作队列中,spider生成urls(type:content,type:column)
#3.spider将urls(type:content,type:column)返回到工作队列中
#4.检查工作队列中spider返回的urls(type:content)是否满足抓取条件
#5.逐个判断urls(type:content)，满足条件的urls(type:content)由爬虫抓取
#6.不满足条件的urls(type:content)，直接删除，不再抓取
#7.判断需要抓取的数据是否抓取完毕，如果抓取完毕则停止向spider的工作队列存入urls(type:sub)，等待下一轮的抓取判断
#8.将新抓取的数据写入爬取日志中
#
#OnTimeTasks 是对数据库里的数据进行操作
#redis数据库中，设定2个队列，一个是wanbang:wencheng:an_urls_work队列，另一个是wanbang:wencheng:an_urls_check队列
#爬虫从wanbang:wencheng:an_urls_work队列获取urls，来完成任务
#爬虫将爬取到的urls存入wanbang:wencheng:an_urls_check队列
#实时调度器将wanbang:wencheng:an_urls_check队列里的urls放入wanbang:wencheng:an_urls_work队列里
#
import __init__
import schedule
from datetime import datetime
import time
from tasks import all_tasks
from wangban_utils.redis_util import get_redis_conn
import re
import logging
import threading
from wangban_utils.mysql_util import get_mysql_conn
import json
import os
from datetime import timedelta
from wangban_utils.mysql_util import MySqlDBClass
#check_mysql_dict = {
#    #'MYSQL_HOST': "rm-bp1k68h2lq872j040mo.mysql.rds.aliyuncs.com",
#    #'MYSQL_PORT': 3306,
#    #'MYSQL_USER':"root",
#    #'MYSQL_PASSWORD':"N5QjbPu097Kuz4BV",
#    #'MYSQL_DBNAME':"zhaobiao",
#    'MYSQL_HOST' : '127.0.0.1',
#    'MYSQL_PORT' : 3306,
#    'MYSQL_USER' :"root",
#    'MYSQL_PASSWORD':"123456",
#    'MYSQL_DBNAME' :"zhaobiao",
#}
#
#UPDATE_FILE_DIR = 'C:\\Program Files (x86)\\crawling_server\\wangban\\wangban\\log\\update_log'

class UpdateFilterClass:
    def __init__(self,spider_name,check_date =None,timeout=100):
        self.tasks = all_tasks[spider_name]
        self.reflesh_urls = []
        self.limitpages = 3
        self.conn = get_redis_conn()
        self.mysql_conn = MySqlDBClass()
        self.outdate = 0#用来判断是否有过期的日期，如果有说明实时爬取的范围有效
        self.logger_filename = spider_name
        self.check_date = check_date
        self.spider_name = spider_name
        print('UpdateFilterClass mysql',self.mysql_conn)

    def byte_to_dict(self,item):
        try:
            links_dict = json.loads(item.decode('utf-8').replace("'", "\""))
        except Exception as e:
            print('byte_to_dict error',e)
            return False
        return links_dict

    def dict_to_byte(self,links_dict):
        try:
            links_dict = json.dumps(links_dict)
        except Exception as e:
            print('dict_to_byte error',e)
            return False
        return links_dict
#自己建立要检查的column_urls池，对比抓取的column_urls，如果column_urls不在其中，就删掉

#check_label为true时，说明该url需要抓取
    def check_url(self,url_item):
        check_label = False
        try:
            for link,link_value in url_item.items():
                if link_value['type'] == 'sub':
                    check_label = True
                if link_value['type'] == 'column':
                    check_label = True
                if link_value['type'] == 'content':
                    up_date_check_able = self.up_date_check(link,link_value)
                    if not up_date_check_able:
                        self.outdate += 1
                        #    self.reflesh_urls.append({link:link_value})
                    not_seen_check_able = self.not_seen_check(link)
                    if not_seen_check_able:
                        return True
                    check_label = (up_date_check_able and not_seen_check_able)
                #print('check_label ',check_label)
        except Exception as e:
            print('check_url error reason:',e)
        return check_label

    def up_date_check(self,link,link_value):
        try:
            if link_value['on_date']:
                content_url_date = self.parse_ymd(link_value['on_date'])
                check_date = self.check_date
                if isinstance(check_date,str):
                    check_date=self.parse_ymd(check_date)
                #print('content_url_date', content_url_date,'check_date',check_date)
                if content_url_date >= check_date:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            return True

    def not_seen_check(self,link):
        seen_check = self.mysql_conn.detect_existence(link,self.spider_name)
        #print('not_seen_check {} {}'.format(link,seen_check))
        return (not seen_check)
        #print('seen_check',seen_check_able)

    def get_update_date(self):
        sql = "select gettime from {}".format(self.spider_name)
        cursor = self.mysql_conn.db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        try:
            update_date = max(results)[0]
        except Exception as e:
            print('update_date error',e)
            update_date = 'NONE'
        try:
            update_date = re.findall(r'\d+-\d+-\d+',update_date)[0]
        except Exception as e:
            print('get_update_date error',e)
            update_date = time.strftime("%Y-%m-%d", time.localtime())
        #update_date = '2018-11-19'
        update_date = self.parse_ymd(update_date)-timedelta(days=2)
        #update_date = '2018-11-19'
        return update_date


    def parse_ymd(self,s):
        year_s,mon_s,day_s = s.split('-')
        return datetime(int(year_s),int(mon_s),int(day_s))

#设定更新条目数量不超过网页前三页的总数量，因此只对前三页进行爬取，筛选前三页的数据
    def check_terminations(self):
        if self.outdate:
            #print('outdate an_content number',self.outdate)
            print('terminous condition is reached')
            #pass

    def yield_from_check(self):
        found = 0
        time.sleep(1)
        while found < 50:
            data = self.conn.lpop(self.tasks['task_check'])
            if not data:
                break
            yield data
            found += 1

    def check_to_work(self):
        #print('welcom to check_to_work')
        finished_label = False
        for data in self.yield_from_check():
            if not data:
                continue
            link_dict = self.byte_to_dict(data)
            if not link_dict:
                continue
            if self.check_url(link_dict):
                link_dict = self.dict_to_byte(link_dict)
                if not link_dict:
                    continue
                self.conn.rpush(self.tasks['task_queue'],link_dict)
        if not self.conn.llen(self.tasks['task_check']):
            finished_label = True
        return finished_label

    def clear(self):
        self.reflesh_urls = []
        self.outdate = 0


    def run(self):
        if self.check_date == None:
            self.check_date = self.get_update_date()
        finished_label = self.check_to_work()
        if finished_label:
            self.check_terminations()
            self.clear()


if __name__ == '__main__':
    def wenchengtasks(spider_name):
        print('i am working now ')
        worker = OnTimeTasks(spider_name)
        worker.run()
    wenchengtasks('jiande')
