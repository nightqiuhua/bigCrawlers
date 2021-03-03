
#可以用
CRAWL_NINGHAI_AJAX_TASKS = {
    'name':'ninghai_ajax',
    'source_url':'',
    'task_queue':'wangban:ninghai_ajax:an_work_urls',
    'task_check':'wangban:ninghai_ajax:an_url_check',
    'task_ajax':'wangban:ninghai_ajax:an_url_ajax',
    'html_type':'ajax',
    'tasks':[
    {
        "an_sub": "NONE",
        "an_major": "农村产权",
        "an_type": "补充公告",
        "an_sub_url": "http://www.nhztb.gov.cn:8030/jmr/jump?num=8"
    },
    {
        "an_sub": "NONE",
        "an_major": "农村产权",
        "an_type": "挂牌信息",
        "an_sub_url": "http://www.nhztb.gov.cn:8030/jmr/jump?num=3"
    },
    {
        "an_sub": "NONE",
        "an_major": "农村产权",
        "an_type": "结果公示",
        "an_sub_url": "http://www.nhztb.gov.cn:8030/jmr/jump?num=4"
    },
    {
        "an_sub": "NONE",
        "an_major": "农村产权",
        "an_type": "出让公告",
        "an_sub_url": "http://www.nhztb.gov.cn:8030/jmr/jump?num=2"
    }
]
}

def main():
    return CRAWL_NINGHAI_AJAX_TASKS