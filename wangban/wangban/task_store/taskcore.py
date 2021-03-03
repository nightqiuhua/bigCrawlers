# -*- coding: utf-8 -*-
from datetime import datetime
import time
from wangban_utils.redis_util import get_redis_conn
import re
import json
from scrapy.utils.project import get_project_settings
import os
SETTINGS = get_project_settings()

class TaskCore:
    def __init__(self,timeout=300):
        self.conn = get_redis_conn()
        self.filepath = SETTINGS['CDATA_FILE_PATH']
        self.error_filepath = SETTINGS['EDATA_FILE_PATH']

    def get_tasks(self,tasks):
        for item in tasks['tasks']:
            item['an_sub_url'] = self.sub_url_defined(self.spider_name,item)
            item['type'] = 'sub'
            item['name'] = self.spider_name
            item['an_county'] = self.get_an_county(self.spider_name,item)
            item['formdata'] = self.gen_formdata(self.spider_name,item)
            yield item

    def sub_url_defined(self,name,option_list):
        return option_list['an_sub_url']

    def get_an_county(self,name,option_list):
        return option_list.get('an_county','NONE')

    def gen_formdata(self,name,option_list):
        if name in ["hangzhou","fuyang"]:
            formdata = {}
            formdata["afficheType"] = option_list["afficheType"]
            formdata["_search"] ="False"
            formdata["rows"]="10"
            formdata["page"]="1"
            formdata["sidx"]="PublishStartTime"
            formdata["sord"]="desc"
            try:
                formdata["proID"] = option_list["proID"]
            except Exception as e:
                formdata["proID"] = ''
        else:
            formdata = {}
        return formdata


    def put_tasks(self,sub_url_dict,tasks):
        sub_url_dict = self.dict_to_byte(sub_url_dict)
        if tasks['html_type'] == 'ajax':
            self.conn.lpush(SETTINGS['SUB_SELE_TASKS'],sub_url_dict)
        else:
            self.conn.lpush(SETTINGS['URLS_CHECK_TASKS'],sub_url_dict)

    def run(self,tasks):
        self.spider_name = tasks['name']
        print('begin {} ontimetasks {} '.format(self.spider_name,datetime.now()))
        for sub_url_dict in self.get_tasks(tasks):
            self.put_tasks(sub_url_dict,tasks)


    def dict_to_byte(self,links_dict):
        try:
            links_dict = json.dumps(links_dict)
        except Exception as e:
            print('dict_to_byte error',e)
            return False
        return links_dict

if __name__ == '__main__':
    worker = OnTimeTasks(spider_name)
    worker.run()
