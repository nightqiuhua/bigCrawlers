from lxml import etree
import lxml.html

def shengzhou_modifier(data):
    try:
        data['text'] = data['text'].replace('iframe','p')
        body = lxml.html.fromstring(data['text'])
        element = body.xpath('//div[@id="mainContent"]')[0]
        content = etree.tostring(element,encoding='utf-8')
        #print(content.decode('utf-8'))
        data['text'] = content.decode('utf-8')
        data['an_title'] = re.sub(r'\s+','',data['an_title'])
    except Exception as e:
        raise e
    return data#id="article"