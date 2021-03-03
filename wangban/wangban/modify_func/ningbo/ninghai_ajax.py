from lxml import etree
import lxml.html

def ninghai_ajax_modifier(response):
    try:
        response = response.replace('iframe','p')
        body = lxml.html.fromstring(response)
        #element = body.xpath('//div[@class="newsdetails-bg"]')[0]
        decide_element_1 = body.xpath('//div[@class="content-box"]')
        if len(decide_element_1):
            element = body.xpath('//div[@class="content-box"]')[0]
        else:
            element = body.xpath('//div[@class="newsdetails-bg"]')[0]

        content = etree.tostring(element,encoding='utf-8')
        #print(content.decode('utf-8'))
        data = content.decode('utf-8')
    except Exception as e:
        raise e
    return data