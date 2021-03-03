import __init__
from mongo_mysql_util import MongoDB_To_MySQL
import time
import os

#NEW_SETTINGS = {
#'MYSQL_HOST' : "rm-bp1aj66015accj2ojqo.mysql.rds.aliyuncs.com",
#'MYSQL_PORT' : 3306,
#'MYSQL_USER' :"yc_03",
#'MYSQL_PASSWORD':"123456789_yc",
#'MYSQL_DBNAME' :"zhaobiao",
#
#
#'MONGODB_HOST' : '127.0.0.1',
#'MONGODB_PORT' : 27017,
#'MONGODB_DBNAME' : 'wangban',
#'MONGODB_SHEETNAME' : '',
#}

NEW_SETTINGS = {
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



def mongo_to_mysql_function(sheet_name,settings):
    m_to_m_instance= MongoDB_To_MySQL(sheet_name,settings)
    #m_to_m_instance.run_mongo_to_mysql(sheet_name,'t_zhaobiao_2')
    m_to_m_instance.run_mongo_to_mysql(sheet_name,'t_zhaobiao')

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
                #yield 'fuyang'
    #task_list = ['fuyang']
    #task_list = ['xiaoshan']
    #return task_list

def run_func(task_paths,settings):
    #for task in get_tasks(task_paths):
    for task in ['taizhou','wenzhou','zhoushan']:
        #print('proccesing {} task'.format(task))
        #if task in ['dajiangdong','chunan']:
        #    continue
        #task = 'zhejiang'
        work_task = task.replace('_ajax','')
        mongo_to_mysql_function(work_task,settings)


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
    #run_func(task_paths,NEW_SETTINGS)
    for task in ['hangzhou']:
        mongo_to_mysql_function(task,NEW_SETTINGS)