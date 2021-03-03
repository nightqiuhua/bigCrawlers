
CRAWL_ZJZFSJ_TASKS = {
    #浙江审计
    'name':'zhejiangsj',
    'source_url':'',
    'task_queue':'wangban:zhejiangsj:an_work_urls',
    'task_check':'wangban:zhejiangsj:an_check_urls',
    'html_type':'ajax',
    'tasks':[
    {
        "an_county": "NONE",
        "an_major": "重点事项",
        "an_sub": "NONE",
        "an_type": "审前公告",
        "an_sub_url": "http://sjt.zj.gov.cn/col/col1320655/index.html"
    },
    {
        "an_county": "NONE",
        "an_major": "重点事项",
        "an_sub": "NONE",
        "an_type": "审计结果公告",
        "an_sub_url": "http://sjt.zj.gov.cn/col/col1320656/index.html"
    }
]
}

def main():
    return CRAWL_ZJZFSJ_TASKS