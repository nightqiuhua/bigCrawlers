from lxml import etree
import lxml.html
import re
from lxml import etree
from lxml.html.clean import Cleaner
from lxml.cssselect import CSSSelector
import requests
import json
import time

def zhejiang_modifier(data):
    pass
#    try:
#        data['text'] = data['text'].replace('iframe','p')
#        data['text'] = data['text'].replace('script','style')
#        body = lxml.html.fromstring(data['text'])
#        
#        decide_element = body.xpath('//table[@class="tab"]')
#        if len(decide_element):
#            element = body.xpath('//table[@class="tab"]')[0]
#        else:
#            element = body.xpath('//td[@id="TDContent"]')[0]
#        content = etree.tostring(element,encoding='utf-8')
#        #print(content.decode('utf-8'))
#        data['text'] = content.decode('utf-8')
#    except Exception as e:
#        raise e
#    return data



#
#}


if __name__ == '__main__':
    url = 'http://sjt.zj.gov.cn/art/2015/11/3/art_1320656_9667456.html'
    HEADERS = {#'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI 6 Build/NMF26X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}
    cleaner = Cleaner(page_structure=False, links=False,style=True,scripts=True)
    response = requests.get(url,headers=HEADERS)
    response.encoding='utf-8'
    time.sleep(2)
    #print(response.text)
    #
    data = cleaner.clean_html(response.text)
    tree = lxml.html.fromstring(data)
    #浙江
    #tree.make_links_absolute('http://new.zmctc.com/')
    #etree.strip_elements(tree,"script","style","title")
    #
    #element = tree.xpath('//table[@id="tblInfo"]')[0]
    #print(etree.tostring(element,encoding='utf-8').decode('utf-8'))
    #浙江交通
    tree.make_links_absolute('http://sjt.zj.gov.cn/')
    #etree.strip_elements(tree,"script","style","title")
    #
    element = tree.xpath('//body')[0]
    #print(element.text_content())
    print(etree.tostring(element,encoding='utf-8').decode('utf-8'))
    