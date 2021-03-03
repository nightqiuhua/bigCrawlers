
CRAWL_YUECHENG_TASKS = {
    'name':'yuecheng',
    'source_url':'',
    'task_queue':'wangban:yuecheng:an_work_urls',
    'task_check':'wangban:yuecheng:an_check_urls',
    'task_ajax':'wangban:yuecheng:an_url_ajax',
    'html_type':'ajax',
   'tasks':[
    {
        "an_sub": "NONE",
        "an_type": "招标公告",
        "an_sub_url": "http://www.sxyc.gov.cn/col/col1559772/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "中标公示",
        "an_sub_url": "http://www.sxyc.gov.cn/col/col1559774/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交信息",
        "an_sub_url": "http://www.sxyc.gov.cn/col/col1559775/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "意见征询",
        "an_sub_url": "http://www.sxyc.gov.cn/col/col1559776/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "采购公告",
        "an_sub_url": "http://www.sxyc.gov.cn/col/col1559777/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "结果公告",
        "an_sub_url": "http://www.sxyc.gov.cn/col/col1559778/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "交易结果公示",
        "an_sub_url": "http://www.sxyc.gov.cn/col/col1559783/index.html",
        "an_major": "产权交易"
    },
    {
        "an_sub": "农村产权",
        "an_type": "交易结果公示",
        "an_sub_url": "http://www.sxyc.gov.cn/col/col1559787/index.html",
        "an_major": "产权交易"
    },
    {
        "an_sub": "国有集体产权",
        "an_type": "交易结果公示",
        "an_sub_url": "http://www.sxyc.gov.cn/col/col1559781/index.html",
        "an_major": "产权交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "招标公告",
        "an_sub_url": "http://www.sxyc.gov.cn/col/col1559789/index.html",
        "an_major": "非中心交易项目"
    },
    {
        "an_sub": "NONE",
        "an_type": "中标公示",
        "an_sub_url": "http://www.sxyc.gov.cn/col/col1559790/index.html",
        "an_major": "非中心交易项目"
    }
]
}

def main():
    return CRAWL_YUECHENG_TASKS