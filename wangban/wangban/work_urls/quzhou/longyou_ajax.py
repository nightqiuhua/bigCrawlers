

CRAWL_LONGYOU_AJAX_TASKS = {
    'name':'longyou_ajax',
    'source_url':'',
    'task_queue':'wangban:longyou_ajax:an_work_urls',
    'task_check':'wangban:longyou_ajax:an_check_urls',
    'task_ajax':'wangban:longyou_ajax:an_ajax_urls',
    'html_type':'ajax',
    'tasks':[
    {'电子竞价平台':{
    '产权交易公告':{'NONE':'http://bid.lyxztb.com:8080/global_globalLaunchProjectList.do?pageSize=25&storetype=2',},
    '产权交易结果':{'NONE':'http://bid.lyxztb.com:8080/global_globalResultProjectList.do?pageSize=25&storetype=2',},
    }},
    ]
}

def main():
    return CRAWL_LONGYOU_AJAX_TASKS