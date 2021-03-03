
CRAWL_WENLING_TASKS = {
    'name':'wenling',
    'source_url':'',
    'task_queue':'wangban:wenling:an_work_urls',
    'task_check':'wangban:wenling:an_url_check',
    'task_ajax':'wangban:wenling:an_url_ajax',
    'html_type':'ajax',
    'tasks':[
    {'工程建设':{
    '招标公告':{'NONE':'http://new.wl.gov.cn/col/col1456441/index.html',},
    '答疑公告':{'NONE':'http://new.wl.gov.cn/col/col1456443/index.html',},
    '资格预审结果公示':{'NONE':'http://new.wl.gov.cn/col/col1456445/index.html',},
    '开标结果公告':{'NONE':'http://new.wl.gov.cn/col/col1622986/index.html',},
    '中标公示':{'NONE':'http://new.wl.gov.cn/col/col1456442/index.html',},
    '中标结果公告':{'NONE':'http://new.wl.gov.cn/col/col1456444/index.html',},
    '合同公告':{'NONE':'http://new.wl.gov.cn/col/col1622988/index.html',},
    }},
    {'政府采购':{
    '采购公告':{
            '集中采购':'http://new.wl.gov.cn/col/col1456446/index.html',
            '分散,国企':'http://new.wl.gov.cn/col/col1456451/index.html',
            },
    '采购结果公告':{
            '集中采购':'http://new.wl.gov.cn/col/col1456447/index.html',
            '分散,国企':'http://new.wl.gov.cn/col/col1456452/index.html',
            },
    '补充变更公告':{
            '集中采购':'http://new.wl.gov.cn/col/col1456448/index.html',
            '分散,国企':'http://new.wl.gov.cn/col/col1456453/index.html',
            },
    '合同公告':{
            '集中采购':'http://new.wl.gov.cn/col/col1456449/index.html',
            '分散,国企':'http://new.wl.gov.cn/col/col1622994/index.html',
            },
    '征求意见':{
            '集中采购':'http://new.wl.gov.cn/col/col1456450/index.html',
            },
    '开标结果公告':{
            '集中采购':'http://new.wl.gov.cn/col/col1622990/index.html',
            },
    }},
    {'土地交易':{
    '出让公告':{'NONE':'http://new.wl.gov.cn/col/col1456454/index.html',},
    '结果公告':{'NONE':'http://new.wl.gov.cn/col/col1456455/index.html',},
    '其他公告':{'NONE':'http://new.wl.gov.cn/col/col1456456/index.html',},
    }},
    {'其他交易':{
    '交易公告':{'NONE':'http://new.wl.gov.cn/col/col1456462/index.html',},
    '结果公告':{'NONE':'http://new.wl.gov.cn/col/col1456463/index.html',},
    }},
    {'国有产权交易':{
    '交易公告':{'NONE':'http://new.wl.gov.cn/col/col1456457/index.html',},
    '结果公告':{'NONE':'http://new.wl.gov.cn/col/col1456458/index.html',},
    '补充公告':{'NONE':'http://new.wl.gov.cn/col/col1456459/index.html',},
    }},
    {'镇街公告':{
    '招标公告':{'NONE':'http://new.wl.gov.cn/col/col1456464/index.html',},
    '澄清或修改公告':{'NONE':'http://new.wl.gov.cn/col/col1619676/index.html',},
    '中标公示':{'NONE':'http://new.wl.gov.cn/col/col1456465/index.html',},
    '中标结果公告':{'NONE':'http://new.wl.gov.cn/col/col1621639/index.html',},
    }},
    ]
}

def main():
    return CRAWL_WENLING_TASKS