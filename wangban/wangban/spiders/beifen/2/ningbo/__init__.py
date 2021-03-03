# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import sys 
import os
BASH_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASH_DIR)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))