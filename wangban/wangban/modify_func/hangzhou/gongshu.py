from lxml import etree
import lxml.html
import re
#class="page-content"
def gongshu_modifier(response):
    body = lxml.html.fromstring(response)
    etree.strip_elements(body,"script","style","title",'iframe')
    del_ele = body.xpath('//div[@class="bread-panel"]')
    for ele in del_ele:
        ele.clear()
    elements = re.findall('onclick="downFile\((.*?)\);"',response)
    node_elems = body.xpath('//td[@id="rsmegWechatpicpath"]/a[@href="javascript:;"]')
    for element,node_elem in zip(elements,node_elems):
        str_list = element.replace('\'','')
        link_str_1,link_str_2 = str_list.split(',')
        href = link_str_1.replace('&quot;','')
        href = re.sub(r'\s+','',href)
        node_elem.set('href',href)
    try:

        decide_element_3 = body.xpath('//div[@class="MainList"]')
        decide_element_1 = body.xpath('//div[@class="page-content"]')
        decide_element_2 = body.xpath('//div[@class="Section0"]')
        if len(decide_element_1):
            element = decide_element_1[0]
        elif len(decide_element_2):
            element = decide_element_2[0]
        elif len(decide_element_3):
            element = decide_element_3[0]
        else:
            element = body.xpath('//div[@class="detail-content"]')[0]
        #//div[@class="Section0"]

    except Exception as e:
        raise e
    content = etree.tostring(element,encoding='utf-8')
    #print(content.decode('utf-8'))
    data = content.decode('utf-8')
    return data