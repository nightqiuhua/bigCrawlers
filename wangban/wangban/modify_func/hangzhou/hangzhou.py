from lxml import etree
import lxml.html
from .. import cleaner
import re

def hangzhou_modifier(response):
    body = lxml.html.fromstring(response)

    del_ele = body.xpath('//div[@class="MainTitle"]')
    for ele in del_ele:
        ele.clear()

    elements = re.findall('onclick="DownLoad\((.*?)\)"',response)
    node_elems = body.xpath('//div/ul/li/a[@href="javascript:void(0);"]')
    for element,node_elem in zip(elements,node_elems):
        str_list = element.replace('\'','')
        link_str_1,link_str_2 = str_list.split(',')
        href = 'http://file.hzctc.cn/UService/DownLoadFile.aspx?dirtype=3&filepath={}&showName={}'.format(link_str_2,link_str_1)
        href = re.sub(r'\s+','',href)
        node_elem.set('href',href)

    body.make_links_absolute('http://www.hzctc.cn/')
    etree.strip_elements(body,"script","style","title")
    for ele in body.xpath('//a[@target="_blank"]'):
        ele.set('href','http://app1.hzctc.cn/')

    try:
        element_2 = body.xpath('//div[@class="content"]')[0]
        content = etree.tostring(element_2,encoding='utf-8').decode('utf-8')
        #print(content.decode('utf-8'))
        data = cleaner.clean_html(content)
    except Exception as e:
        raise e
    #print(data)

    return data