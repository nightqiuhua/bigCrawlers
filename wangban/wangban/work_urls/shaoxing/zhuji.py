

CRAWL_ZHUJI_TASKS = {
    'name':'zhuji',
    'source_url':'',
    'task_queue':'wangban:zhuji:an_work_urls',
    'task_check':'wangban:zhuji:an_check_urls',
    'html_type':'ajax',
    'tasks':[
    {
        "an_sub": "NONE",
        "an_type": "通知公告",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388401/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "中标公示",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388403/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "招标公告",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388402/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交结果",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388404/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交公示",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388408/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "采购公告",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388407/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交结果",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388409/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "要素公示",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388406/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "通知公告",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388405/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "合同公告",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1693203/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "交易公告",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388411/index.html",
        "an_major": "要素资源"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交公示",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388412/index.html",
        "an_major": "要素资源"
    },
    {
        "an_sub": "NONE",
        "an_type": "通知公告",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388410/index.html",
        "an_major": "要素资源"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交结果",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388413/index.html",
        "an_major": "要素资源"
    },
    {
        "an_sub": "NONE",
        "an_type": "交易公告",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388415/index.html",
        "an_major": "镇街部门交易信息"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交公示",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388416/index.html",
        "an_major": "镇街部门交易信息"
    },
    {
        "an_sub": "NONE",
        "an_type": "通知公告",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388414/index.html",
        "an_major": "镇街部门交易信息"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交结果",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388417/index.html",
        "an_major": "镇街部门交易信息"
    },
    {
        "an_sub": "NONE",
        "an_type": "交易公告",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388419/index.html",
        "an_major": "农村产权"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交公示",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388420/index.html",
        "an_major": "农村产权"
    },
    {
        "an_sub": "NONE",
        "an_type": "通知公告",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388418/index.html",
        "an_major": "农村产权"
    },
    {
        "an_sub": "个人产权",
        "an_type": "成交结果",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388422/index.html",
        "an_major": "农村产权"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交结果",
        "an_sub_url": "http://www.zhuji.gov.cn/col/col1388421/index.html",
        "an_major": "农村产权"
    }
]
}

def main():
    return CRAWL_ZHUJI_TASKS