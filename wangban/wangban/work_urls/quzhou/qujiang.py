
CRAWL_QUJIANG_TASKS = {
    'name':'qujiang',
    'source_url':'',
    'task_queue':'wangban:qujiang:an_work_urls',
    'task_check':'wangban:qujiang:an_check_urls',
    'html_type':'static',
    'tasks':[
    {'建设工程':{
    '招标公告':{'NONE':'http://www.qjggzy.com/qjsite/qjq1/index.htm',},
    '中标公示':{'NONE':'http://www.qjggzy.com/qjsite/qjq2/index.htm',},
    '交易结果':{'NONE':'http://www.qjggzy.com/qjsite/qjq3/index.htm',},
    '答疑澄清':{'NONE':'http://www.qjggzy.com/qjsite/qjq4/index.htm',},
    }},
    {'政府采购':{
    '招标公告':{'NONE':'http://www.qjggzy.com/qjsite/zfcg1/index.htm',},
    '中标公示':{'NONE':'http://www.qjggzy.com/qjsite/zfcg2/index.htm',},
    '交易结果':{'NONE':'http://www.qjggzy.com/qjsite/zfcg3/index.htm',},
    '答疑澄清':{'NONE':'http://www.qjggzy.com/qjsite/zfcg4/index.htm',},
    }},
    ]
}

def main():
    return CRAWL_QUJIANG_TASKS