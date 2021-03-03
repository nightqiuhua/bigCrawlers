
CRAWL_JIANGGAN_TASKS = {
    'name':'jianggan',
    'source_url':'http://www.jdggzy.com/index.aspx',
    'task_queue':'wangban:jianggan:an_url_works',
    'task_ajax':'wangban:jianggan:an_url_ajax',
    'task_check':'wangban:jianggan:an_url_check',
    'html_type':'ajax',
    'tasks':[
    {
        "an_major": "小额公共资源交易",
        "an_sub_url": "http://www.jianggan.gov.cn/col/col1365636/index.html",
        "an_sub": "NONE",
        "an_type": "招标信息"
    },
    {
        "an_major": "小额公共资源交易",
        "an_sub_url": "http://www.jianggan.gov.cn/col/col1365637/index.html",
        "an_sub": "NONE",
        "an_type": "中标信息"
    }
]
}

def main():
    return CRAWL_JIANGGAN_TASKS