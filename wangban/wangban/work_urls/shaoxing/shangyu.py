



CRAWL_SHANGYU_TASKS = {
    'name':'shangyu',
    'source_url':'',
    'task_queue':'wangban:shangyu:an_work_urls',
    'task_check':'wangban:shangyu:an_check_urls',
    'html_type':'ajax',
    'tasks':[
    {
        "an_sub": "NONE",
        "an_type": "中标公示",
        "an_sub_url": "http://ztb.shangyu.gov.cn/col/col1513296/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "乡镇街道、部门两区",
        "an_type": "中标公示",
        "an_sub_url": "http://ztb.shangyu.gov.cn/col/col1513301/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "文件公示",
        "an_sub_url": "http://ztb.shangyu.gov.cn/col/col1513338/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "答疑补充",
        "an_sub_url": "http://ztb.shangyu.gov.cn/col/col1513324/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "招标公告",
        "an_sub_url": "http://ztb.shangyu.gov.cn/col/col1513281/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "乡镇街道、部门两区",
        "an_type": "招标公告",
        "an_sub_url": "http://ztb.shangyu.gov.cn/col/col1513288/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交信息",
        "an_sub_url": "http://ztb.shangyu.gov.cn/col/col1513305/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "乡镇街道、部门两区",
        "an_type": "成交信息",
        "an_sub_url": "http://ztb.shangyu.gov.cn/col/col1513309/index.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "采购公告",
        "an_sub_url": "http://ztb.shangyu.gov.cn/col/col1513285/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "采购公示",
        "an_sub_url": "http://ztb.shangyu.gov.cn/col/col1513284/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "乡镇街道、部门两区",
        "an_type": "采购公示",
        "an_sub_url": "http://ztb.shangyu.gov.cn/col/col1675146/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "结果公告",
        "an_sub_url": "http://ztb.shangyu.gov.cn/col/col1513298/index.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "招标公告",
        "an_sub_url": "http://ztb.shangyu.gov.cn/col/col1513282/index.html",
        "an_major": "土地交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交信息",
        "an_sub_url": "http://ztb.shangyu.gov.cn/col/col1513306/index.html",
        "an_major": "土地交易"
    },
    {
        "an_sub": "乡镇街道、部门两区",
        "an_type": "招标公告",
        "an_sub_url": "http://ztb.shangyu.gov.cn/col/col1513290/index.html",
        "an_major": "产权交易"
    },
    {
        "an_sub": "国有产权交易",
        "an_type": "招标公告",
        "an_sub_url": "http://ztb.shangyu.gov.cn/col/col1513286/index.html",
        "an_major": "产权交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "中标公告",
        "an_sub_url": "http://ztb.shangyu.gov.cn/col/col1513303/index.html",
        "an_major": "产权交易"
    },
    {
        "an_sub": "乡镇街道、部门两区",
        "an_type": "成交信息",
        "an_sub_url": "http://ztb.shangyu.gov.cn/col/col1513311/index.html",
        "an_major": "产权交易"
    },
    {
        "an_sub": "国有产权交易",
        "an_type": "成交信息",
        "an_sub_url": "http://ztb.shangyu.gov.cn/col/col1513307/index.html",
        "an_major": "产权交易"
    }
]
}

def main():
    return CRAWL_SHANGYU_TASKS