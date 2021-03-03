from lxml import etree
import lxml.html

def yuhuan_modifier(response):
    try:
        response = response.replace('iframe','p')
        body = lxml.html.fromstring(response)
        decide_element_1 = body.xpath('//td[@id="contentText"]')
        decide_element_2 = body.xpath('//div[@class="details-content"]')
        if len(decide_element_1):
            element = body.xpath('//td[@id="contentText"]')[0]
        elif len(decide_element_2):
            element = body.xpath('//div[@class="details-content"]')[0]
        else:
            element = body.xpath('//div[@class="inner-main-content"]')[0]
        content = etree.tostring(element,encoding='utf-8')
        #print(content.decode('utf-8'))
        data = content.decode('utf-8')
    except Exception as e:
        raise e
    return data