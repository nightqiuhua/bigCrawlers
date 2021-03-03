from lxml import etree
import lxml.html
from .. import cleaner

def quzhou_modifier(response):
    body = lxml.html.fromstring(response)

    body.make_links_absolute('http://www.qzggzy.com/')
    etree.strip_elements(body,"script","style","title",'iframe')
    decide_element = body.xpath('//div[@class="contentall"]')
    del_eles = body.xpath('//div[@class="ewb-location"]') + body.xpath('//div[@class="ewb-detail-intro"]') + body.xpath('//div[@class="ewb-article-share"]') + body.xpath('//div[@class="ewb-detail-middle"]')
    for ele in del_eles:
        ele.clear()
    try:
        element = body.xpath('//div[@class="container"]')[0]
    except Exception as e:
        raise e
    content = etree.tostring(element,encoding='utf-8')
    #print(content.decode('utf-8'))
    data = content.decode('utf-8')
    return data