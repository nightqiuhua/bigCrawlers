#from spiders import all_spiders
import __init__
from work_urls import all_work_urls
from spiders import all_spiders
from scrapy.utils.project import get_project_settings
import time
import schedule
import os
import json
from wangban_utils.dict_process import bfs
SETTINGS = get_project_settings()


def new_tasks(task_list):
    work_urls = []
    for task in task_list:
        for sub_url,value_list in bfs(task):
            sub_url_dict = {}
            sub_url_dict['an_major'] = value_list[0]
            sub_url_dict['an_type'] = value_list[1]
            sub_url_dict['an_sub'] = value_list[2]
            sub_url_dict['an_county'] = value_list[3]
            sub_url_dict['an_sub_url'] =sub_url
            #sub_url_dict["afficheType"] =sub_url[0]
            #try:
            #    sub_url_dict['proID'] =sub_url[1]
            #except Exception as e:
            #    pass
            
            work_urls.append(sub_url_dict)
    return work_urls

def running_task():
    task_list = ['taizhou']
    for task_name in task_list:
        data = new_tasks(all_work_urls[task_name]['tasks'])
        #print(data)
        with open(task_name+'.json','w',encoding='utf-8') as fp:
            json.dump(data,fp,indent=4,ensure_ascii=False)


if __name__ == '__main__':
	running_task()
