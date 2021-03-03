from lxml import etree
import lxml.html
from .. import cleaner
import re
import requests
HEADERS = {#'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI 6 Build/NMF26X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',

}

def taizhou_modifier(response,url):

    content = cleaner.clean_html(response)
    body = lxml.html.fromstring(content)
    body.make_links_absolute('http://www.tzztb.com/')
    etree.strip_elements(body,"script","style","title",'iframe')
    decide_element = body.xpath('//div[@class="Main-p floatL"]')
    try:
        if len(decide_element):
            element = body.xpath('//div[@class="Main-p floatL"]')[0]
        else:
            element = body.xpath('//div[@class="content-box"]')[0]
    except Exception as e:
        raise e

    check_table = None
    for table in element.xpath('.//table'):
        check_str = ''.join(table.xpath('.//text()'))
    
        if '下载' in check_str:
            check_table = table
        else:
            table.clear()
    
    if check_table is not None:
        cid = re.findall(r'/(\d+)\.htm',url)[0]
        n = len(check_table.xpath('.//tr')) - 1
        attachment_url = 'http://www.tzztb.com/tzcms/attachment_url.jspx?cid={}&n={}'.format(cid,n)
        #print(attachment_url)
        try:
            attachment_urls = requests.get(attachment_url,headers=HEADERS)
        except Exception as e:
            print(e)
            raise e
        i = 0
    
        for td_ele,href in zip(check_table.xpath('.//tr//td//a[@title="文件下载"]'),eval(attachment_urls.text)):
            final_href = "http://www.tzztb.com/tzcms/attachment.jspx?cid={}&i={}{}".format(cid,i,href)
            td_ele.set('href',final_href)
            i +=1
    content = etree.tostring(element,encoding='utf-8')
    #print(content.decode('utf-8'))
    data = content.decode('utf-8')
    return data