# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class HangzhouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
    server = scrapy.Field()
    crawling_date = scrapy.Field()

    #primary fields 
    source_website = scrapy.Field()#
    website_area = scrapy.Field()
    specific_area = scrapy.Field()
    an_type = scrapy.Field()
    an_major = scrapy.Field()
    an_sub = scrapy.Field()
    project_title = scrapy.Field()
    on_date = scrapy.Field()
    an_title = scrapy.Field()
    an_content = scrapy.Field()
    an_url = scrapy.Field()
    an_refer_url = scrapy.Field()
    total_page = scrapy.Field()
    crawling_number = scrapy.Field()
    code = scrapy.Field()
