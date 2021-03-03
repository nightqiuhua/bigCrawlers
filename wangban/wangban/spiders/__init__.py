## This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import sys
import os
from scrapy.utils.project import get_project_settings
BASH_DIR_1 = os.path.dirname(os.path.abspath(__file__))
BASH_DIR_2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASH_DIR_1)
sys.path.append(BASH_DIR_2)

import importlib
import re
SETTINGS = get_project_settings()
module_list = SETTINGS['SPIDER_MODULES_LIST']

#from spiders.huzhou.huzhou import HuZhouSpider
#from spiders.hangzhou.chunan import ChunAnSeleSpider,ChunAnSpider
#from spiders.hangzhou.xihuqu import XiHuQuSeleSpider,XiHuQuSpider

#workers = {'huzhou':HuZhouSpider,'chunan':ChunAnSpider,'xihuqu':XiHuQuSpider}
#all_sele_spider = {'chunan':ChunAnSeleSpider,'xihuqu':XiHuQuSeleSpider}

workers = {}
all_sele_spider = {}
#
def dynamic_import(key,name_pre,module):
    my_test_module= importlib.import_module(module,'spiders')
    for post_suf in ['SeleSpider','Spider']:
        try:
            my_test_module_test = getattr(my_test_module,'{}{}'.format(name_pre,post_suf))
            if post_suf == 'SeleSpider':
                all_sele_spider[key] = my_test_module_test
            if post_suf == 'Spider':
                workers[key] = my_test_module_test
        except Exception as e:
            pass
        

for module_name in module_list:
    key = re.findall(r'\..*\.(.*)',module_name['path'])[0]
    dynamic_import(key,module_name['scr_spider'],module_name['path'])


