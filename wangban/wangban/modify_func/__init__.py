# -*- coding: utf-8 -*-
#BASH_DIR = os.path.dirname(os.path.abspath(__file__))
#sys.path.append(BASH_DIR)

import sys 
import os
import importlib
import re
from scrapy.utils.project import get_project_settings
from lxml.html.clean import Cleaner
cleaner = Cleaner(page_structure=False, links=False,style=True,scripts=True)



SETTINGS = get_project_settings()
func_module_list = SETTINGS['SPIDER_MODULES_LIST']

all_modify_func = {}

def dynamic_import(key,module):
    
    my_test_module= importlib.import_module(module,'modify_func')
    my_test_module_test = getattr(my_test_module,'{}_modifier'.format(key))
    return my_test_module_test

for module_name in func_module_list:
    key = re.findall(r'\..*\.(.*)',module_name['path'])[0]
    all_modify_func[key] = dynamic_import(key,module_name['path'])