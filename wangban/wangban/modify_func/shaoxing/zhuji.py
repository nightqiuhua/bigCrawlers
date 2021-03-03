from lxml import etree
import lxml.html


def zhuji_modifier(response):
    body = lxml.html.fromstring(response)
    #
    body.make_links_absolute('http://www.zhuji.gov.cn/')
    etree.strip_elements(body,"script","style","title")
    del_ele = body.xpath('//div[@class="main-fl-gn bt-padding-right-20 bt-padding-left-20"]')
    for ele in del_ele:
        ele.clear()
    try:
        element = body.xpath('//div[@class="main-fl bt-left"]')[0]
    except Exception as e:
        raise e
    content = etree.tostring(element,encoding='utf-8')
    #print(content.decode('utf-8'))
    data = content.decode('utf-8')
    return data