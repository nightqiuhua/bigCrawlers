#{'招标公告':22,'答疑文件':23,
#'答疑公告':465,'开标安排':24,
#'开标结果公示':486,'中标前公示':25,'中标公告':28}
#{
#       '建设':['351',],
#       '施工':['925'],
#       '监理':['926'],
#       '材料设备':['927'],
#       '园林绿化':['355'],
#       '勘察设计':['356'],
#       '物业':['357'],
#       '代建':['928'],
#       '交通':['359'],
#       '林水':['360'],
#       '代理比选':['929'],
#       '其他':['361'],
#   }
CRAWL_HANGZHOU_TASKS = {
    'name':'hangzhou',
    'source_url':'http://www.hzctc.cn/',
    'task_queue':'wangban:hangzhou:an_url_works',
    'task_ajax':'wangban:hangzhou:an_url_ajax',
    'task_check':'wangban:hangzhou:an_url_check',
    'html_type':'static',
    'tasks':[
    {
        "an_type": "招标公告",
        "afficheType": "22",
        "an_sub": "林水",
        "proID": "360",
        "an_major": "工程建设",
        "an_county": "林水",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "招标公告",
        "afficheType": "22",
        "an_sub": "监理",
        "proID": "926",
        "an_major": "工程建设",
        "an_county": "监理",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "招标公告",
        "afficheType": "22",
        "an_sub": "物业",
        "proID": "357",
        "an_major": "工程建设",
        "an_county": "物业",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "招标公告",
        "afficheType": "22",
        "an_sub": "施工",
        "proID": "925",
        "an_major": "工程建设",
        "an_county": "施工",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "招标公告",
        "afficheType": "22",
        "an_sub": "园林绿化",
        "proID": "355",
        "an_major": "工程建设",
        "an_county": "园林绿化",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "招标公告",
        "afficheType": "22",
        "an_sub": "其他",
        "proID": "361",
        "an_major": "工程建设",
        "an_county": "其他",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "招标公告",
        "afficheType": "22",
        "an_sub": "代建",
        "proID": "928",
        "an_major": "工程建设",
        "an_county": "代建",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "招标公告",
        "afficheType": "22",
        "an_sub": "材料设备",
        "proID": "927",
        "an_major": "工程建设",
        "an_county": "材料设备",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "招标公告",
        "afficheType": "22",
        "an_sub": "代理比选",
        "proID": "929",
        "an_major": "工程建设",
        "an_county": "代理比选",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "招标公告",
        "afficheType": "22",
        "an_sub": "建设",
        "proID": "351",
        "an_major": "工程建设",
        "an_county": "建设",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "招标公告",
        "afficheType": "22",
        "an_sub": "交通",
        "proID": "359",
        "an_major": "工程建设",
        "an_county": "交通",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "招标公告",
        "afficheType": "22",
        "an_sub": "勘察设计",
        "proID": "356",
        "an_major": "工程建设",
        "an_county": "勘察设计",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标前公示",
        "afficheType": "25",
        "an_sub": "林水",
        "proID": "360",
        "an_major": "工程建设",
        "an_county": "林水",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标前公示",
        "afficheType": "25",
        "an_sub": "监理",
        "proID": "926",
        "an_major": "工程建设",
        "an_county": "监理",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标前公示",
        "afficheType": "25",
        "an_sub": "物业",
        "proID": "357",
        "an_major": "工程建设",
        "an_county": "物业",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标前公示",
        "afficheType": "25",
        "an_sub": "施工",
        "proID": "925",
        "an_major": "工程建设",
        "an_county": "施工",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标前公示",
        "afficheType": "25",
        "an_sub": "园林绿化",
        "proID": "355",
        "an_major": "工程建设",
        "an_county": "园林绿化",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标前公示",
        "afficheType": "25",
        "an_sub": "其他",
        "proID": "361",
        "an_major": "工程建设",
        "an_county": "其他",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标前公示",
        "afficheType": "25",
        "an_sub": "代建",
        "proID": "928",
        "an_major": "工程建设",
        "an_county": "代建",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标前公示",
        "afficheType": "25",
        "an_sub": "材料设备",
        "proID": "927",
        "an_major": "工程建设",
        "an_county": "材料设备",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标前公示",
        "afficheType": "25",
        "an_sub": "代理比选",
        "proID": "929",
        "an_major": "工程建设",
        "an_county": "代理比选",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标前公示",
        "afficheType": "25",
        "an_sub": "建设",
        "proID": "351",
        "an_major": "工程建设",
        "an_county": "建设",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标前公示",
        "afficheType": "25",
        "an_sub": "交通",
        "proID": "359",
        "an_major": "工程建设",
        "an_county": "交通",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标前公示",
        "afficheType": "25",
        "an_sub": "勘察设计",
        "proID": "356",
        "an_major": "工程建设",
        "an_county": "勘察设计",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑公告",
        "afficheType": "465",
        "an_sub": "林水",
        "proID": "360",
        "an_major": "工程建设",
        "an_county": "林水",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑公告",
        "afficheType": "465",
        "an_sub": "监理",
        "proID": "926",
        "an_major": "工程建设",
        "an_county": "监理",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑公告",
        "afficheType": "465",
        "an_sub": "物业",
        "proID": "357",
        "an_major": "工程建设",
        "an_county": "物业",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑公告",
        "afficheType": "465",
        "an_sub": "施工",
        "proID": "925",
        "an_major": "工程建设",
        "an_county": "施工",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑公告",
        "afficheType": "465",
        "an_sub": "园林绿化",
        "proID": "355",
        "an_major": "工程建设",
        "an_county": "园林绿化",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑公告",
        "afficheType": "465",
        "an_sub": "其他",
        "proID": "361",
        "an_major": "工程建设",
        "an_county": "其他",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑公告",
        "afficheType": "465",
        "an_sub": "代建",
        "proID": "928",
        "an_major": "工程建设",
        "an_county": "代建",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑公告",
        "afficheType": "465",
        "an_sub": "材料设备",
        "proID": "927",
        "an_major": "工程建设",
        "an_county": "材料设备",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑公告",
        "afficheType": "465",
        "an_sub": "代理比选",
        "proID": "929",
        "an_major": "工程建设",
        "an_county": "代理比选",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑公告",
        "afficheType": "465",
        "an_sub": "建设",
        "proID": "351",
        "an_major": "工程建设",
        "an_county": "建设",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑公告",
        "afficheType": "465",
        "an_sub": "交通",
        "proID": "359",
        "an_major": "工程建设",
        "an_county": "交通",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑公告",
        "afficheType": "465",
        "an_sub": "勘察设计",
        "proID": "356",
        "an_major": "工程建设",
        "an_county": "勘察设计",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑文件",
        "afficheType": "23",
        "an_sub": "林水",
        "proID": "360",
        "an_major": "工程建设",
        "an_county": "林水",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑文件",
        "afficheType": "23",
        "an_sub": "监理",
        "proID": "926",
        "an_major": "工程建设",
        "an_county": "监理",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑文件",
        "afficheType": "23",
        "an_sub": "物业",
        "proID": "357",
        "an_major": "工程建设",
        "an_county": "物业",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑文件",
        "afficheType": "23",
        "an_sub": "施工",
        "proID": "925",
        "an_major": "工程建设",
        "an_county": "施工",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑文件",
        "afficheType": "23",
        "an_sub": "园林绿化",
        "proID": "355",
        "an_major": "工程建设",
        "an_county": "园林绿化",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑文件",
        "afficheType": "23",
        "an_sub": "其他",
        "proID": "361",
        "an_major": "工程建设",
        "an_county": "其他",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑文件",
        "afficheType": "23",
        "an_sub": "代建",
        "proID": "928",
        "an_major": "工程建设",
        "an_county": "代建",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑文件",
        "afficheType": "23",
        "an_sub": "材料设备",
        "proID": "927",
        "an_major": "工程建设",
        "an_county": "材料设备",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑文件",
        "afficheType": "23",
        "an_sub": "代理比选",
        "proID": "929",
        "an_major": "工程建设",
        "an_county": "代理比选",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑文件",
        "afficheType": "23",
        "an_sub": "建设",
        "proID": "351",
        "an_major": "工程建设",
        "an_county": "建设",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑文件",
        "afficheType": "23",
        "an_sub": "交通",
        "proID": "359",
        "an_major": "工程建设",
        "an_county": "交通",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑文件",
        "afficheType": "23",
        "an_sub": "勘察设计",
        "proID": "356",
        "an_major": "工程建设",
        "an_county": "勘察设计",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标结果公示",
        "afficheType": "486",
        "an_sub": "林水",
        "proID": "360",
        "an_major": "工程建设",
        "an_county": "林水",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标结果公示",
        "afficheType": "486",
        "an_sub": "监理",
        "proID": "926",
        "an_major": "工程建设",
        "an_county": "监理",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标结果公示",
        "afficheType": "486",
        "an_sub": "物业",
        "proID": "357",
        "an_major": "工程建设",
        "an_county": "物业",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标结果公示",
        "afficheType": "486",
        "an_sub": "施工",
        "proID": "925",
        "an_major": "工程建设",
        "an_county": "施工",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标结果公示",
        "afficheType": "486",
        "an_sub": "园林绿化",
        "proID": "355",
        "an_major": "工程建设",
        "an_county": "园林绿化",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标结果公示",
        "afficheType": "486",
        "an_sub": "其他",
        "proID": "361",
        "an_major": "工程建设",
        "an_county": "其他",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标结果公示",
        "afficheType": "486",
        "an_sub": "代建",
        "proID": "928",
        "an_major": "工程建设",
        "an_county": "代建",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标结果公示",
        "afficheType": "486",
        "an_sub": "材料设备",
        "proID": "927",
        "an_major": "工程建设",
        "an_county": "材料设备",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标结果公示",
        "afficheType": "486",
        "an_sub": "代理比选",
        "proID": "929",
        "an_major": "工程建设",
        "an_county": "代理比选",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标结果公示",
        "afficheType": "486",
        "an_sub": "建设",
        "proID": "351",
        "an_major": "工程建设",
        "an_county": "建设",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标结果公示",
        "afficheType": "486",
        "an_sub": "交通",
        "proID": "359",
        "an_major": "工程建设",
        "an_county": "交通",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标结果公示",
        "afficheType": "486",
        "an_sub": "勘察设计",
        "proID": "356",
        "an_major": "工程建设",
        "an_county": "勘察设计",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标公告",
        "afficheType": "28",
        "an_sub": "林水",
        "proID": "360",
        "an_major": "工程建设",
        "an_county": "林水",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标公告",
        "afficheType": "28",
        "an_sub": "监理",
        "proID": "926",
        "an_major": "工程建设",
        "an_county": "监理",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标公告",
        "afficheType": "28",
        "an_sub": "物业",
        "proID": "357",
        "an_major": "工程建设",
        "an_county": "物业",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标公告",
        "afficheType": "28",
        "an_sub": "施工",
        "proID": "925",
        "an_major": "工程建设",
        "an_county": "施工",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标公告",
        "afficheType": "28",
        "an_sub": "园林绿化",
        "proID": "355",
        "an_major": "工程建设",
        "an_county": "园林绿化",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标公告",
        "afficheType": "28",
        "an_sub": "其他",
        "proID": "361",
        "an_major": "工程建设",
        "an_county": "其他",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标公告",
        "afficheType": "28",
        "an_sub": "代建",
        "proID": "928",
        "an_major": "工程建设",
        "an_county": "代建",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标公告",
        "afficheType": "28",
        "an_sub": "材料设备",
        "proID": "927",
        "an_major": "工程建设",
        "an_county": "材料设备",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标公告",
        "afficheType": "28",
        "an_sub": "代理比选",
        "proID": "929",
        "an_major": "工程建设",
        "an_county": "代理比选",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标公告",
        "afficheType": "28",
        "an_sub": "建设",
        "proID": "351",
        "an_major": "工程建设",
        "an_county": "建设",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标公告",
        "afficheType": "28",
        "an_sub": "交通",
        "proID": "359",
        "an_major": "工程建设",
        "an_county": "交通",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标公告",
        "afficheType": "28",
        "an_sub": "勘察设计",
        "proID": "356",
        "an_major": "工程建设",
        "an_county": "勘察设计",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标安排",
        "afficheType": "24",
        "an_sub": "林水",
        "proID": "360",
        "an_major": "工程建设",
        "an_county": "林水",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标安排",
        "afficheType": "24",
        "an_sub": "监理",
        "proID": "926",
        "an_major": "工程建设",
        "an_county": "监理",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标安排",
        "afficheType": "24",
        "an_sub": "物业",
        "proID": "357",
        "an_major": "工程建设",
        "an_county": "物业",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标安排",
        "afficheType": "24",
        "an_sub": "施工",
        "proID": "925",
        "an_major": "工程建设",
        "an_county": "施工",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标安排",
        "afficheType": "24",
        "an_sub": "园林绿化",
        "proID": "355",
        "an_major": "工程建设",
        "an_county": "园林绿化",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标安排",
        "afficheType": "24",
        "an_sub": "其他",
        "proID": "361",
        "an_major": "工程建设",
        "an_county": "其他",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标安排",
        "afficheType": "24",
        "an_sub": "代建",
        "proID": "928",
        "an_major": "工程建设",
        "an_county": "代建",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标安排",
        "afficheType": "24",
        "an_sub": "材料设备",
        "proID": "927",
        "an_major": "工程建设",
        "an_county": "材料设备",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标安排",
        "afficheType": "24",
        "an_sub": "代理比选",
        "proID": "929",
        "an_major": "工程建设",
        "an_county": "代理比选",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标安排",
        "afficheType": "24",
        "an_sub": "建设",
        "proID": "351",
        "an_major": "工程建设",
        "an_county": "建设",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标安排",
        "afficheType": "24",
        "an_sub": "交通",
        "proID": "359",
        "an_major": "工程建设",
        "an_county": "交通",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标安排",
        "afficheType": "24",
        "an_sub": "勘察设计",
        "proID": "356",
        "an_major": "工程建设",
        "an_county": "勘察设计",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "意见征询",
        "afficheType": "26",
        "an_sub": "NONE",
        "an_major": "政府采购",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑公告",
        "afficheType": "466",
        "an_sub": "NONE",
        "an_major": "政府采购",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "更正答疑",
        "afficheType": "29",
        "an_sub": "NONE",
        "an_major": "政府采购",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "采购公告",
        "afficheType": "27",
        "an_sub": "NONE",
        "an_major": "政府采购",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "结果公告",
        "afficheType": "32",
        "an_sub": "NONE",
        "an_major": "政府采购",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标安排",
        "afficheType": "490",
        "an_sub": "NONE",
        "an_major": "政府采购",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑公告",
        "afficheType": "467",
        "an_sub": "NONE",
        "an_major": "土地矿业",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "结果公告",
        "afficheType": "42",
        "an_sub": "NONE",
        "an_major": "土地矿业",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "更正答疑",
        "afficheType": "40",
        "an_sub": "NONE",
        "an_major": "土地矿业",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "出让公告",
        "afficheType": "39",
        "an_sub": "NONE",
        "an_major": "土地矿业",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标安排",
        "afficheType": "492",
        "an_sub": "NONE",
        "an_major": "土地矿业",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "产权公告",
        "afficheType": "58",
        "an_sub": "NONE",
        "an_major": "产权交易",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "成交公示",
        "afficheType": "97",
        "an_sub": "NONE",
        "an_major": "产权交易",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑公告",
        "afficheType": "468",
        "an_sub": "NONE",
        "an_major": "产权交易",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "更正答疑",
        "afficheType": "96",
        "an_sub": "NONE",
        "an_major": "产权交易",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标安排",
        "afficheType": "494",
        "an_sub": "NONE",
        "an_major": "产权交易",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "招标公告",
        "afficheType": "34",
        "an_sub": "NONE",
        "an_major": "综合其他",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑文件",
        "afficheType": "499",
        "an_sub": "NONE",
        "an_major": "综合其他",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "中标前公示",
        "afficheType": "37",
        "an_sub": "NONE",
        "an_major": "综合其他",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "答疑公告",
        "afficheType": "469",
        "an_sub": "NONE",
        "an_major": "综合其他",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    },
    {
        "an_type": "开标安排",
        "afficheType": "36",
        "an_sub": "NONE",
        "an_major": "综合其他",
        "an_county": "NONE",
        "an_sub_url": "http://www.hzctc.cn/"
    }
]
}
def main():
    return CRAWL_HANGZHOU_TASKS