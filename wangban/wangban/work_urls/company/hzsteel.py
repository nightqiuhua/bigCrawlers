#杭钢招投标平台
CRAWL_HZSTEEL_TASKS = {
    'name':'hzsteel',
    'source_url':'',
    'html_type':'static',
    'tasks':[
    {
        "an_sub": "NONE",
        "an_sub_url": "http://bid.hzsteel.com/tzzx/notice/index.htm",
        "an_county": "NONE",
        "an_type": "招标公告",
        "an_major": "NONE"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://bid.hzsteel.com/tzzx/zbgs/index.htm",
        "an_county": "NONE",
        "an_type": "招标结果公示",
        "an_major": "NONE"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://bid.hzsteel.com/tzzx/competeNotice/index.htm",
        "an_county": "NONE",
        "an_type": "网上竞价公告",
        "an_major": "NONE"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://bid.hzsteel.com/tzzx/hgggtz/index.htm",
        "an_county": "NONE",
        "an_type": "公告通知",
        "an_major": "NONE"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://60.191.4.146:18600/pbgs/index.jhtml",
        "an_county": "NONE",
        "an_type": "评标结果公示",
        "an_major": "NONE"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://bid.hzsteel.com/tzzx/ZBYGG/index.htm",
        "an_county": "NONE",
        "an_type": "招标预公告",
        "an_major": "NONE"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://bid.hzsteel.com/tzzx/ZBGGBG/index.htm",
        "an_county": "NONE",
        "an_type": "招标变更公告",
        "an_major": "NONE"
    },
    ]

}

def main():
    return CRAWL_HZSTEEL_TASKS