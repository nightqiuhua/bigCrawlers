from lxml import etree
import lxml.html

def ninghai_modifier(data):
    try:
        data['text'] = data['text'].replace('iframe','p')
        body = lxml.html.fromstring(data['text'])
        decide_elem = body.xpath('//div[@class="newsdetails-bg"]')
        if len(decide_elem):
            element = body.xpath('//div[@class="newsdetails-bg"]')[0]
        else:
            element = body.xpath('//div[@class="content"]')[0]
        content = etree.tostring(element,encoding='utf-8')
        #print(content.decode('utf-8'))
        data['text'] = content.decode('utf-8')
    except Exception as e:
        raise e
    return data