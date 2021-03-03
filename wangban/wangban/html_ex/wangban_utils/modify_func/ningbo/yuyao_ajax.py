from lxml import etree
import lxml.html

def yuyao_ajax_modifier(data):
    try:
        data['text'] = data['text'].replace('iframe','p')
        body = lxml.html.fromstring(data['text'])
        decide_element_1 = body.xpath('//div[@class="newsdetails-bg"')
        decide_element_2 = body.xpath('//div[@class="detail-info"]')
        if len(decide_element_1):
            element = body.xpath('//div[@class="newsdetails-bg"]')[0]
        elif len(decide_element_2):
            element = body.xpath('//div[@class="detail-info"]')[0]
        else:
            element = body.xpath('//div[@class="inner-main-content"]')[0]
        content = etree.tostring(element,encoding='utf-8')
        #print(content.decode('utf-8'))
        data['text'] = content.decode('utf-8')
    except Exception as e:
        raise e
    return data