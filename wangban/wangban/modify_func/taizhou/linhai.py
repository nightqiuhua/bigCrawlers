from lxml import etree
import lxml.html

def linhai_modifier(response):
    try:
        response = response.replace('iframe','p')
        response = response.replace('script','style')
        body = lxml.html.fromstring(response)
        element = body.xpath('//td[@id="RightPane"]')[0]
        content = etree.tostring(element,encoding='utf-8')
        #print(content.decode('utf-8'))
        data = content.decode('utf-8')
    except Exception as e:
        raise e
    return data