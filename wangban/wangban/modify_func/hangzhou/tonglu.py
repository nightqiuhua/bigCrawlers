from lxml import etree
import lxml.html
import re

def tonglu_modifier(response):
    body = lxml.html.fromstring(response)
    body.make_links_absolute('http://www.tlztb.com.cn/')
    etree.strip_elements(body,"script","style","title",'iframe')
    del_ele = body.xpath('//div[@id="divQuestion"]')
    for ele in del_ele:
        ele.clear()
    try:
        element = body.xpath('//div[@id="othercont"]')[0]
    except Exception as e:
        raise e
    content = etree.tostring(element,encoding='utf-8')
    data = content.decode('utf-8')
    return data