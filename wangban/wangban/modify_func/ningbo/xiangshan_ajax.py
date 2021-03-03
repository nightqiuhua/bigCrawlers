from lxml import etree
import lxml.html

def xiangshan_ajax_modifier(response):
    try:
        response = response.replace('iframe','p')
        body = lxml.html.fromstring(response)
        #element = body.xpath('//div[@class="de_p"]')[0]
        decide_element = body.xpath('//span[@id="ctl00_ContentPlaceHolder3_lblNoticeContent"]')
        if len(decide_element):
            element = body.xpath('//span[@id="ctl00_ContentPlaceHolder3_lblNoticeContent"]')[0]
        else:
            element = body.xpath('//table[@width="820"]//div')[0]
        content = etree.tostring(element,encoding='utf-8')
        data = content.decode('utf-8')
    except Exception as e:
        raise e
    return data