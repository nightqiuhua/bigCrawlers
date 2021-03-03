from lxml import etree
import lxml.html

def beilun_modifier(data):
    try:
        data['text'] = data['text'].replace('iframe','p')
        body = lxml.html.fromstring(data['text'])
        #
        decide_element = body.xpath('//td[@class="lh30 fs14"]')
        if len(decide_element):
            element = body.xpath('//td[@class="lh30 fs14"]')[0]
        else:
            element = body.xpath('//form/table')[0]
        content = etree.tostring(element,encoding='utf-8')
        #print(content.decode('utf-8'))
        data['text'] = content.decode('utf-8')
    except Exception as e:
        raise e
    return data