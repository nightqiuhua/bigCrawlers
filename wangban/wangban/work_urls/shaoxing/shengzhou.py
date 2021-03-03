

CRAWL_SHENGZHOU_TASKS = {
    'name':'shengzhou',
    'source_url':'',
    'task_queue':'wangban:shengzhou:an_work_urls',
    'task_check':'wangban:shengzhou:an_url_check',
    'html_type':'static',
    'tasks':[
    {
        "an_sub": "NONE",
        "an_type": "中标公示",
        "an_sub_url": "http://220.191.224.142/TPFront/jsxmjy/011003/",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "招标公告",
        "an_sub_url": "http://220.191.224.142/TPFront/jsxmjy/011001/",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "中标预公示",
        "an_sub_url": "http://220.191.224.142/TPFront/jsxmjy/011002/",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "招标公告",
        "an_sub_url": "http://220.191.224.142/TPFront/zfcg/012001/",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "中标公告",
        "an_sub_url": "http://220.191.224.142/TPFront/zfcg/012003/",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "征求意见",
        "an_sub_url": "http://220.191.224.142/TPFront/zfcg/012004/",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "中标成交公示",
        "an_sub_url": "http://220.191.224.142/TPFront/zfcg/012002/",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "招标公告",
        "an_sub_url": "http://220.191.224.142/TPFront/tdjy/013001/",
        "an_major": "土地交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "中标公示",
        "an_sub_url": "http://220.191.224.142/TPFront/tdjy/013002/",
        "an_major": "土地交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "交易公告",
        "an_sub_url": "http://220.191.224.142/TPFront/cqjy/021001/",
        "an_major": "产权交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交公示",
        "an_sub_url": "http://220.191.224.142/TPFront/cqjy/021002/",
        "an_major": "产权交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "更正公告",
        "an_sub_url": "http://220.191.224.142/TPFront/xzbm/022002/",
        "an_major": "乡镇(街道)部门"
    },
    {
        "an_sub": "NONE",
        "an_type": "招标公告",
        "an_sub_url": "http://220.191.224.142/TPFront/xzbm/022001/",
        "an_major": "乡镇(街道)部门"
    },
    {
        "an_sub": "NONE",
        "an_type": "中标公示",
        "an_sub_url": "http://220.191.224.142/TPFront/xzbm/022003/",
        "an_major": "乡镇(街道)部门"
    }
]
}

def main():
    return CRAWL_SHENGZHOU_TASKS