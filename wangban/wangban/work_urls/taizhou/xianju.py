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



CRAWL_XIANJU_TASKS = {
    'name':'xianju',
    'source_url':'',
    'task_queue':'wangban:xianju:an_work_urls',
    'task_check':'wangban:xianju:an_check_urls',
    'html_type':'static',
    'tasks':[
    {'工程建设':{
    '招标公告':{'NONE':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?BulletinTypeId=11',},
    '中标公示':{'NONE':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?BulletinTypeId=12',},
    '补充公告':{'NONE':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?BulletinTypeId=13',},
    '退保证金公告':{'NONE':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?BulletinTypeId=14',},
    '中标公告':{'NONE':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?BulletinTypeId=15',},
    '资格预审结果公示':{'NONE':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?frontid=1&BulletinTypeId=16',},
    }},
    {'政府采购':{
    '采购公告':{'集中采购':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?BulletinTypeId=21',},
    '结果公告':{'集中采购':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?BulletinTypeId=22',},
    '补充公告':{'集中采购':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?frontid=2&BulletinTypeId=23',},
    '合同公告':{'集中采购':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?BulletinTypeId=25',},
    '征求意见':{'集中采购':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?BulletinTypeId=28',},
    }},
    {'土地出让':{
    '出让公告':{'NONE':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?BulletinTypeId=31',},
    '成交公告':{'NONE':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?BulletinTypeId=32',},
    }},
    {'其他交易':{
    '交易公告':{'NONE':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?BulletinTypeId=51',},
    '结果公示':{'NONE':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?BulletinTypeId=52',},
    '补充公告':{'NONE':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?BulletinTypeId=53',},
    '征求意见':{'NONE':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?frontid=5&BulletinTypeId=58',},
    }},
    {'政府采购':{
    '采购公告':{'分散采购':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?BulletinTypeId=61',},
    '成交公告':{'分散采购':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?BulletinTypeId=62',},
    '补充公告':{'分散采购':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?BulletinTypeId=63',},
    '合同公告':{'分散采购':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?frontid=6&BulletinTypeId=65',},
    '征求意见':{'分散采购':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?BulletinTypeId=68',},
    }},
    {'产权交易':{
    '出让公告':{'NONE':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?BulletinTypeId=41',},
    '成交公告':{'NONE':'http://www.xjztb.cn/Bulletin/viewmore1.aspx?BulletinTypeId=42',},
    }}
    ]
}

def main():
    return CRAWL_XIANJU_TASKS