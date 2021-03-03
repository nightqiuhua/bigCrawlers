#encoding:utf-8 
import re
import lxml.html
from lxml import etree

data = {
'class_2': '水泥、砖瓦灰砂石及混凝土制品', 
'mt_html': '<div class="details-left-one">\n        <div class="big-material-img">\n\t\t\t\n\t\t\t\t<span><img src="/resources/images/common/nothing_img_two.png"></span>\n\t\t\t\t\n\t\t\t\n\t\t</div>\n        <div class="big-material-mian">\n        \t<div class="big-material-mian-a clearfix"><p>立柜式空调器</p></div>\n            <div class="big-material-mian-block">\n                <ul class="big-mian-block-left">\n                    <li><i class="enquiry-sprite-bg balance-frame"></i><b>规格|需求量：</b>SGT-20 | 4台</li>\n                    <li><i class="enquiry-sprite-bg issue-time"></i><b>发布时间：</b>2015-03-31</li>\n                    <li><i class="enquiry-sprite-bg issue-location"></i><b>报价地区：</b>上海 上海市</li>\n                    \n            \n\t\t\t\t\n\t\t\t\t\n\t\t\t\t\t<li><i class="enquiry-sprite-bg gys-price"></i><b>报 价 数 ：</b><span class="cr-f60" href="#">4</span>个供应商报价</li>\n\t\t\t\t\n\t\t\t\n                    \n                    <li><i class="enquiry-sprite-bg material-grade"></i><b>档次品牌：</b>中档 | 新晃</li>\n                    <li><i class="enquiry-sprite-bg other-price"></i><b>费用说明：</b>不含税费 | 不含运费</li>                  \n                    \n                </ul>\n            </div>\n            \n        </div>\n    </div><ul class="details-left-two">\n   \t\t\n\t\t\t\n\t\t\t\n\t\t\t\t\n\t\t\t        <li>\n\t\t\t        \t<span class="gys-baojia"></span>\n\t\t\t        \t<i class="gys-number" style="background-position: 0px 0px;"></i>\n\t\t\t        \t<div class="details-small-tit">\n\t\t\t            \t<span>供应商：</span><a bicode="Zjt-xunjia-info-c3" href="https://gys.zjtcn.com/gys/c_t_p1_k广东吉荣空调有限公司深圳办事处_b_qi.html" target="_blank">广东吉荣空调有限公司深圳办事处</a>\n\t\t\t            </div>\n\t\t\t            <ul class="details-small-box">\n\t\t\t            \t<li><i>材料品牌：</i><span>吉荣</span></li>\n\t\t\t                <li><i>材料单位：</i><span>台</span></li>\n\t\t\t                <li><i>材料报价：</i><span>\n\t\t\t\t\t\t\t\t \n\t\t\t\t\t\t\t\t\t <em class="cr-f60 details-price">19733.00</em> 元/台\n\t\t\t\t\t\t\t\t\t \n\t\t\t\t\t\t\t\t \n\t\t\t\t\t\t\t</span></li>\n\t\t\t                <li><i>\u3000联系人：</i><span>罗先生</span></li>\n\t\t\t                <li><i>联系方式：</i><span>\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t                \n\t\t\t\t\t\t\t\t0755-82947505   15875552057\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t</span></li>\n\t\t\t                <li><i>报价时间：</i><span>2015-03-31</span></li>\n\t\t\t                <li><i>费用说明：</i><span>不含税费、\n\t\t\t                不含运费</span></li>\n\t\t\t                <li><i>备注说明：</i><span title="此为立柜式空调器风量:15000cmH 余压:500Pa风机功率:5.5KW广东深圳市的价格">此为立柜式空调器风量:15000cmH 余压:500Pa风机功率:5.5KW广东深圳市的价格</span></li>\n\t\t\t            </ul>\n\t\t\t        </li>\n\t\t        \n\t\t\t        <li>\n\t\t\t        \t<span class="gys-baojia"></span>\n\t\t\t        \t<i class="gys-number" style="background-position: 0px -48px;"></i>\n\t\t\t        \t<div class="details-small-tit">\n\t\t\t            \t<span>供应商：</span><a bicode="Zjt-xunjia-info-c3" href="https://gys.zjtcn.com/gys/c_t_p1_k广东吉荣空调有限公司深圳办事处_b_qi.html" target="_blank">广东吉荣空调有限公司深圳办事处</a>\n\t\t\t            </div>\n\t\t\t            <ul class="details-small-box">\n\t\t\t            \t<li><i>材料品牌：</i><span>吉荣</span></li>\n\t\t\t                <li><i>材料单位：</i><span>台</span></li>\n\t\t\t                <li><i>材料报价：</i><span>\n\t\t\t\t\t\t\t\t \n\t\t\t\t\t\t\t\t\t <em class="cr-f60 details-price">29560.00</em> 元/台\n\t\t\t\t\t\t\t\t\t \n\t\t\t\t\t\t\t\t \n\t\t\t\t\t\t\t</span></li>\n\t\t\t                <li><i>\u3000联系人：</i><span>罗先生</span></li>\n\t\t\t                <li><i>联系方式：</i><span>\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t                \n\t\t\t\t\t\t\t\t0755-82947505   15875552057\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t</span></li>\n\t\t\t                <li><i>报价时间：</i><span>2015-03-31</span></li>\n\t\t\t                <li><i>费用说明：</i><span>不含税费、\n\t\t\t                不含运费</span></li>\n\t\t\t                <li><i>备注说明：</i><span title="此为立柜式空调器风量:25000cmH 余压:300Pa风机功率:11KW广东深圳市的价格">此为立柜式空调器风量:25000cmH 余压:300Pa风机功率:11KW广东深圳市的价格</span></li>\n\t\t\t            </ul>\n\t\t\t        </li>\n\t\t        \n\t\t\t        <li>\n\t\t\t        \t<span class="gys-baojia"></span>\n\t\t\t        \t<i class="gys-number" style="background-position: 0px -96px;"></i>\n\t\t\t        \t<div class="details-small-tit">\n\t\t\t            \t<span>供应商：</span><a bicode="Zjt-xunjia-info-c3" href="https://gys.zjtcn.com/gys/c_t_p1_k上海新晃空调设备有限公司_b_qi.html" target="_blank">上海新晃空调设备有限公司</a>\n\t\t\t            </div>\n\t\t\t            <ul class="details-small-box">\n\t\t\t            \t<li><i>材料品牌：</i><span>新晃</span></li>\n\t\t\t                <li><i>材料单位：</i><span>台</span></li>\n\t\t\t                <li><i>材料报价：</i><span>\n\t\t\t\t\t\t\t\t \n\t\t\t\t\t\t\t\t\t <em class="cr-f60 details-price">42858.34</em> 元/台\n\t\t\t\t\t\t\t\t\t \n\t\t\t\t\t\t\t\t \n\t\t\t\t\t\t\t</span></li>\n\t\t\t                <li><i>\u3000联系人：</i><span>陈敏</span></li>\n\t\t\t                <li><i>联系方式：</i><span>\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t                \n\t\t\t\t\t\t\t\t021-54880982   13609765274\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t</span></li>\n\t\t\t                <li><i>报价时间：</i><span>2015-03-31</span></li>\n\t\t\t                <li><i>费用说明：</i><span>不含税费、\n\t\t\t                不含运费</span></li>\n\t\t\t                <li><i>备注说明：</i><span title="-">-</span></li>\n\t\t\t            </ul>\n\t\t\t        </li>\n\t\t        \n\t\t\t        <li>\n\t\t\t        \t<span class="gys-baojia"></span>\n\t\t\t        \t<i class="gys-number" style="background-position: 0px -144px;"></i>\n\t\t\t        \t<div class="details-small-tit">\n\t\t\t            \t<span>供应商：</span><a bicode="Zjt-xunjia-info-c3" href="https://gys.zjtcn.com/gys/c_t_p1_k广东吉荣空调有限公司深圳办事处_b_qi.html" target="_blank">广东吉荣空调有限公司深圳办事处</a>\n\t\t\t            </div>\n\t\t\t            <ul class="details-small-box">\n\t\t\t            \t<li><i>材料品牌：</i><span>吉荣</span></li>\n\t\t\t                <li><i>材料单位：</i><span>台</span></li>\n\t\t\t                <li><i>材料报价：</i><span>\n\t\t\t\t\t\t\t\t \n\t\t\t\t\t\t\t\t\t <em class="cr-f60 details-price">14667.00</em> 元/台\n\t\t\t\t\t\t\t\t\t \n\t\t\t\t\t\t\t\t \n\t\t\t\t\t\t\t</span></li>\n\t\t\t                <li><i>\u3000联系人：</i><span>罗先生</span></li>\n\t\t\t                <li><i>联系方式：</i><span>\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t                \n\t\t\t\t\t\t\t\t0755-82947505   15875552057\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t</span></li>\n\t\t\t                <li><i>报价时间：</i><span>2015-03-31</span></li>\n\t\t\t                <li><i>费用说明：</i><span>不含税费、\n\t\t\t                不含运费</span></li>\n\t\t\t                <li><i>备注说明：</i><span title="此为立柜式空调器风量:22000cmH 余压:350Pa风机功率:7.5KW广东深圳市的价格">此为立柜式空调器风量:22000cmH 余压:350Pa风机功率:7.5KW广东深圳市的价格</span></li>\n\t\t\t            </ul>\n\t\t\t        </li>\n\t\t        \n\t\t\t\n\t\t\n    </ul>', 
'is_cl': 0, 
'class_1': '土建', 
'ID': 85615, 
'class_3': '石子', 
'gettime': '2019-04-06 23:45:21', 
'mt_name': '黄色水泥洗黄色瓜米石', 
'_id': 85615, 
'province': '广东', 
'link': 'https://xunjia.zjtcn.com/askInfo/91414.html', 
'city': '中山市', 
'pubdate': '2012-03-21'}

#print(data['mt_html'])
pre_data_map = {
    '规格|需求量':'CL干法施工砖砌体砌筑砂浆用 | 3000kg',
    '发布时间':'2011-09-22',
    '报价数':'1',
    '档次品牌':'-',
    '材料品牌':'-',
    '材料单位':'kg',
    '材料报价':'18.10元/kg',
    '联系人':'-',
    '联系方式':'-',
    '报价时间':'2011-09-23',
    '费用说明':'不含税费、不含运费',
    '备注说明':'广州双普贸易有限公司 您好，以上价格仅供您参考，谢谢！ 020 22130599',
    '供应商':'广州双普贸易有限公司'
}


field_map= {
    '规格|需求量':'specification',
    '发布时间':'pubdate',
    '报价数':'reply_count',
    '档次品牌':'grade',
    '材料品牌':'mt_brand',
    '材料单位':'mt_unit',
    '材料报价':'mt_price',
    '联系人':'contact',
    '联系方式':'contact_phone',
    '报价时间':'reply_time',
    '费用说明':'fee_notice',
    '备注说明':'notice',
    '供应商':'supplier'

}
after_data = {
    'specification':'CL干法施工砖砌体砌筑砂浆用 | 3000kg',
    'pubdate':'2011-09-22',
    'reply_count':'1',
    'grade':'-',
    'mt_brand':'-',
    'mt_unit':'kg',
    'mt_price':'18.10元/kg',
    'contact':'-',
    'contact_phone':'-',
    'reply_time':'2011-09-23',
    'fee_notice':'不含税费、不含运费',
    'notice':'广州双普贸易有限公司 您好，以上价格仅供您参考，谢谢！ 020 22130599',
    'supplier':'广州双普贸易有限公司'

}


#result_dict = {}
#
tree  = lxml.html.fromstring(data['mt_html'])



head_info = {}


pd_elems = tree.xpath('//ul[@class="big-mian-block-left"]/li')

for elem in pd_elems:
    result = elem.xpath('.//text()')
    #print(result[0],result[1:])
    key = re.sub(r'\s+','',result[0])
    key = key.replace('：','')

    value  = ''.join(result[1:])
    if value == ' ':
        value = '-'
    if key == '报价数':
        try:
            value = re.findall(r'\d+',value)[0]
        except Exception as e:
            raise e
    if key == '费用说明':
        continue
    head_info[key] = value

for index in ['ID','_id','link','mt_html']:
    data.pop(index)
print(data)
#
#
sp_elems = tree.xpath('//ul[@class="details-left-two"]/li')

for elem in sp_elems:
    mt_info = {}
    #print(elem.xpath('./i/text()')[0],elem.xpath('./span//text()'))
    mt_info['供应商'] = elem.xpath('./div[@class="details-small-tit"]//a/text()')[0]
    for sub_elem in elem.xpath('.//ul[@class="details-small-box"]/li'):
        key = sub_elem.xpath('./i/text()')[0]
        key = key.replace('：','')
        key = re.sub(r'\s+','',key)
        value = ''.join(sub_elem.xpath('./span//text()'))
        value = re.sub('\s+',' ',value)
        if value ==' ':
            value ='-'
        mt_info[key] = value
    mt_info.update(head_info)
    af_data = {}
    for key,value in field_map.items():
        af_data[value] = mt_info[key]
    af_data.update(data)
    print(af_data)