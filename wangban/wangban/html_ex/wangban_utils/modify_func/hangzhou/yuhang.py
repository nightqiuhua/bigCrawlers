from lxml import etree
import lxml.html

def yuhang_modifier(data):
    try:
        data['text'] = data['text'].replace('iframe','p')
        body = lxml.html.fromstring(data['text'])
        decide_element_1 = body.xpath('//div[@class="AfficheContent"]')
        if len(decide_element_1):
            element = body.xpath('//div[@class="AfficheContent"]')[0]
        else:
            element = body.xpath('//div[@class="Content"]')[0]
        content = etree.tostring(element,encoding='utf-8')
        #print(content.decode('utf-8'))
        data['text'] = content.decode('utf-8')
    except Exception as e:
        raise e
    return data