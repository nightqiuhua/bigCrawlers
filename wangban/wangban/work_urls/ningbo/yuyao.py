
#国有产权交易
#政府采购
CRAWL_YUYAO_TASKS = {
    'name':'yuyao',
    'source_url':'',
    'task_queue':'wangban:yuyao:an_work_urls',
    'task_check':'wangban:yuyao:an_url_check',
    'html_type':'static',
    'tasks':[
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "保证金退款",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yybzjtk/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "乡镇平台交易信息",
        "an_major": "工程建设",
        "an_type": "中标候选人公示",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zbhxrgs/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "中标候选人公示",
        "an_sub_url": "http://yuyao.bidding.gov.cn/gcjszbhxrgs/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "乡镇平台交易信息",
        "an_major": "工程建设",
        "an_type": "资格入围结果",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yyzgrwjg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "资格入围结果",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yyzgrwqk/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "年度保证金单位",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yyndbzjdw/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "乡镇平台交易信息",
        "an_major": "工程建设",
        "an_type": "中标结果公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yyzbjggg1/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "中标结果公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/fhzbjggg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "乡镇平台交易信息",
        "an_major": "工程建设",
        "an_type": "招标公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yyzbgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "招标公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/gcjszbgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "乡镇平台交易信息",
        "an_major": "工程建设",
        "an_type": "变更公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yybggg1/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "变更公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yygcbggg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "乡镇平台交易信息",
        "an_major": "工程建设",
        "an_type": "开标情况",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yykbqk1/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "工程建设",
        "an_type": "开标情况",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yygckbqk/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "采购文件需求公示",
        "an_major": "政府采购",
        "an_type": "意见征询",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxyjzxcgwj/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "允许采购进口产品公示",
        "an_major": "政府采购",
        "an_type": "意见征询",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxyjzxyxjk/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "单一来源公示",
        "an_major": "政府采购",
        "an_type": "意见征询",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxyjzxdyly/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "其他意见征询公告",
        "an_major": "政府采购",
        "an_type": "意见征询",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxyjzxqtyj/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "其他履约验收公告",
        "an_major": "政府采购",
        "an_type": "履约验收公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxlyysggqtgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "履约验收公告（服务类）",
        "an_major": "政府采购",
        "an_type": "履约验收公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxlyysgglygg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "其他监管公告",
        "an_major": "政府采购",
        "an_type": "政府采购监管公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxzcjgqtgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "监督检查公告",
        "an_major": "政府采购",
        "an_type": "政府采购监管公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxzcjgjdjc/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "行政处罚信息公告",
        "an_major": "政府采购",
        "an_type": "政府采购监管公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxzcjgxzcf/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "供应商、采购代理机构和评审专家的违法失信行为记录公告",
        "an_major": "政府采购",
        "an_type": "政府采购监管公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxzcjggys/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "投诉处理信息公告",
        "an_major": "政府采购",
        "an_type": "政府采购监管公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxzcjgtsgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "集中采购机构考核结果公告",
        "an_major": "政府采购",
        "an_type": "政府采购监管公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxzcjgjzcg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "行政处理信息公告",
        "an_major": "政府采购",
        "an_type": "政府采购监管公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxzcjgxzcl/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "竞争性谈判公告",
        "an_major": "政府采购",
        "an_type": "采购项目公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxcgxmggjzxtp/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "其他采购项目公告",
        "an_major": "政府采购",
        "an_type": "采购项目公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxcgxmggqtcg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "公开招标资格预审公告",
        "an_major": "政府采购",
        "an_type": "采购项目公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxcgxmgggkys/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "询价公告",
        "an_major": "政府采购",
        "an_type": "采购项目公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxcgxmggxj/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "乡镇平台交易信息",
        "an_major": "政府采购",
        "an_type": "采购项目公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yyzbgg1/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "公开招标公告",
        "an_major": "政府采购",
        "an_type": "采购项目公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxcgxmgggkzb/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "邀请招标资格预审公告",
        "an_major": "政府采购",
        "an_type": "采购项目公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxcgxmggyqzb/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "竞争性磋商公告",
        "an_major": "政府采购",
        "an_type": "采购项目公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxcgxmggjzxcs/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "澄清(修改)公告",
        "an_major": "政府采购",
        "an_type": "更正公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxgzggcqgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "更正公告",
        "an_major": "政府采购",
        "an_type": "更正公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxgzgggzgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "其他更正公告",
        "an_major": "政府采购",
        "an_type": "更正公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxgzggqtgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "中止(暂停)公告",
        "an_major": "政府采购",
        "an_type": "更正公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxgzggzzgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "其他采购合同公告",
        "an_major": "政府采购",
        "an_type": "采购合同公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxcghtggqtgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "采购合同公告",
        "an_major": "政府采购",
        "an_type": "采购合同公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxcghtgghtgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "采购结果变更公告",
        "an_major": "政府采购",
        "an_type": "采购结果公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxcgjgggbggg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "中标（成交）结果公告",
        "an_major": "政府采购",
        "an_type": "采购结果公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxcgjgggzbgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "乡镇平台交易信息",
        "an_major": "政府采购",
        "an_type": "采购结果公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yyzbgs/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "终止公告",
        "an_major": "政府采购",
        "an_type": "采购结果公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxcgjgggzzgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "公开招标资格入围公告",
        "an_major": "政府采购",
        "an_type": "采购结果公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxcgjggggkrw/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "废标公告",
        "an_major": "政府采购",
        "an_type": "采购结果公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxcgjgggfbgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "其他采购结果公告",
        "an_major": "政府采购",
        "an_type": "采购结果公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxcgjgggqtgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "邀请招标资格入围公告",
        "an_major": "政府采购",
        "an_type": "采购结果公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxcgjgggyqzb/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "电子卖场公告",
        "an_type": "在线询价公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxdzmcggzxxj/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "电子卖场公告",
        "an_type": "定点服务结果公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxdzmcggddfw/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "电子卖场公告",
        "an_type": "电子卖场采购公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxdzmcggdzmccggg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "电子卖场公告",
        "an_type": "反向竞价结果公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxdzmcggfxjjjg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "电子卖场公告",
        "an_type": "协议定点项目采购结果更正公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxdzmcggxyddjggzgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "电子卖场公告",
        "an_type": "电子卖场合同公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxdzmcggdzmcht/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "电子卖场公告",
        "an_type": "其他电子卖场采购公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxdzmcggqtgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "电子卖场公告",
        "an_type": "电子卖场终止公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxdzmcggdzmczz/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "电子卖场公告",
        "an_type": "电子卖场成交公告（采购成功）",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxdzmcggcgcggg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "电子卖场公告",
        "an_type": "电子卖场中止（暂停）公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxdzmcggdzmczzgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "电子卖场公告",
        "an_type": "电子卖场成交公告（采购失败）",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxdzmcggcgsbgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "电子卖场公告",
        "an_type": "协议定点项目更正公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxdzmcggxyddgzgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "电子卖场公告",
        "an_type": "协议定点项目中标公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxdzmcggxyddzhongbgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "电子卖场公告",
        "an_type": "在线询价结果公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxdzmcggzxxjjg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "电子卖场公告",
        "an_type": "协议定点项目招标公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxdzmcggxyddzbgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "电子卖场公告",
        "an_type": "反向竞价公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxdzmcggfxjj/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "非政府采购公告",
        "an_type": "国库现金管理招标公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxfzfcgguokzbgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "非政府采购公告",
        "an_type": "国库现金管理更正公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxfzfcgguokgzgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "非政府采购公告",
        "an_type": "公款竞争性存放招标公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxfzfcggkzbgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "非政府采购公告",
        "an_type": "其他非政府采购项目结果公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxfzfcgqtjggg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "非政府采购公告",
        "an_type": "其他非政府采购项目意见征询",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxfzfcgqtyjzx/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "非政府采购公告",
        "an_type": "公款竞争性存放更正公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxfzfcggkgzgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "非政府采购公告",
        "an_type": "其他非政府采购项目更正公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxfzfcgqtgzgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "非政府采购公告",
        "an_type": "国库现金管理中标公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxfzfcgguokzhongbgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "非政府采购公告",
        "an_type": "公款竞争性存放意见征询",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxfzfcggkyjzx/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "非政府采购公告",
        "an_type": "其他非政府采购项目合同公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxfzfcgqthtgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "非政府采购公告",
        "an_type": "公款竞争性存放结果公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxfzfcggkjggg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "非政府采购公告",
        "an_type": "其他非政府采购公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxfzfcgqtgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "非政府采购公告",
        "an_type": "其他非政府采购项目招标公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/zcbxfzfcgqtzbgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "土地交易",
        "an_type": "数据统计",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yysjtj/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "土地交易",
        "an_type": "出让公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/tdjycrgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "NONE",
        "an_major": "土地交易",
        "an_type": "出让结果公示",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yycjgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "乡镇(农村)产权交易",
        "an_major": "产权交易",
        "an_type": "中标结果公示",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yyjggg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "乡镇(农村)产权交易",
        "an_major": "产权交易",
        "an_type": "出让公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yycrgg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "公共资源交易",
        "an_major": "其他交易",
        "an_type": "开标情况",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yykbqk/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "公共资源交易",
        "an_major": "其他交易",
        "an_type": "中标结果公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yyzbjggg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "公共资源交易",
        "an_major": "其他交易",
        "an_type": "采购合同",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yycght/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "其他交易",
        "an_major": "其他交易",
        "an_type": "中标候选人情况",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yyzbhxrgs/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "公共资源交易",
        "an_major": "其他交易",
        "an_type": "中标候选人情况",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yyzbhxrqk/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "其他交易",
        "an_major": "其他交易",
        "an_type": "采购公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yyzbgg2/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "公共资源交易",
        "an_major": "其他交易",
        "an_type": "采购公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yycggg/index.jhtml?areaCode=330281"
    },
    {
        "an_sub": "公共资源交易",
        "an_major": "其他交易",
        "an_type": "变更公告",
        "an_sub_url": "http://yuyao.bidding.gov.cn/yybggg/index.jhtml?areaCode=330281"
    }
]
}

def main():
    return CRAWL_YUYAO_TASKS