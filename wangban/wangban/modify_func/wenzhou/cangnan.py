from lxml import etree
import lxml.html
import re

def cangnan_modifier(response):
    body = lxml.html.fromstring(response)
    body.make_links_absolute('http://122.228.139.57/')
    etree.strip_elements(body,"script","style","title",'iframe')
    try:
        element = body.xpath('//td[@id="TDContent"]')[0]
        file_elements = body.xpath('//table[@id="filedown"]')
        element.extend(file_elements)
    except Exception as e:
        raise e
    content = etree.tostring(element,encoding='utf-8')
    data = content.decode('utf-8')
    return data