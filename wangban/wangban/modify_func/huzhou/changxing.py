from lxml import etree
import lxml.html

def changxing_modifier(response):
    try:
        response = response.replace('iframe','p')
        body = lxml.html.fromstring(response)
        decide_element = body.xpath('//div[@class="Content_Border hidden"]')
        if len(decide_element):
            element = body.xpath('//div[@class="Content_Border hidden"]')[0]
        else:
            element = body.xpath('//td[@id="TDContent"]')[0]
        content = etree.tostring(element,encoding='utf-8')
        #print(content.decode('utf-8'))
        data = content.decode('utf-8')
    except Exception as e:
        raise e
    return data