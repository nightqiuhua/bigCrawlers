from lxml import etree
import lxml.html

def yuhuan_ajax_modifier(response):
    try:
        response = response.replace('iframe','p')

        body = lxml.html.fromstring(response)
        element = body.xpath('//body')[0]
        content = etree.tostring(element,encoding='utf-8')
        #print(content.decode('utf-8'))
        data = content.decode('utf-8')
    except Exception as e:
        raise e
    return data