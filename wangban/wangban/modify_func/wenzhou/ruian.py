from lxml import etree
import lxml.html
import re

def ruian_modifier(response):
    body = lxml.html.fromstring(response)
    etree.strip_elements(body,"script","style","title",'iframe')
    try:
        element = body.xpath('//td[@id="TDContent"]')[0]

    except Exception as e:
        raise e
    content = etree.tostring(element,encoding='utf-8')
    #print(content.decode('utf-8'))
    data = content.decode('utf-8')
    return data