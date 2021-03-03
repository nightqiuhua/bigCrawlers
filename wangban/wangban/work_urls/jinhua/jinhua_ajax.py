
CRAWL_JINHUA_AJAX_TASKS = {
    'name':'jinhua_ajax',
    'source_url':'',
    'task_queue':'wangban:jinhua_ajax:an_work_urls',
    'task_check':'wangban:jinhua_ajax:an_check_urls',
    'task_ajax':'wangban:jinhua_ajax:an_ajax_urls',
    'html_type':'static',
    'tasks':[
    {
        "an_major": "工程建设",
        "an_sub_url": "http://ggzyjy.jinhua.gov.cn/platform/noticeController.do?getNoticeList&type=qualifyBulletin&area=&page=0",
        "an_type": "资格预审公告",
        "an_sub": "县市分中心"
    },
    {
        "an_major": "工程建设",
        "an_sub_url": "http://ggzyjy.jinhua.gov.cn/platform/noticeController.do?getNoticeList&type=tenderBulletin&area=&page=0",
        "an_type": "招标公告",
        "an_sub": "县市分中心"
    },
    {
        "an_major": "工程建设",
        "an_sub_url": "http://ggzyjy.jinhua.gov.cn/platform/noticeController.do?getNoticeList&type=winCandidateBulletin&area=&page=0",
        "an_type": "中标候选人公示",
        "an_sub": "县市分中心"
    },
    {
        "an_major": "工程建设",
        "an_sub_url": "http://ggzyjy.jinhua.gov.cn/platform/noticeController.do?getNoticeList&type=openBidRecord&area=&page=0",
        "an_type": "开标记录",
        "an_sub": "县市分中心"
    },
    {
        "an_major": "工程建设",
        "an_sub_url": "http://ggzyjy.jinhua.gov.cn/platform/noticeController.do?getNoticeList&type=winBidBulletin&area=&page=0",
        "an_type": "中标公示",
        "an_sub": "县市分中心"
    },
    {
        "an_major": "工程建设",
        "an_sub_url": "http://ggzyjy.jinhua.gov.cn/platform/noticeController.do?getNoticeList&type=openBidList&area=&page=0",
        "an_type": "开标明细",
        "an_sub": "县市分中心"
    },
    {
        "an_major": "土地市场",
        "an_sub_url": "http://ggzyjy.jinhua.gov.cn/platform/noticeController.do?getNoticeList&type=dealConfirm&area=&page=0",
        "an_type": "土地出让结果",
        "an_sub": "县市分中心"
    },
    {
        "an_major": "土地市场",
        "an_sub_url": "http://ggzyjy.jinhua.gov.cn/platform/noticeController.do?getNoticeList&type=sell&area=&page=0",
        "an_type": "土地招拍挂信息公告",
        "an_sub": "县市分中心"
    },
    {
        "an_major": "其他交易",
        "an_sub_url": "http://ggzyjy.jinhua.gov.cn/platform/noticeController.do?getNoticeList&type=OTHER_TRADE_PUB_INFO&area=&page=0",
        "an_type": "公告信息",
        "an_sub": "县市分中心"
    },
    {
        "an_major": "其他交易",
        "an_sub_url": "http://ggzyjy.jinhua.gov.cn/platform/noticeController.do?getNoticeList&type=OTHER_TRADE_RESULT_INFO&area=&page=0",
        "an_type": "结果信息",
        "an_sub": "县市分中心"
    },
    {
        "an_major": "产权交易",
        "an_sub_url": "http://ggzyjy.jinhua.gov.cn/platform/noticeController.do?getNoticeList&type=dealNotice&area=&page=0",
        "an_type": "评标公示",
        "an_sub": "县市分中心"
    },
    {
        "an_major": "产权交易",
        "an_sub_url": "http://ggzyjy.jinhua.gov.cn/platform/noticeController.do?getNoticeList&type=announcement&area=&page=0",
        "an_type": "招标公告",
        "an_sub": "县市分中心"
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://ggzyjy.jinhua.gov.cn/platform/noticeController.do?getNoticeList&type=zhongBiaoResultZFCG&area=&page=0",
        "an_type": "中标成交公告",
        "an_sub": "县市分中心"
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://ggzyjy.jinhua.gov.cn/platform/noticeController.do?getNoticeList&type=caiGouGGZFCG&area=&page=0",
        "an_type": "采购公告",
        "an_sub": "县市分中心"
    }
]
}

def main():
    return CRAWL_JINHUA_AJAX_TASKS