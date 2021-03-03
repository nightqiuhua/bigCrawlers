

#可以用
CRAWL_YUYAO_AJAX_TASKS = {
    'name':'yuyao_ajax',
    'source_url':'',
    'task_queue':'wangban:yuyao_ajax:an_work_urls',
    'task_check':'wangban:yuyao_ajax:an_url_check',
    'task_ajax':'wangban:yuyao_ajax:an_url_ajax',
    'html_type':'ajax',
    'tasks':[
    {
        "an_sub": "交易信息",
        "an_major": "国有产权交易",
        "an_type": "挂牌信息",
        "an_sub_url": "http://121.196.209.13:7080/jmr/jump?num=3"
    },
    {
        "an_sub": "招标信息",
        "an_major": "国有产权交易",
        "an_type": "结果公示",
        "an_sub_url": "http://121.196.209.13:7080/jmr/jump?num=4"
    },
    {
        "an_sub": "招标信息",
        "an_major": "国有产权交易",
        "an_type": "出让公告",
        "an_sub_url": "http://121.196.209.13:7080/jmr/jump?num=2"
    }
]
}
def main():
    return CRAWL_YUYAO_AJAX_TASKS