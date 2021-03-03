from lxml import etree
import lxml.html
import re
from lxml import etree
from lxml.html.clean import Cleaner
from lxml.cssselect import CSSSelector
import requests
import json
import time

def hangzhou_modifier(data):
    try:
        data['text'] = data['text'].replace('iframe','p')
        data['text'] = data['text'].replace('script','style')
        body = lxml.html.fromstring(data['text'])
        element = body.xpath('//div[@class="content"]')[0]
        content = etree.tostring(element,encoding='utf-8')
        #print(content.decode('utf-8'))
        data['text'] = content.decode('utf-8')
    except Exception as e:
        raise e
    return data

if __name__ == '__main__':
    url = 'http://www.lajyzx.cn/Bulletin/BulletinBrowse.aspx?id=9888'
    HEADERS = {#'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; MI 6 Build/NMF26X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    
    }
    
    cleaner = Cleaner(page_structure=False, links=False,style=True,scripts=True)
    response = requests.get(url,headers=HEADERS)
    response.encoding='utf-8'
    time.sleep(2)
    #print(response.text)
    body = lxml.html.fromstring(response.text)
    #
    #element = element.replace('DownLoad(','').replace(')','')
    #做判断
    #杭州
    #elements = re.findall('onclick="DownLoad\((.*?)\)"',response.text)
    #del_ele = tree.xpath('//div[@class="MainTitle"]')
    #for ele in del_ele:
    #    ele.clear()
    #node_elems = tree.xpath('//div/ul/li/a[@href="javascript:void(0);"]')
    #for element,node_elem in zip(elements,node_elems):
    #    str_list = element.replace('\'','')
    #    link_str_1,link_str_2 = str_list.split(',')
    #    href = 'http://file.hzctc.cn/UService/DownLoadFile.aspx?dirtype=3&filepath={}&showName={}'.format(link_str_2,link_str_1)
    #    href = re.sub(r'\s+','',href)
    #    node_elem.set('href',href)
    #
    #element_2 = tree.xpath('//div[@class="content"]')[0]
    #tree.make_links_absolute('http://www.hzctc.cn/')
    #etree.strip_elements(tree,"script","style","title")
    #
    #for ele in tree.xpath('//a[@target="_blank"]'):
    #    print(ele)
    #    ele.set('href','http://app1.hzctc.cn/')
    ##print(etree.tostring(element_2,encoding='utf-8').decode('utf-8'))
    #content = etree.tostring(element_2,encoding='utf-8').decode('utf-8')
    #
    #data = cleaner.clean_html(content)
    #萧山
    #element_2 = body.xpath('//div[@class="Content"]')[0]
    #body.make_links_absolute('http://www.xszbjyw.com/')
    #etree.strip_elements(body,"script","style","title")
#
    #content = etree.tostring(element_2,encoding='utf-8').decode('utf-8')
    #data = cleaner.clean_html(content)

    #余杭
    #element_2 = body.xpath('//div[@class="Content"]')[0]
    #body.make_links_absolute('http://www.yhggzy.com.cn/ProArticle/')
    #etree.strip_elements(body,"script","style","title")
#
    #content = etree.tostring(element_2,encoding='utf-8').decode('utf-8')
    #data = cleaner.clean_html(content)

    #临安
    element_2 = body.xpath('//div[@class="Content"]')[0]
    body.make_links_absolute('http://www.lajyzx.cn/Bulletin/')
    etree.strip_elements(body,"script","style","title")

    content = etree.tostring(element_2,encoding='utf-8').decode('utf-8')
    data = cleaner.clean_html(content)

    #富阳
    #del_ele = body.xpath('//div[@class="MainTitle"]')
    #for ele in del_ele:
    #    ele.clear()
#
    #elements = re.findall('onclick="DownLoad\((.*?)\)"',response.text)
    #node_elems = body.xpath('//div/ul/li/a[@href="javascript:void(0);"]')
    #for element,node_elem in zip(elements,node_elems):
    #    str_list = element.replace('\'','')
    #    link_str_1,link_str_2 = str_list.split(',')
    #    href = 'http://218.108.176.14:8002/DService/UpLoadFiles/ProAfficheAccessory/{}'.format(link_str_2)
    #    href = re.sub(r'\s+','',href)
    #    node_elem.set('href',href)
#
    #body.make_links_absolute('http://www.hzfyggzy.org.cn/')
    #etree.strip_elements(body,"script","title")
    #for ele in body.xpath('//a[@target="_blank"]'):
    #    print(ele)
    #    ele.set('title','投标人平台用户请登录投标人平台下载，其他用户请到交易中心窗口领取')
#
    #try:
    #    element_2 = body.xpath('//div[@class="content"]')[0]
    #    content = etree.tostring(element_2,encoding='utf-8').decode('utf-8')
    #    #print(content.decode('utf-8'))
    #    data = cleaner.clean_html(content)
    #    #data = re.sub(r'\s+','',data)
    #except Exception as e:
    #    raise e
    print(data)
    
    

