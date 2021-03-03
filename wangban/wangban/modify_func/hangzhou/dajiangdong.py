from lxml import etree
import lxml.html
import re

def dajiangdong_modifier(response):
    try:

        response = response.replace('iframe','p')
        body = lxml.html.fromstring(response)
        decide_element = body.xpath('//div[@class="AfficheContent"]')
        if len(decide_element):
            element = body.xpath('//div[@class="AfficheContent"]')[0]
        else:
            element = body.xpath('//div[@class="Content"]')[0]
        content = etree.tostring(element,encoding='utf-8')
        #print(content.decode('utf-8'))
        data = content.decode('utf-8')
    except Exception as e:
        if '未发布' in response:
            data = response
        else:
            raise e
    return data