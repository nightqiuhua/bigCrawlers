

CRAWL_LINHAI_TASKS = {
    'name':'linhai',
    'source_url':'http://www.lhztb.gov.cn/',
    'task_queue':'wangban:linhai:an_work_urls',
    'task_check':'wangban:linhai:an_check_urls',
    'html_type':'ajax',
    'tasks':[
    {'工程建设':{
    '招标公告':{
         'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=01&BulletinTypeId=11',
         },
    '澄清或修改':{
         'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=01&BulletinTypeId=13',
         },
    '开标结果':{
         'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=01&BulletinTypeId=16',
         },
    '中标候选人公示':{
         'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=01&BulletinTypeId=12',
         },
    '中标结果':{
         'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=01&BulletinTypeId=15',
         },
    '合同公告':{
         'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=01&BulletinTypeId=17',
         },
    '履约公告':{
         'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=01&BulletinTypeId=14',
         },
    }},
    {'政府采购':{
    '征询意见':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=02&BulletinTypeId=28',},
    '采购公告':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=02&BulletinTypeId=21',},
    '澄清或修改':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=02&BulletinTypeId=23',},
    '开标结果':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=02&BulletinTypeId=26',},
    '预成交公示':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=02&BulletinTypeId=22',},
    '采购成交公告':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=02&BulletinTypeId=25',},
    '履约公告':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=02&BulletinTypeId=24',},
    '合同公告':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=02&BulletinTypeId=27',},
    }},
    {'土地交易':{
    '出让公告':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=03&BulletinTypeId=31',},
    '成交公告':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=03&BulletinTypeId=32',},
    '补充通知':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=03&BulletinTypeId=33',},
    }},
    {'产权交易':{
    '信息披露':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=04&BulletinTypeId=41',},
    '澄清或修改':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=04&BulletinTypeId=43',},
    '履约验收公告':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=04&BulletinTypeId=44',},
    '成交公告':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=04&BulletinTypeId=42',},
    }},
    {'拓展资源交易':{
    '招、拍、挂公告':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=08&BulletinTypeId=81',},
    '澄清或修改':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=08&BulletinTypeId=83',},
    '履约验收公告':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=08&BulletinTypeId=84',},
    '成交公告':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=08&BulletinTypeId=82',},
    }},
    {'自行招标':{
    '交易公告':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=05&BulletinTypeId=51',},
    '预中标公示':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=05&BulletinTypeId=52',},
    '澄清或修改':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=05&BulletinTypeId=53',},
    '中标结果':{'NONE':'http://www.lhztb.gov.cn/dahai/Bulltinmore1.aspx?PrjTypeId=05&BulletinTypeId=55',},
    }}
    ]
}

def main():
    return CRAWL_LINHAI_TASKS