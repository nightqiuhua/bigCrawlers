import __init__
from mysql_util import MySqlDBClass
import json
import os

class Check_data:
    def __init__(self):
        self.mysql_conn = MySqlDBClass()
        self.filename = 'check_data.txt'

    def check(self,sheet_name,column,condition_key=''):
        try:
            for item in self.mysql_conn.get_column_data(sheet_name,column):
                yield {sheet_name:item}
        except Exception as e:
            print('check error',e)


    def get_tasks(self,task_paths):
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
        #task_list = ['linhai']
        #task_list = ['xiaoshan']
        return task_list

    def write_check_file(self,item):
        try:
            one_jsonfile = json.dumps(item)
            with open(self.filename,'a') as f:
                f.write(one_jsonfile + '\n')
        except Exception as e:
            raise e

    def run_check_tasks(self,task_paths,column):
        for task_name in self.get_tasks(task_paths):
            for item in self.check(task_name,column):
                self.write_check_file(item)

if __name__ == '__main__':
    task_paths = [
                'C:\\Program Files (x86)\\crawling_server\\wangban\\wangban\\spiders\\ningbo',
                'C:\\Program Files (x86)\\crawling_server\\wangban\\wangban\\spiders\\hangzhou',
                'C:\\Program Files (x86)\\crawling_server\\wangban\\wangban\\spiders\\huzhou',
                'C:\\Program Files (x86)\\crawling_server\\wangban\\wangban\\spiders\\shaoxing',
                'C:\\Program Files (x86)\\crawling_server\\wangban\\wangban\\spiders\\quzhou',
                'C:\\Program Files (x86)\\crawling_server\\wangban\\wangban\\spiders\\taizhou',
                'C:\\Program Files (x86)\\crawling_server\\wangban\\wangban\\spiders\\wenzhou',
                'C:\\Program Files (x86)\\crawling_server\\wangban\\wangban\\spiders\\zhoushan',
                ]
    check_way = Check_data()
    check_way.run_check_tasks(task_paths,'max(pubdate)')


