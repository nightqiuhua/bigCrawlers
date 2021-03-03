from lxml import etree
import lxml.html
from .. import cleaner
import re

def jiaxing_modifier(response):
    body = lxml.html.fromstring(response)
    body.make_links_absolute('http://www.jxzbtb.cn/')
    etree.strip_elements(body,"script","style","title",'iframe')
    try:
        element = body.xpath('//div[@class="container"]')[0]
    except Exception as e:
        raise e
    del_eles = body.xpath('//div[@class="ewb-loca"]') + body.xpath('//p[@class="info-sources"]')
    for ele in del_eles:
        ele.clear()
    content = etree.tostring(element,encoding='utf-8')
    #print(content.decode('utf-8'))
    data = content.decode('utf-8')
    return data