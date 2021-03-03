
CRAWL_TAISHUN_TASKS = {
    'name':'taishun',
    'source_url':'',
    'task_queue':'wangban:taishun:an_work_urls',
    'task_check':'wangban:taishun:an_check_urls',
    'html_type':'static',
    'tasks':[
    {
        "an_sub_url": "http://117.149.227.75:81/TPFront/jyxx/004001/004001001/",
        "an_county": "NONE",
        "an_major": "建设工程",
        "an_type": "招标公告",
        "an_sub": "NONE"
    },
    {
        "an_sub_url": "http://117.149.227.75:81/TPFront/jyxx/004001/004001005/",
        "an_county": "NONE",
        "an_major": "建设工程",
        "an_type": "中标结果",
        "an_sub": "NONE"
    },
    {
        "an_sub_url": "http://117.149.227.75:81/TPFront/jyxx/004001/004001004/",
        "an_county": "NONE",
        "an_major": "建设工程",
        "an_type": "候选公示",
        "an_sub": "NONE"
    },
    {
        "an_sub_url": "http://117.149.227.75:81/TPFront/jyxx/004001/004001003/",
        "an_county": "NONE",
        "an_major": "建设工程",
        "an_type": "答疑与补充",
        "an_sub": "NONE"
    },
    {
        "an_sub_url": "http://117.149.227.75:81/TPFront/jyxx/004002/004002005/",
        "an_county": "NONE",
        "an_major": "政府采购",
        "an_type": "中标公示",
        "an_sub": "NONE"
    },
    {
        "an_sub_url": "http://117.149.227.75:81/TPFront/jyxx/004002/004002001/",
        "an_county": "NONE",
        "an_major": "政府采购",
        "an_type": "采购公告",
        "an_sub": "NONE"
    },
    {
        "an_sub_url": "http://117.149.227.75:81/TPFront/jyxx/004002/004002003/",
        "an_county": "NONE",
        "an_major": "政府采购",
        "an_type": "更正公告",
        "an_sub": "NONE"
    },
    {
        "an_sub_url": "http://117.149.227.75:81/TPFront/jyxx/004005/004005001/",
        "an_county": "NONE",
        "an_major": "产权交易",
        "an_type": "交易公告",
        "an_sub": "NONE"
    },
    {
        "an_sub_url": "http://117.149.227.75:81/TPFront/jyxx/004005/004005003/",
        "an_county": "NONE",
        "an_major": "产权交易",
        "an_type": "出让结果",
        "an_sub": "NONE"
    },
    {
        "an_sub_url": "http://117.149.227.75:81/TPFront/jyxx/004006/004006002/",
        "an_county": "NONE",
        "an_major": "镇(乡)交易平台",
        "an_type": "乡镇中标公告",
        "an_sub": "NONE"
    },
    {
        "an_sub_url": "http://117.149.227.75:81/TPFront/jyxx/004006/004006003/",
        "an_county": "NONE",
        "an_major": "镇(乡)交易平台",
        "an_type": "乡镇公告变更",
        "an_sub": "NONE"
    },
    {
        "an_sub_url": "http://117.149.227.75:81/TPFront/jyxx/004006/004006001/",
        "an_county": "NONE",
        "an_major": "镇(乡)交易平台",
        "an_type": "乡镇交易公告",
        "an_sub": "NONE"
    }
]
}

def main():
    return CRAWL_TAISHUN_TASKS