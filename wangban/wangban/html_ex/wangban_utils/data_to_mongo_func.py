import __init__
from mongo_mysql_util import MongoDB_To_MySQL
import os


#OLD_SETTINGS = {
#'MYSQL_HOST' : "rm-bp1k68h2lq872j040mo.mysql.rds.aliyuncs.com",
#'MYSQL_PORT' : 3306,
#'MYSQL_USER' :"root",
#'MYSQL_PASSWORD':"N5QjbPu097Kuz4BV",
#'MYSQL_DBNAME' :"zhaobiao",
#
#
#'MONGODB_HOST' : '127.0.0.1',
#'MONGODB_PORT' : 27017,
#'MONGODB_DBNAME' : 'wangban',
#'MONGODB_SHEETNAME' : '',
#}


OLD_SETTINGS = {
#'MYSQL_HOST' : "rm-bp1aj66015accj2ojqo.mysql.rds.aliyuncs.com",
#'MYSQL_PORT' : 3306,
#'MYSQL_USER' :"yc_03",
#'MYSQL_PASSWORD':"123456789_yc",
#'MYSQL_DBNAME' :"zhaobiao",

'MYSQL_HOST' : "rm-bp1347o8ygf2t265vho.mysql.rds.aliyuncs.com",
'MYSQL_PORT' : 3306,
'MYSQL_USER' :"wbpmzb",
'MYSQL_PASSWORD':"123456789Wbpm",
'MYSQL_DBNAME' :"wpzb",

'MONGODB_HOST' : '127.0.0.1',
'MONGODB_PORT' : 27017,
'MONGODB_DBNAME' : 'wangban',
'MONGODB_SHEETNAME' : '',
}

def mysql_to_mongo_function(sheet_name,mongo_name,cond):
    m_to_m_instance= MongoDB_To_MySQL(sheet_name,OLD_SETTINGS)
    
    m_to_m_instance.run_mysql_to_mongo(mongo_name,cond)


def get_tasks(task_paths):
    task_list = []
    for path in task_paths:
        for root,dirs,files in os.walk(path):
            for file in files:
                if 'init' in file:
                    continue
                #if 'fuyang' in file:
                #    continue
                if 'cpython' in file:
                    continue
                #print('file',file)
                if file.endswith('.py'):
                    file = file.replace('.py','')
                    task_list.append(file)
                yield file
                #yield 'xunjia'
    #task_list = ['fuyang']
    #task_list = ['xiaoshan']
    #return task_list

def run_func(task_paths):
    for task in get_tasks(task_paths):
        #print('proccesing {} task'.format(task))
        #if task in ['zhuji','fuyang','dajiangdong','chunan']:
        #    continue
        #task = 'zhejiang'
        work_task = task.replace('_ajax','')
        mysql_to_mongo_function(work_task)


if __name__ == '__main__':
    task_paths = [
                #'C:\\Program Files (x86)\\crawling_server\\wangban_utils\\modify_func\\ningbo',
                #'C:\\Program Files (x86)\\crawling_server\\wangban_utils\\modify_func\\hangzhou',
                #'C:\\Program Files (x86)\\crawling_server\\wangban_utils\\modify_func\\huzhou',
                #'C:\\Program Files (x86)\\crawling_server\\wangban_utils\\modify_func\\shaoxing',
                #'C:\\Program Files (x86)\\crawling_server\\wangban_utils\\modify_func\\quzhou',
                #'C:\\Program Files (x86)\\crawling_server\\wangban_utils\\modify_func\\taizhou',
                #'C:\\Program Files (x86)\\crawling_server\\wangban_utils\\modify_func\\wenzhou',
                'C:\\Program Files (x86)\\crawling_server\\wangban_utils\\modify_func\\zhoushan',
                #'C:\\Program Files (x86)\\crawling_server\\wangban\\wangban\\spiders\\jiaxing',
                #'C:\\Program Files (x86)\\crawling_server\\wangban\\wangban\\spiders\\jinhua',
                #'C:\\Program Files (x86)\\crawling_server\\wangban\\wangban\\spiders\\lishui',
                #'C:\\Program Files (x86)\\crawling_server\\wangban\\wangban\\spiders\\zhejiang',
                ]
    #run_func(task_paths)
    #for sheet_name,sitename in [('wenzhou_clean','温州市公共资源交易网'),('pingyang_clean','温州市平阳县公共资源交易网'),('cangnan_clean','温州市苍南县公共资源交易网'),('wengcheng_clean','温州市文成县公共资源交易网'),('ruian_clean','温州市瑞安市公共资源交易网'),]:
    #for sheet_name,sitename in [('hangzhou_clean','杭州市公共资源交易网')]:
    #    cond = 'sitename = "{}"'.format(sitename)
    cond = ''
    mysql_to_mongo_function('xunjia','xunjia',cond)
