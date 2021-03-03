from lxml import etree
import lxml.html
import re

def anji_modifier(response):
    body = lxml.html.fromstring(response)
    body.make_links_absolute('http://www.ajztb.com/')
    del_ele = body.xpath('//div[@class="ewb-route"]')
    for ele in del_ele:
        ele.clear()
    etree.strip_elements(body,"script","style","title",'iframe')
    try:
        element = body.xpath('//div[@class="ewb-container"]')[0]
    except Exception as e:
        raise e
    content = etree.tostring(element,encoding='utf-8')
    #print(content.decode('utf-8'))
    data = content.decode('utf-8')
    return data