from lxml import etree
import lxml.html

def xinchang_modifier(response):
    body = lxml.html.fromstring(response)
    #新昌
    body.make_links_absolute('http://www.zjxc.gov.cn/')
    etree.strip_elements(body,"script","style","title",'iframe','meta')
    del_ele = body.xpath('//div[@id="zoom"]/a[@href="http://www.hanweb.com"]') + body.xpath('//div[@id="hiddenLocation"]')
    for ele in del_ele:
        ele.clear()
    try:
        element = body.xpath('//div[@id="zoom"]')[0]
    except Exception as e:
        raise e
    content = etree.tostring(element,encoding='utf-8')
    #print(content.decode('utf-8'))
    data = content.decode('utf-8')
    return data