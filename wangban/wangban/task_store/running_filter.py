import __init__
from wangban_utils.updatefilterfunc import UpdateFilterClass
import os
import time



def run_filter_func():
    spider_filter = UpdateFilterClass()
    spider_filter.run()

if __name__ == '__main__':
    run_filter_func()
