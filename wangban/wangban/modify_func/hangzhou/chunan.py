from lxml import etree
import lxml.html
import re

def chunan_modifier(response):
    body = lxml.html.fromstring(response)
    body.make_links_absolute('http://www.cajyzx.org.cn:8080/')
    etree.strip_elements(body,"script","style","title")
    del_eles = body.xpath('//font[@class="webfont"]')
    for ele in del_eles:
        ele.clear()
    try:
        element = body.xpath('//table[@id="Table4"]')[0]
    except Exception as e:
        raise e
    content = etree.tostring(element,encoding='utf-8')
    #print(content.decode('utf-8'))
    data = content.decode('utf-8')
    return data