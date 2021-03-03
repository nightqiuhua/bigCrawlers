

CRAWL_CHANGSHAN_TASKS = {
    'name':'changshan',
    'source_url':'',
    'task_queue':'wangban:changshan:an_work_urls',
    'task_check':'wangban:changshan:an_check_urls',
    'task_ajax':'wangban:changshan:an_ajax_urls',
    'html_type':'ajax',
    'tasks':[
    {'建设工程':{
    '招标公告':{'NONE':'http://qzcs.zjzwfw.gov.cn/col/col1341164/index.html',},
    '中标公告':{'NONE':'http://qzcs.zjzwfw.gov.cn/col/col1341165/index.html',},
    }},
    {'政府采购':{
    '采购公告':{'NONE':'http://qzcs.zjzwfw.gov.cn/col/col1341159/index.html',},
    '中标公告':{'NONE':'http://qzcs.zjzwfw.gov.cn/col/col1341161/index.html',},
    }},
    {'综合交易':{
    '交易公告':{'NONE':'http://qzcs.zjzwfw.gov.cn/col/col1341172/index.html',},
    '成交结果':{'NONE':'http://qzcs.zjzwfw.gov.cn/col/col1341173/index.html',},
    }},
    {'土地产权':{
    '拍卖公告':{'NONE':'http://qzcs.zjzwfw.gov.cn/col/col1341170/index.html',},
    '成交结果':{'NONE':'http://qzcs.zjzwfw.gov.cn/col/col1341171/index.html',},
    }},
    {'乡镇（部门）平台':{
    '交易公告':{'NONE':'http://qzcs.zjzwfw.gov.cn/col/col1341176/index.html',},
    '中标公告':{'NONE':'http://qzcs.zjzwfw.gov.cn/col/col1341177/index.html',},
    }},
    {'其他交易':{
    '交易公告':{'NONE':'http://qzcs.zjzwfw.gov.cn/col/col1341178/index.html',},
    '中标公告':{'NONE':'http://qzcs.zjzwfw.gov.cn/col/col1341179/index.html',},
    }}
    ]
}

def main():
    return CRAWL_CHANGSHAN_TASKS