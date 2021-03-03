from lxml import etree
import lxml.html
from .. import cleaner


def zhejiang_modifier(response):
    content = cleaner.clean_html(response)
    body = lxml.html.fromstring(content)
    try:
        body.make_links_absolute('http://new.zmctc.com/')
        etree.strip_elements(body,"script","style","title")
        decide_element = body.xpath('//table[@class="tab"]')
        if len(decide_element):
            element = body.xpath('//table[@class="tab"]')[0]
        else:
            element = body.xpath('//td[@id="TDContent"]')[0]
    except Exception as e:
        raise e
    data = etree.tostring(element,encoding='utf-8').decode('utf-8')
    return data

