

CRAWL_YUHUAN_AJAX_TASKS = {
    'name':'yuhuan_ajax',
    'source_url':'',
    'task_queue':'wangban:yuhuan_ajax:an_work_urls',
    'task_check':'wangban:yuhuan_ajax:an_check_urls',
    'task_ajax':'wangban:yuhuan_ajax:an_url_ajax',
    'html_type':'ajax',
    'tasks':[
    {'国有产权交易':{
    '交易指南':{'NONE':'http://www.yhjyzx.com:8070/jmr/index',},
    '出让公告':{'NONE':'http://www.yhjyzx.com:8070/jmr/jump?num=2',},
    '挂牌信息':{'NONE':'http://www.yhjyzx.com:8070/jmr/jump?num=3',},
    '结果公示':{'NONE':'http://www.yhjyzx.com:8070/jmr/jump?num=4',},
    '保证金退款':{'NONE':'http://www.yhjyzx.com:8070/jmr/jump?num=7',},
    '履约公告':{'NONE':'http://www.yhjyzx.com:8070/jmr/jump?num=9',},
    }},
    ]
}

def main():
    return CRAWL_YUHUAN_AJAX_TASKS