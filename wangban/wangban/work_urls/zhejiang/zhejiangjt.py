
CRAWL_ZJZFJT_TASKS = {
    #浙江交通
    'name':'zhejiangjt',
    'source_url':'',
    'task_queue':'wangban:zhejiangjt:an_work_urls',
    'task_check':'wangban:zhejiangjt:an_check_urls',
    'html_type':'ajax',
    'tasks':[
    {
        "an_county": "NONE",
        "an_major": "政府采购",
        "an_sub": "NONE",
        "an_type": "结果公示",
        "an_sub_url": "http://jtyst.zj.gov.cn/col/col1676906/index.html"
    },
    {
        "an_county": "NONE",
        "an_major": "政府采购",
        "an_sub": "NONE",
        "an_type": "招标公告",
        "an_sub_url": "http://jtyst.zj.gov.cn/col/col1676905/index.html"
    }
]
}

def main():
    return CRAWL_ZJZFJT_TASKS