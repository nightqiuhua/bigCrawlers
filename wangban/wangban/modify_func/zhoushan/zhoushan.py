from lxml import etree
import lxml.html
from .. import cleaner
import re

def zhoushan_modifier(response):
    body = lxml.html.fromstring(response)
    body.make_links_absolute('http://www.zsztb.gov.cn/')
    etree.strip_elements(body,"script","style","title",'iframe')
    try:
        element = body.xpath('//table[@id="tblInfo"]')[0]
    except Exception as e:
        raise e
    content = etree.tostring(element,encoding='utf-8')
    data = content.decode('utf-8')
    return data