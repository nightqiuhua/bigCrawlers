


CRAWL_XINCHANG_TASKS = {
    'name':'xinchang',
    'source_url':'',
    'task_queue':'wangban:xinchang:an_work_urls',
    'task_check':'wangban:xinchang:an_check_urls',
    'html_type':'ajax',
    'tasks':[
    {
        "an_sub": "NONE",
        "an_type": "招标公告",
        "an_sub_url": "http://www.zjxc.gov.cn/col/col1637585/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "评标结果",
        "an_sub_url": "http://www.zjxc.gov.cn/col/col1634829/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "合同公示",
        "an_sub_url": "http://www.zjxc.gov.cn/col/col1673601/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "中标结果公告",
        "an_sub_url": "http://www.zjxc.gov.cn/col/col1634830/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "答疑与补充",
        "an_sub_url": "http://www.zjxc.gov.cn/col/col1637586/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "采购公告",
        "an_sub_url": "http://www.zjxc.gov.cn/col/col1634832/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交公告",
        "an_sub_url": "http://www.zjxc.gov.cn/col/col1634833/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "意见征求",
        "an_sub_url": "http://www.zjxc.gov.cn/col/col1637588/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "采购合同公示",
        "an_sub_url": "http://www.zjxc.gov.cn/col/col1634834/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "交易公告",
        "an_sub_url": "http://www.zjxc.gov.cn/col/col1634836/index.html",
        "an_major": "产权交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交公告",
        "an_sub_url": "http://www.zjxc.gov.cn/col/col1634837/index.html",
        "an_major": "产权交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交公告",
        "an_sub_url": "http://www.zjxc.gov.cn/col/col1634844/index.html",
        "an_major": "国土出让"
    },
    {
        "an_sub": "NONE",
        "an_type": "出让公告",
        "an_sub_url": "http://www.zjxc.gov.cn/col/col1634843/index.html",
        "an_major": "国土出让"
    },
    {
        "an_sub": "NONE",
        "an_type": "交易公告",
        "an_sub_url": "http://www.zjxc.gov.cn/col/col1634840/index.html",
        "an_major": "乡镇(街道)交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交信息",
        "an_sub_url": "http://www.zjxc.gov.cn/col/col1634841/index.html",
        "an_major": "乡镇(街道)交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "答疑与补充",
        "an_sub_url": "http://www.zjxc.gov.cn/col/col1634842/index.html",
        "an_major": "乡镇(街道)交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "交易公告",
        "an_sub_url": "http://www.zjxc.gov.cn/col/col1634838/index.html",
        "an_major": "其他交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交公告",
        "an_sub_url": "http://www.zjxc.gov.cn/col/col1634839/index.html",
        "an_major": "其他交易"
    }
]
}

def main():
    return CRAWL_XINCHANG_TASKS 