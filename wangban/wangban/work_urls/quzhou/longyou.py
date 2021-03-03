

CRAWL_LONGYOU_TASKS = {
    'name':'longyou',
    'source_url':'',
    'task_queue':'wangban:longyou:an_work_urls',
    'task_check':'wangban:longyou:an_check_urls',
    'task_ajax':'wangban:longyou:an_url_ajax',
    'html_type':'ajax',
    'tasks':[
    {'政府采购':{
    '采购公告':{'NONE':'http://www.lyxztb.com/index.php?c=content&a=list&catid=10',},
    '采购公示':{'NONE':'http://www.lyxztb.com/index.php?c=content&a=list&catid=11',},
    '采购结果':{'NONE':'http://www.lyxztb.com/index.php?c=content&a=list&catid=12',},
    '采购合同':{'NONE':'http://www.lyxztb.com/index.php?c=content&a=list&catid=52',},
    }},
    {'建设工程':{
    '工程公告':{'NONE':'http://www.lyxztb.com/index.php?c=content&a=list&catid=13',},
    '工程公示':{'NONE':'http://www.lyxztb.com/index.php?c=content&a=list&catid=14',},
    '结果公告':{'NONE':'http://www.lyxztb.com/index.php?c=content&a=list&catid=15',},
    '开标记录':{'NONE':'http://www.lyxztb.com/index.php?c=content&a=list&catid=56',},
    }},
    {'产权交易':{
    '交易公告':{'NONE':'http://www.lyxztb.com/index.php?c=content&a=list&catid=16',},
    '交易结果':{'NONE':'http://www.lyxztb.com/index.php?c=content&a=list&catid=17',},
    }},
    {'土地交易':{
    '交易公告':{'NONE':'http://www.lyxztb.com/index.php?c=content&a=list&catid=18',},
    '交易结果':{'NONE':'http://www.lyxztb.com/index.php?c=content&a=list&catid=19',},
    }},
    {'乡镇':{
    '乡镇公告':{'NONE':'http://www.lyxztb.com/index.php?c=content&a=list&catid=21',},
    '乡镇公示':{'NONE':'http://www.lyxztb.com/index.php?c=content&a=list&catid=50',},
    '开标记录':{'NONE':'http://www.lyxztb.com/index.php?c=content&a=list&catid=57',},
    '结果公告':{'NONE':'http://www.lyxztb.com/index.php?c=content&a=list&catid=58',},
    }},
    {'部门单位':{
    '部门公告':{'NONE':'http://www.lyxztb.com/index.php?c=content&a=list&catid=53',},
    '部门公示':{'NONE':'http://www.lyxztb.com/index.php?c=content&a=list&catid=59',},
    '驻龙单位公告':{'NONE':'http://www.lyxztb.com/index.php?c=content&a=list&catid=20',},
    }},
    ]
}

#http://www.lyxztb.com/index.php?c=content&a=list&catid=59
#http://www.lyxztb.com/index.php?c=content&a=list&catid=20&page=50
#
def main():
    return CRAWL_LONGYOU_TASKS