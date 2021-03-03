

CRAWL_JIANDE_TASKS = {
    'name':'jiande',
    'source_url':'http://www.jdggzy.com/index.aspx',
    'task_queue':'wangban:jiande:an_url_works',
    'task_ajax':'wangban:jiande:an_url_ajax',
    'task_check':'wangban:jiande:an_url_check',
    'html_type':'ajax',
    'tasks':[
    {
        "an_major": "工程建设",
        "an_sub_url": "http://www.jdggzy.com/ProArticle/ProArticleList.aspx?ViewID=312&AfficheType=17",
        "an_sub": "NONE",
        "an_type": "通知答疑"
    },
    {
        "an_major": "工程建设",
        "an_sub_url": "http://www.jdggzy.com/web_news/ProCommonList.aspx?&ViewID=311&AfficheType=",
        "an_sub": "NONE",
        "an_type": "开标实况"
    },
    {
        "an_major": "工程建设",
        "an_sub_url": "http://www.jdggzy.com/ProArticle/ProArticleList.aspx?ViewID=310&AfficheType=18",
        "an_sub": "NONE",
        "an_type": "中标公示"
    },
    {
        "an_major": "工程建设",
        "an_sub_url": "http://www.jdggzy.com/ProArticle/ProArticleList.aspx?ViewID=313&AfficheType=23",
        "an_sub": "NONE",
        "an_type": "废标公告"
    },
    {
        "an_major": "工程建设",
        "an_sub_url": "http://www.jdggzy.com/ProArticle/ProArticleList.aspx?ProClass=95&ViewID=309&AfficheType=2",
        "an_sub": "NONE",
        "an_type": "招标公告"
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.jdggzy.com/ProArticle/ProArticleList.aspx?ViewID=318&AfficheType=104",
        "an_sub": "NONE",
        "an_type": "中标公示 "
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.jdggzy.com/ProArticle/ProArticleList.aspx?ViewID=316&AfficheType=103",
        "an_sub": "NONE",
        "an_type": "通知答疑 "
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.jdggzy.com/ProArticle/ProArticleList.aspx?ViewID=317&AfficheType=190",
        "an_sub": "NONE",
        "an_type": "废标公告 "
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.jdggzy.com/ProArticle/ProArticleList.aspx?ProClass=95&ViewID=315&AfficheType=102",
        "an_sub": "NONE",
        "an_type": "招标公告 "
    },
    {
        "an_major": "产权交易",
        "an_sub_url": "http://www.jdggzy.com/ProArticle/ProArticleList.aspx?ViewID=428&AfficheType=139",
        "an_sub": "NONE",
        "an_type": "产权公告 "
    },
    {
        "an_major": "产权交易",
        "an_sub_url": "http://www.jdggzy.com/web_news/ProArrangeList.aspx?TradeType=389&ViewID=339&AfficheType=",
        "an_sub": "NONE",
        "an_type": "开标实况"
    },
    {
        "an_major": "产权交易",
        "an_sub_url": "http://www.jdggzy.com/ProArticle/ProArticleList.aspx?ViewID=341&AfficheType=141",
        "an_sub": "NONE",
        "an_type": "中标公示 "
    },
    {
        "an_major": "土地矿产交易",
        "an_sub_url": "http://www.jdggzy.com/ProArticle/ProArticleList.aspx?ViewID=326&AfficheType=145",
        "an_sub": "NONE",
        "an_type": "通知答疑"
    },
    {
        "an_major": "土地矿产交易",
        "an_sub_url": "http://www.jdggzy.com/ProArticle/ProArticleList.aspx?ViewID=328&AfficheType=146",
        "an_sub": "NONE",
        "an_type": "中标公示"
    },
    {
        "an_major": "土地矿产交易",
        "an_sub_url": "http://www.jdggzy.com/web_news/ProArrangeList.aspx?TradeType=388&ViewID=327&AfficheType=",
        "an_sub": "NONE",
        "an_type": "开标实况"
    },
    {
        "an_major": "土地矿产交易",
        "an_sub_url": "http://www.jdggzy.com/ProArticle/ProArticleList.aspx?ViewID=325&AfficheType=144",
        "an_sub": "NONE",
        "an_type": "招标公告"
    },
    {
        "an_major": "分中心平台",
        "an_sub_url": "http://www.jdggzy.com/ProArticle/ProArticleList_xe.aspx?ViewID=346&AfficheType=148",
        "an_sub": "NONE",
        "an_type": "更正公告"
    },
    {
        "an_major": "分中心平台",
        "an_sub_url": "http://www.jdggzy.com/ProArticle/ProArticleList_xe.aspx?ViewID=347&AfficheType=149",
        "an_sub": "NONE",
        "an_type": "中标公示"
    },
    {
        "an_major": "分中心平台",
        "an_sub_url": "http://www.jdggzy.com/ProArticle/ProArticleList_xe.aspx?ViewID=348&AfficheType=150",
        "an_sub": "NONE",
        "an_type": "废标公告"
    },
    {
        "an_major": "分中心平台",
        "an_sub_url": "http://www.jdggzy.com/ProArticle/ProArticleList_xe.aspx?ViewID=345&AfficheType=147",
        "an_sub": "NONE",
        "an_type": "招标公告"
    }
]
}

def main():
    return CRAWL_JIANDE_TASKS