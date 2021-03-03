from lxml import etree
import lxml.html
import re

def fuyang_modifier(response):
    body = lxml.html.fromstring(response)
    body.make_links_absolute('http://www.hzfyggzy.org.cn/')
    etree.strip_elements(body,"script","style","title",'iframe')
    del_ele = body.xpath('//div[@class="MainTitle"]')
    for ele in del_ele:
        ele.clear()
    elements = re.findall('onclick="DownLoad\((.*?)\)"',response)
    node_elems = body.xpath('//div/ul/li/a[@href="javascript:void(0);"]')
    for element,node_elem in zip(elements,node_elems):
        str_list = element.replace('\'','')
        link_str_1,link_str_2 = str_list.split(',')
        href = 'http://218.108.176.14:8002/DService/UpLoadFiles/ProAfficheAccessory/{}'.format(link_str_2)
        href = re.sub(r'\s+','',href)
        node_elem.set('href',href)
    for ele in body.xpath('//a[@target="_blank"]'):
        ele.set('title','投标人平台用户请登录投标人平台下载，其他用户请到交易中心窗口领取')
    try:
        element = body.xpath('//div[@class="content"]')[0]
    except Exception as e:
        raise e
    content = etree.tostring(element,encoding='utf-8')
    #print(content.decode('utf-8'))
    data = content.decode('utf-8')
    return data