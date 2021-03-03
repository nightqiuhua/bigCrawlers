from lxml import etree
import lxml.html

def jiaxing_modifier(data):
    try:
        data['text'] = data['text'].replace('iframe','p')
        data['text'] = data['text'].replace('script','tbody')
        body = lxml.html.fromstring(data['text'])
        element = body.xpath('//div[@class="container"]')[0]
        content = etree.tostring(element,encoding='utf-8')
        #print(content.decode('utf-8'))
        data['text'] = content.decode('utf-8')
    except Exception as e:
        raise e
    return data