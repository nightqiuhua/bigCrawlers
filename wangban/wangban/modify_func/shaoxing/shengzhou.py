from lxml import etree
import lxml.html

def shengzhou_modifier(response):
    body = lxml.html.fromstring(response)
    #嵊州
    body.make_links_absolute('http://220.191.224.142/')
    etree.strip_elements(body,"script","style","title")
    try:
        element = body.xpath('//div[@class="ewb-right-bd ewb-mt10"]')[0]
    except Exception as e:
        raise e
    content = etree.tostring(element,encoding='utf-8')
    #print(content.decode('utf-8'))
    data = content.decode('utf-8')
    return data