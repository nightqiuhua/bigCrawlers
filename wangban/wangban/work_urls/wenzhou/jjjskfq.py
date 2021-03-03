
CRAWL_JJJSKFQ_TASKS = {
    'name':'jjjskfq',
    'source_url':'',
    'task_queue':'wangban:jjjskfq:an_work_urls',
    'task_check':'wangban:jjjskfq:an_check_urls',
    'html_type':'ajax',
    'tasks':[
    {
        "an_sub_url": "http://www.wetdz.gov.cn/col/col1316362/index.html",
        "an_county": "NONE",
        "an_major": "工程建设",
        "an_type": "招标公告",
        "an_sub": "NONE"
    },
    {
        "an_sub_url": "http://www.wetdz.gov.cn/col/col1316365/index.html",
        "an_county": "NONE",
        "an_major": "工程建设",
        "an_type": "中标结果",
        "an_sub": "NONE"
    },
    {
        "an_sub_url": "http://www.wetdz.gov.cn/col/col1331282/index.html",
        "an_county": "NONE",
        "an_major": "工程建设",
        "an_type": "答疑补充",
        "an_sub": "NONE"
    },
    {
        "an_sub_url": "http://www.wetdz.gov.cn/col/col1316363/index.html",
        "an_county": "NONE",
        "an_major": "工程建设",
        "an_type": "候选公示",
        "an_sub": "NONE"
    },
    {
        "an_sub_url": "http://www.wetdz.gov.cn/col/col1316366/index.html",
        "an_county": "NONE",
        "an_major": "工程建设",
        "an_type": "保证金退付",
        "an_sub": "NONE"
    },
    {
        "an_sub_url": "http://www.wetdz.gov.cn/col/col1366266/index.html",
        "an_county": "NONE",
        "an_major": "国企采购",
        "an_type": "保证金退付",
        "an_sub": "NONE"
    },
    {
        "an_sub_url": "http://www.wetdz.gov.cn/col/col1316367/index.html",
        "an_county": "NONE",
        "an_major": "国企采购",
        "an_type": "采购公告",
        "an_sub": "NONE"
    },
    {
        "an_sub_url": "http://www.wetdz.gov.cn/col/col1366264/index.html",
        "an_county": "NONE",
        "an_major": "国企采购",
        "an_type": "中标公告",
        "an_sub": "NONE"
    }
]
}

def main():
    return CRAWL_JJJSKFQ_TASKS