
#利用以前的
CRAWL_XIANGSHAN_AJAX_TASKS = {
    'name':'xiangshan_ajax',
    'source_url':'',
    'task_queue':'wangban:xiangshan_ajax:an_work_urls',
    'task_check':'wangban:xiangshan_ajax:an_url_check',
    'task_ajax':'wangban:xiangshan_ajax:an_url_ajax',
    'html_type':'ajax',
    'tasks':[
    {
        "an_sub": "NONE",
        "an_major": "政府采购",
        "an_type": "意见征询",
        "an_sub_url": "http://www.nbzfcg.cn/project/DemandNotice.aspx?NoticeType=2&NoticeRegion=330225&NoticeTitle="
    },
    {
        "an_sub": "NONE",
        "an_major": "政府采购",
        "an_type": "采购公告",
        "an_sub_url": "http://www.nbzfcg.cn/project/NoticeSearch.aspx?Type=2&Region=330225&TenderId=&NoticeTitle="
    },
    {
        "an_sub": "NONE",
        "an_major": "政府采购",
        "an_type": "单一来源公示",
        "an_sub_url": "http://www.nbzfcg.cn/project/DemandNotice.aspx?NoticeType=1&NoticeRegion=330225&NoticeTitle="
    },
    {
        "an_sub": "NONE",
        "an_major": "政府采购",
        "an_type": "采购结果公告",
        "an_sub_url": "http://www.nbzfcg.cn/project/NoticeSearch.aspx?Type=3&Region=330225&TenderId=&NoticeTitle="
    },
    {
        "an_sub": "NONE",
        "an_major": "政府采购",
        "an_type": "资格预审公告",
        "an_sub_url": "http://www.nbzfcg.cn/project/NoticeSearch.aspx?Type=1&Region=330225&TenderId=&NoticeTitle="
    }
]
}

#用以前的
def main():
    return CRAWL_XIANGSHAN_AJAX_TASKS