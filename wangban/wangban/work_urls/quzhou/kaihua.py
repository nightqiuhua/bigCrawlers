
CRAWL_KAIHUA_TASKS = {
    'name':'kaihua',
    'source_url':'',
    'task_queue':'wangban:kaihua:an_work_urls',
    'task_check':'wangban:kaihua:an_check_urls',
    'task_ajax':'wangban:kaihua:an_ajax_urls',
    'html_type':'ajax',
    'tasks':[
    {'建设工程':{
    '中标公告':{'NONE':'http://www.kaihua.gov.cn/col/col1384140/index.html?uid=4442405&pageNum=1',},
    '中标公示':{'NONE':'http://www.kaihua.gov.cn/col/col1384139/index.html?uid=4442405&pageNum=1',},
    '招标公告':{'NONE':'http://www.kaihua.gov.cn/col/col1384138/index.html?uid=4442405&pageNum=1',},
    }},
    {'政府采购':{
    '采购合同':{'NONE':'http://www.kaihua.gov.cn/col/col1384145/index.html?uid=4442405&pageNum=1',},
    '中标成交公告':{'NONE':'http://www.kaihua.gov.cn/col/col1384144/index.html?uid=4442405&pageNum=1',},
    '采购公告':{'NONE':'http://www.kaihua.gov.cn/col/col1384143/index.html?uid=4442405&pageNum=1',},
    '意见征求及公示':{'NONE':'http://www.kaihua.gov.cn/col/col1384142/index.html?uid=4442405&pageNum=1',},
    }},
    {'产权交易':{
    '交易结果公告':{'NONE':'http://www.kaihua.gov.cn/col/col1384151/index.html?uid=4442405&pageNum=1',},
    '交易结果公示':{'NONE':'http://www.kaihua.gov.cn/col/col1384150/index.html?uid=4442405&pageNum=1',},
    '交易公告':{'NONE':'http://www.kaihua.gov.cn/col/col1384149/index.html?uid=4442405&pageNum=1',},
    }},
    {'土地交易':{
    '交易结果公告':{'NONE':'http://www.kaihua.gov.cn/col/col1384153/index.html?uid=4442405&pageNum=1',},
    '交易公告':{'NONE':'http://www.kaihua.gov.cn/col/col1384152/index.html?uid=4442405&pageNum=1',},
    }},
    ]
}

def main():
    return CRAWL_KAIHUA_TASKS