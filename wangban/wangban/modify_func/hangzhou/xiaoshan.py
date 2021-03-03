from lxml import etree
import lxml.html
from .. import cleaner
import re

def xiaoshan_modifier(response):
    body = lxml.html.fromstring(response)
    body.make_links_absolute('http://www.xszbjyw.com/')
    etree.strip_elements(body,"script","style","title")
    try:
        element = body.xpath('//div[@class="Content"]')[0]
    except Exception as e:
        raise e
    content = etree.tostring(element,encoding='utf-8').decode('utf-8')
    data = cleaner.clean_html(content)
    return data