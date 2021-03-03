#中国石油电子招标投标交易平台
#
#
[
{"id":"01","area":"国网冀北电力有限公司",},
{"id":"02","area":"国网北京市电力公司",},
{"id":"03","area":"国网天津市电力公司",},
{"id":"04","area":"国网河北省电力有限公司",},
{"id":"05","area":"国网山西省电力公司",},
{"id":"06","area":"国网山东电力集团公司",},
{"id":"09","area":"国网上海市电力公司",},
{"id":"10","area":"国网江苏省电力公司",},
{"id":"11","area":"国网浙江省电力公司",},
{"id":"12","area":"国网安徽省电力公司",},
{"id":"13","area":"国网福建省电力有限公司",},
{"id":"22","area":"国网辽宁省电力有限公司",},
{"id":"23","area":"国网吉林省电力有限公司",},
{"id":"24","area":"国网黑龙江省电力有限公司",},
{"id":"07","area":"国网内蒙古东部电力有限公司",},
{"id":"26","area":"国网陕西省电力公司",},
{"id":"27","area":"国网甘肃省电力公司",},
{"id":"28","area":"国网青海省电力公司",},
{"id":"29","area":"国网宁夏电力公司",},
{"id":"30","area":"国网新疆电力有限公司",},
{"id":"31","area":"国网西藏电力有限公司",},
{"id":"15","area":"国网湖北省电力有限公司",},
{"id":"16","area":"国网湖南省电力有限公司",},
{"id":"17","area":"国网河南省电力公司",},
{"id":"18","area":"国网江西省电力有限公司",},
{"id":"19","area":"国网四川省电力公司",},
{"id":"20","area":"国网重庆市电力公司",},
{"id":"34","area":"国家电网公司交流建设分公司",},
{"id":"33","area":"国家电网公司直流建设分公司",},
{"id":"53","area":"中兴电力实业发展有限公司",},
{"id":"61","area":"英大证券有限责任公司",},
{"id":"46","area":"国网新源控股有限公司",},
{"id":"72","area":"国网通用航空有限公司",},
{"id":"41","area":"中国电力科学研究院有限公司",},
{"id":"50","area":"国家电网公司高级培训中心",},
{"id":"32","area":"国家电网公司运行分公司",},
{"id":"66","area":"英大传媒投资集团有限公司",},
{"id":"48","area":"国家电网公司信息通信分公司",},
{"id":"83","area":"国网国际发展有限公司",},
{"id":"57","area":"中国电力财务有限公司",},
{"id":"59","area":"英大泰和人寿保险股份有限公司",},
{"id":"82","area":"英大期货有限公司",},
{"id":"78","area":"全球能源互联网研究院有限公司",},
{"id":"85","area":"国网信息通信产业集团有限公司",},
{"id":"45","area":"国网经济技术研究院有限公司",},
{"id":"98","area":"国网电子商务有限公司",},
{"id":"55","area":"中国电力技术装备有限公司",},
{"id":"67","area":"英大长安保险经纪集团有限公司",},
{"id":"95","area":"国网电动汽车服务有限公司",},
{"id":"A7","area":"山西重力工程咨询有限公司",},
{"id":"42","area":"国网能源研究院",},
{"id":"94","area":"北京电力交易中心有限公司",},
{"id":"89","area":"国中康健集团有限公司",},
{"id":"79","area":"国网节能服务有限公司",},
{"id":"80","area":"鲁能集团有限公司",},
{"id":"91","area":"国网技术学院本部",},
{"id":"90","area":"国网大数据中心",},
{"id":"51","area":"国网国际融资租赁有限公司",},
{"id":"74","area":"许继集团有限公司",},
{"id":"76","area":"国家电网公司客户服务中心",},
]


#CRAWL_CNPC_TASKS = {
#    'name':'cnpc',
#    'source_url':'https://www.cnpcbidding.com/cms/pmsbidInfo/listPageOut',
#    'html_type':'static',
#    'tasks':[
#    {
#        "an_type": "招标公告",
#        "an_sub": "NONE",
#        "an_major": "NONE",
#        "an_county": "NONE",
#        "an_sub_url": "https://www.cnpcbidding.com/cms/pmsbidInfo/listPageOut",
#        "url":"./list.html",
#        "pid":"198",
#        "pageSize":15,
#        "categoryId":199,
#        "title": "",
#        "projectType":"",
#    },
#    {
#        "an_type": "资格预审公告",
#        "an_sub": "NONE",
#        "an_major": "NONE",
#        "an_county": "NONE",
#        "an_sub_url": "https://www.cnpcbidding.com/cms/pmsbidInfo/listPageOut"
#        "url":"./list.html",
#        "pid":"198",
#        "pageSize":15,
#        "categoryId":201,
#        "title": "",
#        "projectType":"",
#    },
#    {
#        "an_type": "公开招标中标候选人公示",
#        "an_sub": "NONE",
#        "an_major": "NONE",
#        "an_county": "NONE",
#        "an_sub_url": "https://www.cnpcbidding.com/cms/pmsbidInfo/listPageOut"
#        "url":"./list.html",
#        "pid":"180",
#        "pageSize":15,
#        "categoryId":181,
#        "title": "",
#        "projectType":"",
#    },
#    {
#        "an_type": "公开招标中标结果公示",
#        "an_sub": "NONE",
#        "an_major": "NONE",
#        "an_county": "NONE",
#        "an_sub_url": "https://www.cnpcbidding.com/cms/pmsbidInfo/listPageOut"
#        "url":"./list.html",
#        "pid":"180",
#        "pageSize":15,
#        "categoryId":183,
#        "title": "",
#        "projectType":"",
#    },
#
#    {
#        "an_type": "谈判采购公告",
#        "an_sub": "NONE",
#        "an_major": "NONE",
#        "an_county": "NONE",
#        "an_sub_url": "https://www.cnpcbidding.com/cms/pmsbidInfo/listPageOut"
#        "url":"./list.html",
#        "pid":"193",
#        "pageSize":15,
#        "categoryId":194,
#        "title": "",
#        "projectType":"",
#    },
#    {
#        "an_type": "询价（竞价）采购公告",
#        "an_sub": "NONE",
#        "an_major": "NONE",
#        "an_county": "NONE",
#        "an_sub_url": "https://www.cnpcbidding.com/cms/pmsbidInfo/listPageOut"
#        "url":"./list.html",
#        "pid":"193",
#        "pageSize":15,
#        "categoryId":195,
#        "title": "",
#        "projectType":"",
#    },
#
#    {
#        "an_type": "谈判采购拟成交结果公告",
#        "an_sub": "NONE",
#        "an_major": "NONE",
#        "an_county": "NONE",
#        "an_sub_url": "https://www.cnpcbidding.com/cms/pmsbidInfo/listPageOut"
#        "url":"./list.html",
#        "pid":"193",
#        "pageSize":15,
#        "categoryId":196,
#        "title": "",
#        "projectType":"",
#    },
#    {
#        "an_type": "询价（竞价）拟成交结果公告",
#        "an_sub": "NONE",
#        "an_major": "NONE",
#        "an_county": "NONE",
#        "an_sub_url": "https://www.cnpcbidding.com/cms/pmsbidInfo/listPageOut"
#        "url":"./list.html",
#        "pid":"193",
#        "pageSize":15,
#        "categoryId":197,
#        "title": "",
#        "projectType":"",
#    },
#    ]
#
#}

def main():
    return CRAWL_CNPC_TASKS

import re
data ="[国网上海市电力公司]国网上海市电力公司10kV台区智能配变终端改造（融资租赁）招标采购项目推荐的中标..." 

county = re.findall(r'\[(.*?)\]',data)[0]
print(county)

                            
                     