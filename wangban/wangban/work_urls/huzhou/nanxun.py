

CRAWL_NANXUN_TASKS = {
    'name':'nanxun',
    'source_url':'',
    'task_queue':'wangban:nanxun:an_work_urls',
    'task_check':'wangban:nanxun:an_check_urls',
    'task_ajax':'wangban:nanxun:an_ajax_urls',
    'html_type':'ajax',
    'tasks':[
    {
        "an_sub": "建设类",
        "an_type": "中标公告",
        "an_sub_url": "http://ggzy.nanxun.gov.cn/gcxmjy/zbgg/jsl/index.html",
        "an_major": "工程项目交易"
    },
    {
        "an_sub": "交通类",
        "an_type": "中标公告",
        "an_sub_url": "http://ggzy.nanxun.gov.cn/gcxmjy/zbgg/jtl/index.html",
        "an_major": "工程项目交易"
    },
    {
        "an_sub": "水利类",
        "an_type": "中标公告",
        "an_sub_url": "http://ggzy.nanxun.gov.cn/gcxmjy/zbgg/sll/index.html",
        "an_major": "工程项目交易"
    },
    {
        "an_sub": "建设类",
        "an_type": "招标公告",
        "an_sub_url": "http://ggzy.nanxun.gov.cn/gcxmjy/fbgg/jsl/index.html",
        "an_major": "工程项目交易"
    },
    {
        "an_sub": "交通类",
        "an_type": "招标公告",
        "an_sub_url": "http://ggzy.nanxun.gov.cn/gcxmjy/fbgg/jtl/index.html",
        "an_major": "工程项目交易"
    },
    {
        "an_sub": "水利类",
        "an_type": "招标公告",
        "an_sub_url": "http://ggzy.nanxun.gov.cn/gcxmjy/fbgg/sll/index.html",
        "an_major": "工程项目交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "中标公示",
        "an_sub_url": "http://ggzy.nanxun.gov.cn/ysscjy/zbgs/index.html",
        "an_major": "要素市场交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "招标公告",
        "an_sub_url": "http://ggzy.nanxun.gov.cn/ysscjy/zbgg/index.html",
        "an_major": "要素市场交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "中标公示",
        "an_sub_url": "http://ggzy.nanxun.gov.cn/gzkfqjqjbm/zbgs/index.html",
        "an_major": "各镇(开发区)及区级部门"
    },
    {
        "an_sub": "NONE",
        "an_type": "招标公告",
        "an_sub_url": "http://ggzy.nanxun.gov.cn/gzkfqjqjbm/fbgg/index.html",
        "an_major": "各镇(开发区)及区级部门"
    }
]
}
#http://ggzy.chinananxun.gov.cn
#http://ggzy.nanxun.gov.cn


def main():
    return CRAWL_NANXUN_TASKS