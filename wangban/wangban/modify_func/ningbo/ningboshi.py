from lxml import etree
import lxml.html
from .. import cleaner
import re

def ningboshi_modifier(response):
    content = cleaner.clean_html(response)
    body = lxml.html.fromstring(content)
    body.make_links_absolute('http://www.bidding.gov.cn/')
    etree.strip_elements(body,"script","style","title",'iframe')
    try:
        element_decide_1 = body.xpath('//div[@class="content-box"]')
        if len(element_decide_1):
            element = body.xpath('//div[@class="content-box"]')[0]
        else:
            element = body.xpath('//div[@class="frameNews"]')[0]
    except Exception as e:
        raise e
    content = etree.tostring(element,encoding='utf-8')
    #print(content.decode('utf-8'))
    data = content.decode('utf-8')
    return data