from lxml import etree
import lxml.html

def yuecheng_modifier(data):
    try:
        data['text'] = data['text'].replace('iframe','p')
        body = lxml.html.fromstring(data['text'])
        decide_element = body.xpath('//div[@class="main-txt"]')
        if len(decide_element):
            element = body.xpath('//div[@class="main-txt"]')[0]
        else:
            element = body.xpath('//table[@id="article"]')[0]
        content = etree.tostring(element,encoding='utf-8')
        #print(content.decode('utf-8'))
        data['text'] = content.decode('utf-8')
    except Exception as e:
        raise e
    return data#