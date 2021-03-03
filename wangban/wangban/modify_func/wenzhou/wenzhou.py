from lxml import etree
import lxml.html
from .. import cleaner
import re

def wenzhou_modifier(response):
    content = cleaner.clean_html(response)
    body = lxml.html.fromstring(content)
    body.make_links_absolute('https://ggzy.wzzbtb.com/')
    etree.strip_elements(body,"script","style","title",'iframe')
    try:
        element = body.xpath('//div[@class="Main-p"]')[0]
        content = etree.tostring(element,encoding='utf-8')
    except Exception as e:
        raise e
    data = content.decode('utf-8')
    return data