# -*- coding: utf-8 -*-

CRAWL_ANJI_TASKS = {
    'name':'anji',
    'source_url':'',
    'task_queue':'wangban:anji:an_work_urls',
    'task_check':'wangban:anji:an_url_check',
    'html_type':'static',
    'tasks':[
    {
        "an_sub": "NONE",
        "an_type": "中标候选人公示",
        "an_sub_url": "http://www.ajztb.com/jyxx/003001/003001005/moreinfo.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "开标结果公示",
        "an_sub_url": "http://www.ajztb.com/jyxx/003001/003001004/moreinfo.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "答疑澄清",
        "an_sub_url": "http://www.ajztb.com/jyxx/003001/003001002/moreinfo.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "招标公告",
        "an_sub_url": "http://www.ajztb.com/jyxx/003001/003001001/moreinfo.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "中标结果",
        "an_sub_url": "http://www.ajztb.com/jyxx/003001/003001006/moreinfo.html",
        "an_major": "建设工程"
    },
    {
        "an_sub": "NONE",
        "an_type": "结果公示",
        "an_sub_url": "http://www.ajztb.com/jyxx/003002/003002005/moreinfo.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "答疑澄清",
        "an_sub_url": "http://www.ajztb.com/jyxx/003002/003002004/moreinfo.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "招标公告",
        "an_sub_url": "http://www.ajztb.com/jyxx/003002/003002001/moreinfo.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "合同公示",
        "an_sub_url": "http://www.ajztb.com/jyxx/003002/003002006/moreinfo.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "变更公告",
        "an_sub_url": "http://www.ajztb.com/jyxx/003002/003002003/moreinfo.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "意见征询",
        "an_sub_url": "http://www.ajztb.com/jyxx/003002/003002002/moreinfo.html",
        "an_major": "政府采购"
    },
    {
        "an_sub": "NONE",
        "an_type": "结果公示",
        "an_sub_url": "http://www.ajztb.com/jyxx/003006/003006004/moreinfo.html",
        "an_major": "土地交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "交易公告",
        "an_sub_url": "http://www.ajztb.com/jyxx/003006/003006001/moreinfo.html",
        "an_major": "土地交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "答疑澄清",
        "an_sub_url": "http://www.ajztb.com/jyxx/003006/003006003/moreinfo.html",
        "an_major": "土地交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "变更公告",
        "an_sub_url": "http://www.ajztb.com/jyxx/003006/003006002/moreinfo.html",
        "an_major": "土地交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "结果公示",
        "an_sub_url": "http://www.ajztb.com/jyxx/003005/003005004/moreinfo.html",
        "an_major": "产权交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "交易公告",
        "an_sub_url": "http://www.ajztb.com/jyxx/003005/003005001/moreinfo.html",
        "an_major": "产权交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "答疑澄清",
        "an_sub_url": "http://www.ajztb.com/jyxx/003005/003005003/moreinfo.html",
        "an_major": "产权交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "变更公告",
        "an_sub_url": "http://www.ajztb.com/jyxx/003005/003005002/moreinfo.html",
        "an_major": "产权交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "成交公示",
        "an_sub_url": "http://www.ajztb.com/jyxx/003007/003007004/moreinfo.html",
        "an_major": "小额交易项目"
    },
    {
        "an_sub": "NONE",
        "an_type": "开标结果公示",
        "an_sub_url": "http://www.ajztb.com/jyxx/003007/003007003/moreinfo.html",
        "an_major": "小额交易项目"
    },
    {
        "an_sub": "NONE",
        "an_type": "交易公告",
        "an_sub_url": "http://www.ajztb.com/jyxx/003007/003007001/moreinfo.html",
        "an_major": "小额交易项目"
    },
    {
        "an_sub": "NONE",
        "an_type": "答疑澄清",
        "an_sub_url": "http://www.ajztb.com/jyxx/003007/003007002/moreinfo.html",
        "an_major": "小额交易项目"
    },
    {
        "an_sub": "NONE",
        "an_type": "中标结果",
        "an_sub_url": "http://www.ajztb.com/jyxx/003007/003007005/moreinfo.html",
        "an_major": "小额交易项目"
    },
    {
        "an_sub": "NONE",
        "an_type": "结果公示",
        "an_sub_url": "http://www.ajztb.com/jyxx/003008/003008004/moreinfo.html",
        "an_major": "资源要素交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "交易公告",
        "an_sub_url": "http://www.ajztb.com/jyxx/003008/003008001/moreinfo.html",
        "an_major": "资源要素交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "答疑澄清",
        "an_sub_url": "http://www.ajztb.com/jyxx/003008/003008003/moreinfo.html",
        "an_major": "资源要素交易"
    },
    {
        "an_sub": "NONE",
        "an_type": "变更公告",
        "an_sub_url": "http://www.ajztb.com/jyxx/003008/003008002/moreinfo.html",
        "an_major": "资源要素交易"
    }
]
}

def main():
    return CRAWL_ANJI_TASKS