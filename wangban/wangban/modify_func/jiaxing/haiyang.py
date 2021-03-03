from lxml import etree
import lxml.html

def haiyang_modifier(response):
    body = lxml.html.fromstring(response)
    body.make_links_absolute('http://hy.jxzbtb.cn/')
    del_ele = body.xpath('//div[@class="ewb-loca"]')
    for ele in del_ele:
        ele.clear()
    etree.strip_elements(body,"script","style","title",'iframe')
    try:
        element = body.xpath('//div[@class="container"]')[0]

    except Exception as e:
        raise e
    content = etree.tostring(element,encoding='utf-8')
    #print(content.decode('utf-8'))
    data = content.decode('utf-8')
    return data