#浙江海港
CRAWL_ZJSEAPORT_TASKS = {
    'name':'zjseaport',
    'source_url':'',
    'html_type':'static',
    'tasks':[
    {
        "an_sub": "NONE",
        "an_sub_url": "http://www.zjseaport.com/jtww/yggc/zbgg/index.html",
        "an_county": "NONE",
        "an_type": "招标公告",
        "an_major": "NONE"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://www.zjseaport.com/jtww/yggc/zbgs/index.html",
        "an_county": "NONE",
        "an_type": "中标公示",
        "an_major": "NONE"
    },
    ]

}

def main():
    return CRAWL_ZJSEAPORT_TASKS