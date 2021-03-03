
#政府采购
CRAWL_GUOJIAGAOXINQU_TASKS = {
    'name':'guojiagaoxinqu',
    'source_url':'',
    'task_queue':'wangban:guojiagaoxinqu:an_work_urls',
    'task_check':'wangban:guojiagaoxinqu:an_url_check',
    'task_ajax':'wangban:guojiagaoxinqu:an_url_ajax',
    'html_type':'static',
    'tasks':[
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "资格预审结果公示",
        "an_sub_url": "http://gaoxin.bidding.gov.cn/gxzgysgs/index.jhtml?areaCode=330231"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "中标候选人公示",
        "an_sub_url": "http://gaoxin.bidding.gov.cn/gcjszbhxrgs/index.jhtml?areaCode=330231"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "招标公告",
        "an_sub_url": "http://gaoxin.bidding.gov.cn/gcjszbgg/index.jhtml?areaCode=330231"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "中标结果公示",
        "an_sub_url": "http://gaoxin.bidding.gov.cn/gcjszbjggs/index.jhtml?areaCode=330231"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "资格预审公告",
        "an_sub_url": "http://gaoxin.bidding.gov.cn/gcjszgysgg/index.jhtml?areaCode=330231"
    },
    {
        "an_sub": "NONE",
        "an_major": "其他交易",
        "an_type": "成交结果公示",
        "an_sub_url": "http://gaoxin.bidding.gov.cn/gxcjjggs/index.jhtml?areaCode=330231"
    },
    {
        "an_sub": "NONE",
        "an_major": "其他交易",
        "an_type": "招标公告",
        "an_sub_url": "http://gaoxin.bidding.gov.cn/qtjyzbgg/index.jhtml?areaCode=330231"
    }
]
}
#国家高新区


def main():
    return CRAWL_GUOJIAGAOXINQU_TASKS