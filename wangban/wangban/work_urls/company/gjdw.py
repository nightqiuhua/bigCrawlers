#国家电网有限公司电子商务平台
CRAWL_GJDW_TASKS = {
    'name':'gjdw',
    'source_url':'',
    'html_type':'static',
    'tasks':[
    {
        "an_sub": "NONE",
        "an_sub_url": "http://ecp.sgcc.com.cn/topic_project_list.jsp?columnName=topic10&site=global&company_id=&status=&project_name=&pageNo=1",
        "an_county": "NONE",
        "an_type": "招标公告",
        "an_major": "NONE"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://ecp.sgcc.com.cn/topic_news_list.jsp?columnName=topic21&site=global&company_id=&column_code1=014001008&column_code2=014002008&pageNo=1",
        "an_county": "NONE",
        "an_type": "非招标公告",
        "an_major": "NONE"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://ecp.sgcc.com.cn/topic_news_list.jsp?columnName=topic22&site=global&company_id=&column_code1=014001003&column_code2=014002009&pageNo=1",
        "an_county": "NONE",
        "an_type": "推荐的中标候选人公示",
        "an_major": "NONE"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://ecp.sgcc.com.cn/topic_news_list.jsp?columnName=topic23&site=global&company_id=&column_code1=014001007&column_code2=014002003&pageNo=1",
        "an_county": "NONE",
        "an_type": "中标（成交）结果公告",
        "an_major": "NONE"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://ecp.sgcc.com.cn/topic_news_list.jsp?columnName=topic24&site=global&company_id=&column_code1=014001005&column_code2=014002006&pageNo=1",
        "an_county": "NONE",
        "an_type": "否决公告",
        "an_major": "NONE"
    },
    {
        "an_sub": "NONE",
        "an_sub_url": "http://ecp.sgcc.com.cn/topic_announcement_list.jsp?columnName=topic40&site=global&column_code=019001&company_id=&pageNo=1",
        "an_county": "NONE",
        "an_type": "竞价公告",
        "an_major": "NONE"
    },
    ]

}

def main():
    return CRAWL_GJDW_TASKS