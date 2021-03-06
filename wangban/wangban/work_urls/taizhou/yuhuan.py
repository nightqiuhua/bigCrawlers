

CRAWL_YUHUAN_TASKS = {
    'name':'yuhuan',
    'source_url':'',
    'task_queue':'wangban:yuhuan:an_work_urls',
    'task_check':'wangban:yuhuan:an_check_urls',
    'html_type':'static',
    'tasks':[
    {'工程建设':{
    '项目信息':{'NONE':'https://www.yhjyzx.com/TransactionInfo/jsgc/xmdjxx',},
    '招标公告':{'NONE':'https://www.yhjyzx.com/BidNotice/jsgc/zbgg',},
    '澄清或修改公告':{'NONE':'https://www.yhjyzx.com/BidNotice/jsgc/bggg',},
    '开标结果公示':{'NONE':'https://www.yhjyzx.com/BidNotice/jsgc/kbqk',},
    '中标候选人公示':{'NONE':'https://www.yhjyzx.com/BidNotice/jsgc/zbhxrgs',},
    '中标公示':{'NONE':'https://www.yhjyzx.com/BidNotice/jsgc/zbjggg',},
    '保证金退款':{'NONE':'https://www.yhjyzx.com/BidNotice/jsgc/bzjtk',},
    '中标通知书':{'NONE':'https://www.yhjyzx.com/TransactionInfo/jsgc/zbtzs',},
    '合同公示':{'NONE':'https://www.yhjyzx.com/TransactionInfo/jsgc/ht',},
    '履约公告':{'NONE':'https://www.yhjyzx.com/TransactionInfo/jsgc/lyqk',},
    }},
    {'政府采购':{
    '项目信息':{'NONE':'https://www.yhjyzx.com/TransactionInfo/zfcg/xmxx',},
    '征求意见':{'NONE':'https://www.yhjyzx.com/BidNotice/zfcg/zqyj',},
    '采购公告':{'NONE':'https://www.yhjyzx.com/BidNotice/zfcg/cggg',},
    '变更公告':{'NONE':'https://www.yhjyzx.com/BidNotice/zfcg/bggg',},
    '开标结果公告':{'NONE':'https://www.yhjyzx.com/BidNotice/zfcg/kbjggg',},
    '成交候选人公示':{'NONE':'https://www.yhjyzx.com/BidNotice/zfcg/cjhxrgs',},
    '成交公告':{'NONE':'https://www.yhjyzx.com/BidNotice/zfcg/zbjggg',},
    '合同公告':{'NONE':'https://www.yhjyzx.com/BidNotice/zfcg/htgg',},
    '废标公告':{'NONE':'https://www.yhjyzx.com/BidNotice/zfcg/fbgg',},
    '履约公告':{'NONE':'https://www.yhjyzx.com/BidNotice/zfcg/lygg',},
    }},
    {'土地交易':{
    '项目信息':{'NONE':'https://www.yhjyzx.com/TransactionInfo/gtjy/xmxx',},
    '出让公告':{'NONE':'https://www.yhjyzx.com/BidNotice/gtjy/crgg',},
    '补充公告':{'NONE':'https://www.yhjyzx.com/BidNotice/gtjy/bcgg',},
    '成交结果公布':{'NONE':'https://www.yhjyzx.com/BidNotice/gtjy/cjjggb',},
    }},
    #{'国有产权交易':{
    #'交易指南':{'NONE':'http://www.yhjyzx.com:8070/jmr/index',},
    #'出让公告':{'NONE':'http://www.yhjyzx.com:8070/jmr/jump?num=2',},
    #'挂牌信息':{'NONE':'http://www.yhjyzx.com:8070/jmr/jump?num=3',},
    #'结果公示':{'NONE':'http://www.yhjyzx.com:8070/jmr/jump?num=4',},
    #'保证金退款':{'NONE':'http://www.yhjyzx.com:8070/jmr/jump?num=7',},
    #'履约公告':{'NONE':'http://www.yhjyzx.com:8070/jmr/jump?num=9',},
    #}},
    {'农村产权交易':{
    '项目信息':{'NONE':'https://www.yhjyzx.com/BidNotice/nccq/xmxx',},
    '招标(竞、拍、挂)公告':{'NONE':'https://www.yhjyzx.com/BidNotice/nccq/zbgg',},
    '更正公告':{'NONE':'https://www.yhjyzx.com/BidNotice/nccq/gzgg',},
    '成交候选人公示':{'NONE':'https://www.yhjyzx.com/BidNotice/nccq/cjhxrgs',},
    '成交公告':{'NONE':'https://www.yhjyzx.com/BidNotice/nccq/cjgg',},
    '履约公告':{'NONE':'https://www.yhjyzx.com/BidNotice/nccq/lygg',},
    }},
    {'排污权交易':{
    '项目信息':{'NONE':'https://www.yhjyzx.com/TransactionInfo/pwqjy/xmxx',},
    '招标(竞、拍、挂)公告':{'NONE':'https://www.yhjyzx.com/BidNotice/pwqjy/zbgg',},
    '更正公告':{'NONE':'https://www.yhjyzx.com/BidNotice/pwqjy/gzgg',},
    '成交候选人公示':{'NONE':'https://www.yhjyzx.com/BidNotice/pwqjy/cjhxrgs',},
    '成交公告':{'NONE':'https://www.yhjyzx.com/BidNotice/pwqjy/cjgg',},
    '履约公告':{'NONE':'https://www.yhjyzx.com/BidNotice/pwqjy/lygg',},
    }},
    {'国有企业物资采购':{
    '项目信息':{'NONE':'https://www.yhjyzx.com/BidNotice/gyqywzcg/xmxx',},
    '招标(竞、拍、挂)公告':{'NONE':'https://www.yhjyzx.com/BidNotice/gyqywzcg/zbgg',},
    '更正公告':{'NONE':'https://www.yhjyzx.com/BidNotice/gyqywzcg/gzgg',},
    '成交候选人公示':{'NONE':'https://www.yhjyzx.com/BidNotice/gyqywzcg/cjhxrgs',},
    '成交公告':{'NONE':'https://www.yhjyzx.com/BidNotice/gyqywzcg/cjgg',},
    '履约公告':{'NONE':'https://www.yhjyzx.com/BidNotice/gyqywzcg/lygg',},
    }},
    {'其它公共资源交易':{
    '项目信息':{'NONE':'https://www.yhjyzx.com/TransactionInfo/qtggzyjy/hysyq/xmxx',},
    '招标(竞、拍、挂)公告':{'NONE':'https://www.yhjyzx.com/BidNotice/qtggzyjy/hysyq/zbgg',},
    '更正公告':{'NONE':'https://www.yhjyzx.com/BidNotice/qtggzyjy/hysyq/gzgg',},
    '成交候选人公示':{'NONE':'https://www.yhjyzx.com/BidNotice/qtggzyjy/hysyq/cjhxrgs',},
    '成交公告':{'NONE':'https://www.yhjyzx.com/BidNotice/qtggzyjy/hysyq/cjgg',},
    '履约公告':{'NONE':'https://www.yhjyzx.com/BidNotice/qtggzyjy/hysyq/lygg',},
    }},
    {'乡镇平台交易信息':{
    '项目信息':{'NONE':'https://www.yhjyzx.com/TransactionInfo/Qtxm/xmxx',},
    '招标(竞、拍、挂)公告':{'NONE':'https://www.yhjyzx.com/BidNotice/Qtxm/xxgg',},
    '更正公告':{'NONE':'https://www.yhjyzx.com/BidNotice/Qtxm/gzgg',},
    '成交候选人公示':{'NONE':'https://www.yhjyzx.com/BidNotice/Qtxm/cjhxrgs',},
    '成交公告':{'NONE':'https://www.yhjyzx.com/BidNotice/Qtxm/cjgg',},
    '履约公告':{'NONE':'https://www.yhjyzx.com/BidNotice/Qtxm/lygg',},
    }},
    {'部门自行交易信息':{
    '项目信息':{'NONE':'https://www.yhjyzx.com/TransactionInfo/bmzb/xmxx',},
    '招标(竞、拍、挂)公告':{'NONE':'https://www.yhjyzx.com/BidNotice/bmzb/zbgg',},
    '更正公告':{'NONE':'https://www.yhjyzx.com/BidNotice/bmzb/gzgg',},
    '成交候选人公示':{'NONE':'https://www.yhjyzx.com/BidNotice/bmzb/cjhxrgs',},
    '成交公告':{'NONE':'https://www.yhjyzx.com/BidNotice/bmzb/cjgg',},
    '履约公告':{'NONE':'https://www.yhjyzx.com/BidNotice/bmzb/lygg',},
    }},
    ]
}

def main():
    return CRAWL_YUHUAN_TASKS