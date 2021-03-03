

CRAWL_XIHUQU_TASKS = {
    'name':'xihuqu',
    'source_url':'http://www.jdggzy.com/index.aspx',
    'task_queue':'wangban:xihuqu:an_url_works',
    'task_ajax':'wangban:xihuqu:an_url_ajax',
    'task_check':'wangban:xihuqu:an_url_check',
    'html_type':'ajax',
    'tasks':[
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.hzxh.gov.cn/col/col1178004/index.html?uid=4554067&pageNum=1",
        "an_sub": "NONE",
        "an_type": "中标公示 "
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.hzxh.gov.cn/col/col1178003/index.html?uid=4554067&pageNum=1",
        "an_sub": "NONE",
        "an_type": "招标公告 "
    }
]
}

def main():
    return CRAWL_XIHUQU_TASKS