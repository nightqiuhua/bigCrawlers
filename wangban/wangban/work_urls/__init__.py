# -*- coding: utf-8 -*-

import sys 
import os
import importlib
import re 
from scrapy.utils.project import get_project_settings
SETTINGS = get_project_settings()
task_module_list = SETTINGS['SPIDER_MODULES_LIST']


all_work_urls = {}

def dynamic_import(module):
    return importlib.import_module(module,'work_urls')


def get_crawl_task(module_name):
    module = dynamic_import(module_name)
    return module.main()

for module_name in task_module_list:
    key = re.findall(r'\..*\.(.*)',module_name['path'])[0]
    all_work_urls[key] = get_crawl_task(module_name['path'])

