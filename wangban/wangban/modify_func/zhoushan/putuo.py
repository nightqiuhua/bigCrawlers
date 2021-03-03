from lxml import etree
import lxml.html

def putuo_modifier(response):
    body = lxml.html.fromstring(response)
    #普陀区
    body.make_links_absolute('http://www.zsptztb.com.cn/')
    etree.strip_elements(body,"script","style","title")
    try:
        element = body.xpath('//table[@id="tblInfo"]')[0]
    except Exception as e:
        raise e
    content = etree.tostring(element,encoding='utf-8')
    #print(content.decode('utf-8'))
    data = content.decode('utf-8')
    return data