from lxml import etree
import lxml.html
from .. import cleaner

def zhejiangjt_modifier(response):
    content = cleaner.clean_html(response)
    body = lxml.html.fromstring(content)
    try:
        body.make_links_absolute('http://jtyst.zj.gov.cn/')
        etree.strip_elements(body,"script","style","title")
        element = body.xpath('//div[@id="zoom"]')[0]
        #print(content.decode('utf-8'))
    except Exception as e:
        raise e
    data = etree.tostring(element,encoding='utf-8').decode('utf-8')
    return data