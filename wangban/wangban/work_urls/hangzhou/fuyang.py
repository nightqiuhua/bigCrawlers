
CRAWL_FUYANG_TASKS = {
    'name':'fuyang',
    'source_url':'http://www.hzfyggzy.org.cn/',
    'task_queue':'wangban:fuyang:an_url_works',
    'task_ajax':'wangban:fuyang:an_url_ajax',
    'task_check':'wangban:fuyang:an_url_check',
    'html_type':'static',
    'tasks':[
    {
        "an_county": "NONE",
        "an_type": "开标安排",
        "an_major": "工程建设",
        "an_sub_url": "http://www.hzfyggzy.org.cn/",
        "an_sub": "NONE",
        "afficheType": "24"
    },
    {
        "an_county": "NONE",
        "an_type": "答疑文件",
        "an_major": "工程建设",
        "an_sub_url": "http://www.hzfyggzy.org.cn/",
        "an_sub": "NONE",
        "afficheType": "23"
    },
    {
        "an_county": "NONE",
        "an_type": "招标公告",
        "an_major": "工程建设",
        "an_sub_url": "http://www.hzfyggzy.org.cn/",
        "an_sub": "NONE",
        "afficheType": "22"
    },
    {
        "an_county": "NONE",
        "an_type": "中标公告",
        "an_major": "工程建设",
        "an_sub_url": "http://www.hzfyggzy.org.cn/",
        "an_sub": "NONE",
        "afficheType": "28"
    },
    {
        "an_county": "NONE",
        "an_type": "采购公告",
        "an_major": "政府采购",
        "an_sub_url": "http://www.hzfyggzy.org.cn/",
        "an_sub": "NONE",
        "afficheType": "27"
    },
    {
        "an_county": "NONE",
        "an_type": "中标公示",
        "an_major": "政府采购",
        "an_sub_url": "http://www.hzfyggzy.org.cn/",
        "an_sub": "NONE",
        "afficheType": "497"
    },
    {
        "an_county": "NONE",
        "an_type": "意见征询",
        "an_major": "政府采购",
        "an_sub_url": "http://www.hzfyggzy.org.cn/",
        "an_sub": "NONE",
        "afficheType": "26"
    },
    {
        "an_county": "NONE",
        "an_type": "单一来源公示",
        "an_major": "政府采购",
        "an_sub_url": "http://www.hzfyggzy.org.cn/",
        "an_sub": "NONE",
        "afficheType": "29"
    },
    {
        "an_county": "NONE",
        "an_type": "招标公告",
        "an_major": "土地交易",
        "an_sub_url": "http://www.hzfyggzy.org.cn/",
        "an_sub": "NONE",
        "afficheType": "495"
    },
    {
        "an_county": "NONE",
        "an_type": "成交结果",
        "an_major": "土地交易",
        "an_sub_url": "http://www.hzfyggzy.org.cn/",
        "an_sub": "NONE",
        "afficheType": "496"
    },
    {
        "an_county": "国有产权交易",
        "an_type": "交易公告",
        "an_major": "产权交易",
        "an_sub_url": "http://www.hzfyggzy.org.cn/",
        "an_sub": "国有产权交易",
        "afficheType": "503"
    },
    {
        "an_county": "农村集体产权交易",
        "an_type": "交易公告",
        "an_major": "产权交易",
        "an_sub_url": "http://www.hzfyggzy.org.cn/",
        "an_sub": "农村集体产权交易",
        "afficheType": "499"
    },
    {
        "an_county": "国有产权交易",
        "an_type": "更正公告",
        "an_major": "产权交易",
        "an_sub_url": "http://www.hzfyggzy.org.cn/",
        "an_sub": "国有产权交易",
        "afficheType": "504"
    },
    {
        "an_county": "农村集体产权交易",
        "an_type": "更正公告",
        "an_major": "产权交易",
        "an_sub_url": "http://www.hzfyggzy.org.cn/",
        "an_sub": "农村集体产权交易",
        "afficheType": "500"
    },
    {
        "an_county": "国有产权交易",
        "an_type": "成交结果公示",
        "an_major": "产权交易",
        "an_sub_url": "http://www.hzfyggzy.org.cn/",
        "an_sub": "国有产权交易",
        "afficheType": "505"
    },
    {
        "an_county": "农村集体产权交易",
        "an_type": "成交结果公示",
        "an_major": "产权交易",
        "an_sub_url": "http://www.hzfyggzy.org.cn/",
        "an_sub": "农村集体产权交易",
        "afficheType": "501"
    },
    {
        "an_county": "NONE",
        "an_type": "中标公示",
        "an_major": "小额工程",
        "an_sub_url": "http://www.hzfyggzy.org.cn/",
        "an_sub": "NONE",
        "afficheType": "493"
    },
    {
        "an_county": "NONE",
        "an_type": "招标公告",
        "an_major": "小额工程",
        "an_sub_url": "http://www.hzfyggzy.org.cn/",
        "an_sub": "NONE",
        "afficheType": "492"
    },
    {
        "an_county": "NONE",
        "an_type": "更正通知",
        "an_major": "小额工程",
        "an_sub_url": "http://www.hzfyggzy.org.cn/",
        "an_sub": "NONE",
        "afficheType": "494"
    }
]
}

def main():
    return CRAWL_FUYANG_TASKS