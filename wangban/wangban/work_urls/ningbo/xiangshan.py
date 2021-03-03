
#利用以前的
CRAWL_XIANGSHAN_TASKS = {
    'name':'xiangshan',
    'source_url':'',
    'task_queue':'wangban:xiangshan:an_work_urls',
    'task_check':'wangban:xiangshan:an_url_check',
    'task_ajax':'wangban:xiangshan:an_url_ajax',
    'html_type':'static',
    'tasks':[
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "资格预审结果公示",
        "an_sub_url": "http://xiangshan.bidding.gov.cn/gcjsysjggs/index.jhtml?areaCode=330225"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "中标候选人公示",
        "an_sub_url": "http://xiangshan.bidding.gov.cn/gcjszbhxrgs/index.jhtml?areaCode=330225"
    },
    {
        "an_sub": "乡镇（街道）交易",
        "an_major": "工程建设",
        "an_type": "中标结果公示",
        "an_sub_url": "http://xiangshan.bidding.gov.cn/cqjyzbjggs/index.jhtml?areaCode=330225"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "中标结果公示",
        "an_sub_url": "http://xiangshan.bidding.gov.cn/gcjszbjggs/index.jhtml?areaCode=330225"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "资格预审公告",
        "an_sub_url": "http://xiangshan.bidding.gov.cn/gcjszgysgg/index.jhtml?areaCode=330225"
    },
    {
        "an_sub": "乡镇（街道）交易",
        "an_major": "工程建设",
        "an_type": "澄清或修改",
        "an_sub_url": "http://xiangshan.bidding.gov.cn/cqjycqgg/index.jhtml?areaCode=330225"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "澄清或修改",
        "an_sub_url": "http://xiangshan.bidding.gov.cn/gcjscqgg/index.jhtml?areaCode=330225"
    },
    {
        "an_sub": "乡镇（街道）交易",
        "an_major": "工程建设",
        "an_type": "招标公告",
        "an_sub_url": "http://xiangshan.bidding.gov.cn/xzjyzbgg/index.jhtml?areaCode=330225"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "招标公告",
        "an_sub_url": "http://xiangshan.bidding.gov.cn/gcjszbgg/index.jhtml?areaCode=330225"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "招标文件预公示",
        "an_sub_url": "http://xiangshan.bidding.gov.cn/gcjszbggygs/index.jhtml?areaCode=330225"
    },
    {
        "an_sub": "NONE",
        "an_major": "产权交易",
        "an_type": "中标结果公示",
        "an_sub_url": "http://xiangshan.bidding.gov.cn/fhjggs/index.jhtml?areaCode=330225"
    },
    {
        "an_sub": "NONE",
        "an_major": "产权交易",
        "an_type": "出让公告",
        "an_sub_url": "http://xiangshan.bidding.gov.cn/cqjyjygg/index.jhtml?areaCode=330225"
    },
    {
        "an_sub": "NONE",
        "an_major": "产权交易",
        "an_type": "澄清或修改公告",
        "an_sub_url": "http://xiangshan.bidding.gov.cn/cqjycqgg2/index.jhtml?areaCode=330225"
    }
]
}

#用以前的
def main():
    return CRAWL_XIANGSHAN_TASKS