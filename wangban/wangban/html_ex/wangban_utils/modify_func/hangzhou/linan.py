from lxml import etree
import lxml.html

def linan_modifier(data):
    try:
        data['TEXT'] = data['TEXT'].replace('iframe','p')
        data['TEXT'] = data['TEXT'].replace('script','tbody')
        body = lxml.html.fromstring(data['TEXT'])
        decide_element_2 = body.xpath('//div[@class="AfficheContent"]')
        decide_element_1 = body.xpath('//div[@class="Section0"]')
        #//div[@class="Section0"]
        if len(decide_element_1):
            element = body.xpath('//div[@class="Section0"]')[0]
        elif len(decide_element_2):
            element = body.xpath('//div[@class="AfficheContent"]')[0]
        else:
            element = body.xpath('//div[@class="Content"]')[0]
        content = etree.tostring(element,encoding='utf-8')
        #print(content.decode('utf-8'))
        data['TEXT'] = content.decode('utf-8')
    except Exception as e:
        raise e
    return data