from lxml import etree
import lxml.html

def huangyan_modifier(data):
    try:
        data['text'] = data['text'].replace('iframe','p')
        data['text'] = data['text'].replace('script','style')
        body = lxml.html.fromstring(data['text'])
        decide_element = body.xpath('//table[@id="ysq"]')
        if len(decide_element):
            element = body.xpath('//table[@id="ysq"]')[0]
        else:
            element = body.xpath('//div[@class="word-warp"]')[0]
        content = etree.tostring(element,encoding='utf-8')
        #print(content.decode('utf-8'))
        data['text'] = content.decode('utf-8')
    except Exception as e:
        raise e
    return data