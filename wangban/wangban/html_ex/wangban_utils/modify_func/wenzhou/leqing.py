from lxml import etree
import lxml.html

def leqing_modifier(data):
    try:
        data['TEXT'] = data['TEXT'].replace('iframe','p')
        data['TEXT'] = data['TEXT'].replace('script','tbody')
        body = lxml.html.fromstring(data['TEXT'])
        element = body.xpath('//div[@class="article-block"]')[0]
        content = etree.tostring(element,encoding='utf-8')
        title =body.xpath('//h2/text()')
        #print(content.decode('utf-8'))
        #data['TEXT'] = content.decode('utf-8')
        data['TEXTTITLE'] = ''.join(title)
        data['TITLE'] = ''.join(title)
    except Exception as e:
        raise e
    return data