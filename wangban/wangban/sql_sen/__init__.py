# -*- coding: utf-8 -*-
import sys 
import os
import importlib
import re 


from scrapy.utils.project import get_project_settings
SETTINGS = get_project_settings()
sql_module_list = SETTINGS['SQL_MODULE_LIST']
#

all_sql_sentence = {}


def dynamic_import(module):
    return importlib.import_module(module,'sql_sen')


def get_crawl_task(module_name):
    module = dynamic_import(module_name)
    return module.main()

for module_name in sql_module_list:
    key = re.findall(r'\.(.*)',module_name)[0]
    value = get_crawl_task(module_name)
    all_sql_sentence[key] = {'create_table':value[0],'sql_insert':value[1]}

#print(all_sql_sentence)