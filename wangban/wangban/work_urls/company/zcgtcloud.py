#绿城集团招采平台 
CRAWL_ZCGT_TASKS = {
    'name':'zcgtcloud',
    'source_url':'',
    'html_type':'ajax',
    'tasks':[
    {
        "an_sub": "NONE",
        "an_sub_url": "http://zc.gtcloud.cn/HomePage/TenderNotice.aspx",
        "an_county": "NONE",
        "an_type": "招标公告",
        "an_major": "NONE"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://zc.gtcloud.cn/HomePage/BidAnnouncement.aspx",
        "an_county": "NONE",
        "an_type": "中标公告",
        "an_major": "NONE"
    },
    ]

}

def main():
    return CRAWL_ZCGT_TASKS