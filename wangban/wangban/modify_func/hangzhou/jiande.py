from lxml import etree
import lxml.html
import re

def jiande_modifier(response):
    body = lxml.html.fromstring(response)
    body.make_links_absolute('http://www.jdggzy.com/')
    etree.strip_elements(body,"script","style","title",'iframe')
    del_ele = body.xpath('//div[@id="ctl00_ContentPlaceHolder1_divQuestion"]')
    for ele in del_ele:
        ele.clear()
    try:
        element = body.xpath('//div[@class="Content"]')[0]
    except Exception as e:
        if '未发布' in response:
            data = response
        else:
            raise e
    content = etree.tostring(element,encoding='utf-8')
    #print(content.decode('utf-8'))
    data = content.decode('utf-8')
    return data