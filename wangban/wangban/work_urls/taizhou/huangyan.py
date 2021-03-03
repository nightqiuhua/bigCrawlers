
CRAWL_HUANGYAN_TASKS = {
    'name':'huangyan',
    'source_url':'',
    'task_queue':'wangban:huangyan:an_work_urls',
    'task_check':'wangban:huangyan:an_url_check',
    'task_ajax':'wangban:huangyan:an_url_ajax',
    'html_type':'ajax',
    'tasks':[
    {'国有土地使用权出让领域':{
    'NONE':{'NONE':'http://www.zjhy.gov.cn/col/col1633716/index.html',},
    }},
    {' 矿业权出让领域':{
    'NONE':{'NONE':'http://www.zjhy.gov.cn/col/col1633717/index.html',},
    }},
    {'政府采购领域':{
    'NONE':{'NONE':'http://www.zjhy.gov.cn/col/col1633718/index.html',},
    }},
    {' 国有产权交易领域':{
    'NONE':{'NONE':'http://www.zjhy.gov.cn/col/col1633719/index.html',},
    }},
    {'工程建设招标投标领域':{
    'NONE':{'NONE':'http://www.zjhy.gov.cn/col/col1633721/index.html',},
    }},
    ]
}

def main():
    return CRAWL_HUANGYAN_TASKS