#construction:建设工程
#con_source_url:建筑工程源链接
#con_invite_url:建筑工程招标源链接
#con_supplement_url:建筑工程补充通知源链接
#con_open_url:开标结果公告(建筑工程开标实况源链接)
#con_candidate_url:建筑工程候选人源链接
#con_win_url:建筑工程中标源链接
#con_petty_url:建筑工程小额源链接
#con_petty_dis:小额发包
#con_petty_supplement:小额补充通知
#con_petty_res:小额发包结果
#con_recognized:招标范围、招标方式、招标组织形式认定
#con_modify:澄清或修改公告
#con_contract: 合同公告
#con_check: 履约验收公告
#
#'goverment':政府采购
#'gov_source':政府采购源链接
#'gov_purchase':政府采购招标源链接,
#'gov_modify':政府采购更改通知源链接,
#'gov_candidate':政府采购候选人源链接,
#'gov_win':政府采购中标源链接,
#'gov_contract':政府采购合同源链接,
# gov_ne_for_comp:竞争性谈判公告
# gov_ask:询价公告
# gov_stop:中止（暂停）公告
# gov_clear:澄清（修改）公告
# gov_terminal:采购终止公告
# gov_result_change: 采购结果变更公告
# gov_for_public:政府向社会公众提供的公共服务项目履约验收公告
# gov_for_complacement:投诉、监督检查等处理（罚）决定公告

#'property':产权交易
#'pro_source':产权源链接
#'pro_transaction':招租公告(产权交易源链接)
#'pro_supplement':产权交易补充源链接
#'pro_deal':产权交易成交源链接,
#'pro_modify': 更正（竞价会取消、项目中止等）公告
#
#'land':国土
#'land_source':国土源链接
#'land_transaction':国土交易源链接
#'land_supplement':国土补充源链接
#'land_deal':国土成交源链接
#
#'others':其他
#'other_source':其他源链接
#'other_transaction':其他交易源链接
#'other_supplement':其他补充源链接
#'other_deal':其他成交源链接
#
#
#petty:小额公共资源交易
#petty_invite招标(采购)公告
#petty_open开标
#petty_modify澄清、修改公告
#petty_candidate中标候选人公示
#petty_win中标公告
#petty_condition合同订立及履约情况



CRAWL_LUQIAO_TASKS = {
    'name':'luqiao',
    'source_url':'',
    'task_queue':'wangban:luqiao:an_work_urls',
    'task_check':'wangban:luqiao:an_check_urls',
    'html_type':'static',
    'tasks':[
    {'政府采购':{
    '招标公告':{'NONE':'http://www.luqiao.gov.cn/InfoPub/ArticleList.aspx?CategoryID=528',},
    '中标公告':{'NONE':'http://www.luqiao.gov.cn/InfoPub/ArticleList.aspx?CategoryID=526',},
    '采购政策、资料及其他':{'NONE':'http://www.luqiao.gov.cn/InfoPub/ArticleList.aspx?CategoryID=523',},
    }},
    {'农村产权交易平台':{
    'NONE':{'NONE':'http://www.luqiao.gov.cn/InfoPub/ArticleList.aspx?CategoryID=3007',},
    }},
    ]
}

def main():
    return CRAWL_LUQIAO_TASKS