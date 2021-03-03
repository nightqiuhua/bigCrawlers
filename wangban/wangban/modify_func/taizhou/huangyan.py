from lxml import etree
import lxml.html

def huangyan_modifier(response):
    try:
        response = response.replace('iframe','p')
        response = response.replace('script','style')
        body = lxml.html.fromstring(response)
        decide_element_1 = body.xpath('//table[@id="ysq"]')
        decide_element_2 = body.xpath('//div[@class="word-warp"]')
        if len(decide_element_1):
            element = body.xpath('//table[@id="ysq"]')[0]
        elif len(decide_element_2):
            element = body.xpath('//div[@class="word-warp"]')[0]
        else:
            element = body.xpath('//div[@id="zoom"]')[0]
        content = etree.tostring(element,encoding='utf-8')
        #print(content.decode('utf-8'))
        data = content.decode('utf-8')
    except Exception as e:
        raise e
    return data