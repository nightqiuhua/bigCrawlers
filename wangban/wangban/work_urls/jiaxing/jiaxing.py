
CRAWL_JIAXING_TASKS = {
    'name':'jiaxing',
    'source_url':'',
    'task_queue':'wangban:jiaxing:an_work_urls',
    'task_check':'wangban:jiaxing:an_check_urls',
    'task_ajax':'wangban:jiaxing:an_ajax_urls',
    'html_type':'ajax',
    'tasks':[
    {
        "an_sub": "NONE",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003001/003001001/subpagesecond.html",
        "an_major": "工程建设",
        "an_type": "招标公告"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003001/003001005/subpagesecond.html",
        "an_major": "工程建设",
        "an_type": "中标结果公告"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003001/003001003/subpagesecond.html",
        "an_major": "工程建设",
        "an_type": "开标记录"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003001/003001004/subpagesecond.html",
        "an_major": "工程建设",
        "an_type": "中标候选人公示"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003001/003001002/subpagesecond.html",
        "an_major": "工程建设",
        "an_type": "资格预审公告"
    },
    {
        "an_sub": "招标",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003004/003004003/subpagesecond.html",
        "an_major": "土地矿产",
        "an_type": "出让公告"
    },
    {
        "an_sub": "挂牌",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003004/003004001/subpagesecond.html",
        "an_major": "土地矿产",
        "an_type": "出让公告"
    },
    {
        "an_sub": "拍卖",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003004/003004002/subpagesecond.html",
        "an_major": "土地矿产",
        "an_type": "出让公告"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003004/003004004/subpagesecond.html",
        "an_major": "土地矿产",
        "an_type": "结果公示"
    },
    {
        "an_sub": "挂牌",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003003/003003001/subpagesecond.html",
        "an_major": "产权交易",
        "an_type": "出让公告"
    },
    {
        "an_sub": "拍卖",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003003/003003002/subpagesecond.html",
        "an_major": "产权交易",
        "an_type": "出让公告"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003003/003003003/subpagesecond.html",
        "an_major": "产权交易",
        "an_type": "结果公示"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003002/003002003/subpagesecond.html",
        "an_major": "政府采购",
        "an_type": "招标答疑"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003002/003002002/subpagesecond.html",
        "an_major": "政府采购",
        "an_type": "中标成交公告"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003002/003002001/subpagesecond.html",
        "an_major": "政府采购",
        "an_type": "采购公告"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003006/003006002/subpagesecond.html",
        "an_major": "要素交易",
        "an_type": "结果公告"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003006/003006001/subpagesecond.html",
        "an_major": "要素交易",
        "an_type": "出让信息"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003007/003007001/subpagesecond.html",
        "an_major": "镇街道部门国资公司",
        "an_type": "招标"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003007/003007002/subpagesecond.html",
        "an_major": "镇街道部门国资公司",
        "an_type": "招租"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003007/003007003/subpagesecond.html",
        "an_major": "镇街道部门国资公司",
        "an_type": "结果"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003008/003008001/subpagesecond.html",
        "an_major": "其他交易",
        "an_type": "公告信息"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://www.jxzbtb.cn/jygg/003008/003008002/subpagesecond.html",
        "an_major": "其他交易",
        "an_type": "结果信息"
    }
]
}

def main():
    return CRAWL_JIAXING_TASKS