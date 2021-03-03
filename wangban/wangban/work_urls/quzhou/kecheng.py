
CRAWL_KECHENG_TASKS = {
    'name':'kecheng',
    'source_url':'',
    'task_queue':'wangban:kecheng:an_work_urls',
    'task_check':'wangban:kecheng:an_check_urls',
    'task_ajax':'wangban:kecheng:an_ajax_urls',
    'html_type':'ajax',
    'tasks':[
    {'建设工程':{
    '招标公告':{'NONE':'http://www.kecheng.gov.cn/col/col1577791/index.html',},
    '中标公示':{'NONE':'http://www.kecheng.gov.cn/col/col1577793/index.html',},
    '直接发包':{'NONE':'http://www.kecheng.gov.cn/col/col1577794/index.html',},
    }},
    {'政府采购':{
    '采购公告':{'NONE':'http://www.kecheng.gov.cn/col/col1577782/index.html',},
    '成交公示':{'NONE':'http://www.kecheng.gov.cn/col/col1577784/index.html',},
    '其他公告':{'NONE':'http://www.kecheng.gov.cn/col/col1577786/index.html',},
    }},
    {'土地、矿业权出让':{
    '供地计划':{'NONE':'http://www.kecheng.gov.cn/col/col1577772/index.html',},
    '出让公告':{'NONE':'http://www.kecheng.gov.cn/col/col1577773/index.html',},
    '结果公示':{'NONE':'http://www.kecheng.gov.cn/col/col1577774/index.html',},
    }},
    ]
}

def main():
    return CRAWL_KECHENG_TASKS