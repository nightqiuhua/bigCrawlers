# -*- coding: utf-8 -*-
import __init__
from work_urls import all_work_urls
from scrapy.utils.project import get_project_settings
from task_store.taskcore import TaskCore
import time
import schedule
import os
SETTINGS = get_project_settings()

class TasksInput:
    def __init__(self):
        #self.interval = interval
        self.task_list = list(all_work_urls.keys())
        self.task_num_at_once = 3
        self.con_task = ['longyou','longyou','longyou_ajax','linhai']

    def running_task(self):
        #self.task_list = ['leqing']
        work_task = TaskCore()
        for task_name in self.task_list:
            if task_name in self.con_task:
                continue
            work_task.run(all_work_urls.get(task_name))
        print('{} work in this round has fininshed'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))


if __name__ == '__main__':
    work_schedule = TasksInput()
    work_schedule.running_task()