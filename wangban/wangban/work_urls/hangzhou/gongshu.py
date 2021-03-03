

CRAWL_GONGSHU_TASKS = {
    'name':'gongshu',
    'source_url':'http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmForPublic.action',
    'task_queue':'wangban:gongshu:an_url_works',#用于存放静态网页的url
    'task_ajax':'wangban:gongshu:an_url_ajax',#用于存放动态网页的url
    'task_check':'wangban:gongshu:an_url_check',#检查队列，用于检查url是否过期，以及是否重复。所有url都会经过该队列
    'html_type':'ajax',
    'tasks':[
    {
        "an_major": "建设工程",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=0E0AAE46433C4519A3C6C3556228536F",
        "an_sub": "资格后审",
        "an_type": "招标"
    },
    {
        "an_major": "建设工程",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=FE52B41C91634FC59248303507CB6D57",
        "an_sub": "资格预审",
        "an_type": "招标"
    },
    {
        "an_major": "建设工程",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=306DE1E768FF4C83B655280C46C0146D",
        "an_sub": "None",
        "an_type": "澄清或修改公告"
    },
    {
        "an_major": "建设工程",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=A63286176A2145578934B02A26F999E0",
        "an_sub": "None",
        "an_type": "开标结果公告"
    },
    {
        "an_major": "建设工程",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=87D397B243A744E9BED6EF540AD9D4AC",
        "an_sub": "None",
        "an_type": "履约验收公告"
    },
    {
        "an_major": "建设工程",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=B4B9F0DAABB94229A1D3C754073A8B05",
        "an_sub": "None",
        "an_type": "中标"
    },
    {
        "an_major": "建设工程",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=C9CCD00B0A834C1685AA0F8A1E0614D3",
        "an_sub": "None",
        "an_type": "候选人"
    },
    {
        "an_major": "建设工程",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=B1AABE5EBAF04E418E0EC06940E89396",
        "an_sub": "建设项目代建类",
        "an_type": "招标范围、招标方式、招标组织形式认定"
    },
    {
        "an_major": "建设工程",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=A1D35924B0594C0BB9015018A9A9E970",
        "an_sub": "勘察、设计类",
        "an_type": "招标范围、招标方式、招标组织形式认定"
    },
    {
        "an_major": "建设工程",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=5FA097F4501D43E79D24AFF6C8391AF2",
        "an_sub": "施工类",
        "an_type": "招标范围、招标方式、招标组织形式认定"
    },
    {
        "an_major": "建设工程",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=0A78435F7C634475A9823FA5E5AED01D",
        "an_sub": "监理类",
        "an_type": "招标范围、招标方式、招标组织形式认定"
    },
    {
        "an_major": "建设工程",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=4DFC68819A554DE5955D9A09EE7F6A58",
        "an_sub": "None",
        "an_type": "合同公告"
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=F2BB2907660E4FD083E68801C4C6968D",
        "an_sub": "None",
        "an_type": "询价公告"
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=408902396B474A228AD69BE64773BF4E",
        "an_sub": "None",
        "an_type": "成交结果公告"
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=308FC2F7EFCB415189F2786CFF7243A3",
        "an_sub": "None",
        "an_type": "采购文件意见征询"
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=1C3F0223908B4A5E816A364F96F92FE8",
        "an_sub": "None",
        "an_type": "政府采购合同"
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=910EBABC3E824F3BB826B2342823CD48",
        "an_sub": "None",
        "an_type": "采购结果变更公告"
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=8E90BE4955F443E6A7BF22C0979D1552",
        "an_sub": "None",
        "an_type": "政府向社会公众提供的公共服务项目履约验收公告"
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=F4F0F98C0CBD43178A0B81D91670B6C4",
        "an_sub": "None",
        "an_type": "竞争性磋商公告"
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=3AFC91B2B3C0413D8036F85144991129",
        "an_sub": "None",
        "an_type": "竞争性谈判公告"
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=F9161F21EAAA4D678A2E222B9F06A2C8",
        "an_sub": "None",
        "an_type": "采购终止公告"
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=9370A552C56B410AA3C9E3B6BB63C263",
        "an_sub": "None",
        "an_type": "中止（暂停）公告"
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=97FADD9AFF5247939BF4D39C5FF00D6B",
        "an_sub": "None",
        "an_type": "政府采购招标"
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=09982DF401C643B9A93C4A15DC36DA62",
        "an_sub": "None",
        "an_type": "政府采购更改通知"
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=DFB3331959B24CDCA3396DA96F777EDE",
        "an_sub": "None",
        "an_type": "投诉、监督检查等处理（罚）决定公告"
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=F3B5EC63D5734A15BAD42D60B6EF9C7C",
        "an_sub": "None",
        "an_type": "澄清（修改）公告"
    },
    {
        "an_major": "政府采购",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=A830B7C52CA841B8A8282807017029AC",
        "an_sub": "None",
        "an_type": "单一来源公示"
    },
    {
        "an_major": "产权交易",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=8D472DC7A3AE4030ABF8920397FB1784",
        "an_sub": "None",
        "an_type": "产权交易成交"
    },
    {
        "an_major": "产权交易",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=2A997C3C018B40BC8372A061F0A6A3A1",
        "an_sub": "None",
        "an_type": "更正（竞价会取消、项目中止等）公告"
    },
    {
        "an_major": "产权交易",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=EE9F9C74DAB840AAAB5E4C0233585AC9",
        "an_sub": "None",
        "an_type": "招租公告"
    },
    {
        "an_major": "小额公共资源交易",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=D39B055458904DEFBF4CFA9BD0221993",
        "an_sub": "None",
        "an_type": "中标公告"
    },
    {
        "an_major": "小额公共资源交易",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=DD5820E4E3D349E8B39FED9F9141F577",
        "an_sub": "None",
        "an_type": "开标"
    },
    {
        "an_major": "小额公共资源交易",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=2D605980EBA84FD5BEA902959B74A226",
        "an_sub": "None",
        "an_type": "合同订立及履约情况"
    },
    {
        "an_major": "小额公共资源交易",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=7F0FDF601EB04D3FB4F079A47470C8BB",
        "an_sub": "None",
        "an_type": "招标(采购)公告"
    },
    {
        "an_major": "小额公共资源交易",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=3523AC17CB304104AF950237D0B583E8",
        "an_sub": "None",
        "an_type": "中标候选人公示"
    },
    {
        "an_major": "小额公共资源交易",
        "an_sub_url": "http://www.gongshu.gov.cn/zwgk/public/home/gszw/realmList.action?strMap.columnUuid=737AD390F4F84346A93FC242E31EB67E",
        "an_sub": "None",
        "an_type": "澄清、修改公告"
    }
]
}


def main():
    return CRAWL_GONGSHU_TASKS