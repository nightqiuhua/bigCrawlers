import lxml.html
import re
import requests
from lxml import etree
HEADERS = {#'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI 6 Build/NMF26X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',

}

def longwan_modifier(response,url):
    body = lxml.html.fromstring(response)
    body.make_links_absolute('http://61.164.128.8:6081/')
    etree.strip_elements(body,"script","style","title",'iframe')

    try:
        element = body.xpath('//div[@class="Content-Main FloatL"]')[0]
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
        attachment_url = 'http://61.164.128.8:6081/lwcms/attachment_url.jspx?cid={}&n={}'.format(cid,n)
        try:
            attachment_urls = requests.get(attachment_url,headers=HEADERS)
        except Exception as e:
            raise e
        #print(type(attachment_urls.text))
        i = 0
    
        for td_ele,href in zip(check_table.xpath('.//tr//td//a[@title="文件下载"]'),eval(attachment_urls.text)):
            final_href = "http://61.164.128.8:6081/lwcms/attachment.jspx?cid={}&i={}{}".format(cid,i,href)
            td_ele.set('href',final_href)
            i +=1
    content = etree.tostring(element,encoding='utf-8')
    #print(content.decode('utf-8'))
    data = content.decode('utf-8')
    return data