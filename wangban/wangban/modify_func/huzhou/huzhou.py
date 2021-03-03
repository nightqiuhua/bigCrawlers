from lxml import etree
import lxml.html
from .. import cleaner
import re

def huzhou_modifier(response):

    body = lxml.html.fromstring(response)
    body.make_links_absolute('http://ggzy.huzhou.gov.cn/')
    etree.strip_elements(body,"script","style","title",'iframe')
    try:
        element = body.xpath('//div[@align="center"]/table')[0]
    except Exception as e:
        raise e
    del_eles = body.xpath('//td[@class="float"]')
    for ele in del_eles:
        ele.clear()
    content = etree.tostring(element,encoding='utf-8')
    #print(content.decode('utf-8'))
    data = content.decode('utf-8')
    return data