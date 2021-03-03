


CRAWL_CIXI_TASKS = {
    'name':'cixi',
    'source_url':'',
    'task_queue':'wangban:cixi:an_work_urls',
    'task_check':'wangban:cixi:an_url_check',
    'task_ajax':'wangban:cixi:an_url_ajax',
    'html_type':'static',
    'tasks':[
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "招标公告",
        "an_sub_url": "http://cixi.bidding.gov.cn/cxxizbgg/index.jhtml?areaCode=330282"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "结果公示",
        "an_sub_url": "http://cixi.bidding.gov.cn/cxjjgs/index.jhtml?areaCode=330282"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "招标文件预公示",
        "an_sub_url": "http://cixi.bidding.gov.cn/gcjszbggygs/index.jhtml?areaCode=330282"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "补充文件",
        "an_sub_url": "http://cixi.bidding.gov.cn/cxbcwj/index.jhtml?areaCode=330282"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "中标结果公告",
        "an_sub_url": "http://cixi.bidding.gov.cn/fhzbjggg/index.jhtml?areaCode=330282"
    },
    {
        "an_sub": "NONE",
        "an_major": "政府采购",
        "an_type": "采购文件或需求公示",
        "an_sub_url": "http://cixi.bidding.gov.cn/cxcgwjhxqgs/index.jhtml?areaCode=330282"
    },
    {
        "an_sub": "NONE",
        "an_major": "政府采购",
        "an_type": "采购公告",
        "an_sub_url": "http://cixi.bidding.gov.cn/zfcgcggg/index.jhtml?areaCode=330282"
    },
    {
        "an_sub": "NONE",
        "an_major": "政府采购",
        "an_type": "单一来源公示",
        "an_sub_url": "http://cixi.bidding.gov.cn/zfcgdyly/index.jhtml?areaCode=330282"
    },
    {
        "an_sub": "NONE",
        "an_major": "政府采购",
        "an_type": "采购结果公示",
        "an_sub_url": "http://cixi.bidding.gov.cn/zfcgcgjggs2/index.jhtml?areaCode=330282"
    },
    {
        "an_sub": "NONE",
        "an_major": "土地交易",
        "an_type": "出让公告",
        "an_sub_url": "http://cixi.bidding.gov.cn/tdjycrgg/index.jhtml?areaCode=330282"
    },
    {
        "an_sub": "NONE",
        "an_major": "土地交易",
        "an_type": "出让结果公示",
        "an_sub_url": "http://cixi.bidding.gov.cn/tdjycrjggs/index.jhtml?areaCode=330282"
    },
    {
        "an_sub": "NONE",
        "an_major": "产权交易",
        "an_type": "交易结果公示",
        "an_sub_url": "http://cixi.bidding.gov.cn/cxjyjggs1/index.jhtml?areaCode=330282"
    },
    {
        "an_sub": "NONE",
        "an_major": "产权交易",
        "an_type": "交易公告",
        "an_sub_url": "http://cixi.bidding.gov.cn/cqjyjygg/index.jhtml?areaCode=330282"
    },
    {
        "an_sub": "NONE",
        "an_major": "工业用地二级市场",
        "an_type": "交易结果公示",
        "an_sub_url": "http://cixi.bidding.gov.cn/cxjzjggs/index.jhtml?areaCode=330282"
    },
    {
        "an_sub": "NONE",
        "an_major": "工业用地二级市场",
        "an_type": "交易公告",
        "an_sub_url": "http://cixi.bidding.gov.cn/cxjygg/index.jhtml?areaCode=330282"
    },
    {
        "an_sub": "NONE",
        "an_major": "其他交易",
        "an_type": "交易结果公示",
        "an_sub_url": "http://cixi.bidding.gov.cn/cxjygggs1/index.jhtml?areaCode=330282"
    },
    {
        "an_sub": "NONE",
        "an_major": "其他交易",
        "an_type": "交易公告",
        "an_sub_url": "http://cixi.bidding.gov.cn/cxjygg1/index.jhtml?areaCode=330282"
    },
    {
        "an_sub": "NONE",
        "an_major": "镇级平台(农交所)",
        "an_type": "工程招标公告",
        "an_sub_url": "http://cixi.bidding.gov.cn/gczbgg/index.jhtml?areaCode=330282"
    },
    {
        "an_sub": "NONE",
        "an_major": "镇级平台(农交所)",
        "an_type": "采购公示",
        "an_sub_url": "http://cixi.bidding.gov.cn/cxcggs/index.jhtml?areaCode=330282"
    },
    {
        "an_sub": "NONE",
        "an_major": "镇级平台(农交所)",
        "an_type": "采购公告",
        "an_sub_url": "http://cixi.bidding.gov.cn/cxcggg1/index.jhtml?areaCode=330282"
    },
    {
        "an_sub": "NONE",
        "an_major": "镇级平台(农交所)",
        "an_type": "工程结果公示",
        "an_sub_url": "http://cixi.bidding.gov.cn/gcjggs/index.jhtml?areaCode=330282"
    }
]
}

def main():
    return CRAWL_CIXI_TASKS 