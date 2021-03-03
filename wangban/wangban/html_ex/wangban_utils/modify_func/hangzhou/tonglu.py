from lxml import etree
import lxml.html

def tonglu_modifier(data):
    try:
        data['text'] = data['text'].replace('iframe','p')
        body = lxml.html.fromstring(data['text'])
        element = body.xpath('//div[@id="othercont"]')[0]
        decide_element = body.xpath('//div[@id="AfficheContent"]')
        if len(decide_element):
            element = body.xpath('//div[@id="AfficheContent"]')[0]
        else:
            element = body.xpath('//div[@id="othercont"]')[0]
        #id="AfficheContent"
        content = etree.tostring(element,encoding='utf-8')
        #print(content.decode('utf-8'))
        data['text'] = content.decode('utf-8')
    except Exception as e:
        raise e
    return data