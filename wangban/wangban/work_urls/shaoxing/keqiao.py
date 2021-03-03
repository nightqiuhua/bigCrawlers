


CRAWL_KEQIAO_TASKS = {
    'name':'keqiao',
    'source_url':'',
    'task_queue':'wangban:keqiao:an_work_urls',
    'task_check':'wangban:keqiao:an_check_urls',
    'html_type':'ajax',
    'tasks':[
    {
        "an_sub": "NONE",
        "an_type": "答疑公告",
        "an_sub_url": "http://www.kq.gov.cn/col/col1658098/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "招标公告",
        "an_sub_url": "http://www.kq.gov.cn/col/col1658095/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "中标公示",
        "an_sub_url": "http://www.kq.gov.cn/col/col1658096/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "答疑公告",
        "an_sub_url": "http://www.kq.gov.cn/col/col1658104/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "采购公告",
        "an_sub_url": "http://www.kq.gov.cn/col/col1658099/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "中标公示",
        "an_sub_url": "http://www.kq.gov.cn/col/col1658100/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "征询意见",
        "an_sub_url": "http://www.kq.gov.cn/col/col1658103/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "电子反拍结果",
        "an_sub_url": "http://www.kq.gov.cn/col/col1658106/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "电子反拍公告",
        "an_sub_url": "http://www.kq.gov.cn/col/col1658105/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "拍卖服务公告",
        "an_sub_url": "http://www.kq.gov.cn/col/col1658107/index.html",
        "an_major": "产权交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "交易公告",
        "an_sub_url": "http://www.kq.gov.cn/col/col1658109/index.html",
        "an_major": "产权交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交结果",
        "an_sub_url": "http://www.kq.gov.cn/col/col1658110/index.html",
        "an_major": "产权交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "交易公告",
        "an_sub_url": "http://www.kq.gov.cn/col/col1658113/index.html",
        "an_major": "土地出让"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交公告",
        "an_sub_url": "http://www.kq.gov.cn/col/col1658114/index.html",
        "an_major": "土地出让"
    },
    {
        "an_sub": "NONE",
        "an_type": "交易公告",
        "an_sub_url": "http://www.kq.gov.cn/col/col1658115/index.html",
        "an_major": "限额以下交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "答疑公告",
        "an_sub_url": "http://www.kq.gov.cn/col/col1688011/index.html",
        "an_major": "限额以下交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交结果",
        "an_sub_url": "http://www.kq.gov.cn/col/col1658116/index.html",
        "an_major": "限额以下交易"
    }
]
}

def main():
    return CRAWL_KEQIAO_TASKS 