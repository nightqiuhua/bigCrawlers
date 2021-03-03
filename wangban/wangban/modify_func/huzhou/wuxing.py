from lxml import etree
import lxml.html

def wuxing_modifier(response):
    body = lxml.html.fromstring(response)
    body.make_links_absolute('http://ggzy.wuxing.gov.cn/')
    etree.strip_elements(body,"script","style","title",'iframe')
    try:
        element = body.xpath('//div[@class="zw"]')[0]
    except Exception as e:
        raise e
    content = etree.tostring(element,encoding='utf-8')
    #print(content.decode('utf-8'))
    data = content.decode('utf-8')
    return data