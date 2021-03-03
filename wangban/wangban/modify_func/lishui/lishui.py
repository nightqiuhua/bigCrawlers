from lxml import etree
import lxml.html
from .. import cleaner
import re

def lishui_modifier(response):
    body = lxml.html.fromstring(response)

    body.make_links_absolute('http://www.lssggzy.com/')
    etree.strip_elements(body,"script","style","title",'iframe')
    del_eles = body.xpath('//div[@class="s-mid-head"]') + body.xpath('//div[@class="s-content-foot"]')
    for ele in del_eles:
        ele.clear()
    decide_element = body.xpath('//div[@class="contentall"]')
    try:
        if len(decide_element):
            element = body.xpath('//div[@class="contentall"]')[0]
        else:
            element = body.xpath('//div[@class="container"]')[0]
    except Exception as e:
        raise e

    content = etree.tostring(element,encoding='utf-8')
    #print(content.decode('utf-8'))
    data = content.decode('utf-8')
    return data