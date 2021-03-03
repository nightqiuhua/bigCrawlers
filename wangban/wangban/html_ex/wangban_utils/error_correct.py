import __init__
from mysql_util import MySqlDBClass
from mongo_mysql_util import MongoDB_To_MySQL
import os
import json
import time

import threading
lock = threading.Lock()

class Row_dict(dict):
    def __getattr__(self,name):
        try:
            return self[name]
        except KeyError:
            raise AttributerError(name)

class ErrorCorrect(MongoDB_To_MySQL):
    def read_files(self,file_path,sheet_name):
        file_name = os.path.join(file_path,'{}_error.txt'.format(sheet_name))
        with open(file_name,'r') as file:
            content = file.read()
            for line in content.split(";"):
                if not len(line):
                    continue
                if 'xiangshan' in line:
                    continue
                try:
                    info =  json.loads(line)
                except Exception as e:
                    print(e,line)
                    continue
                
                yield info

    def get_mysql_primary_key(self,pri_key,link):
        #cond = "type = '采购公示'"
        cond = "link = '{}'".format(link)
        try:
            for item in self.mysql_conn.get_column_data(self.sheet_name,pri_key,cond):
                self.redis_conn.sadd('wangban:{}:mysql_redis'.format(self.sheet_name),item)
        except Exception as e:
            print('get mysql primary_key error',e)


    def get_all_keys(self,file_path):
        for info in self.read_files(file_path,self.sheet_name):
            self.get_mysql_primary_key('ID',info['id'])

    def get_from_mysql(self):
        finished_abled = False
        while True:
            found = 0
            while found <= self.mysql_batch_size:
                row_key = self.redis_conn.spop('wangban:{}:mysql_redis'.format(self.sheet_name))
                if not row_key:
                    finished_abled = True
                    break
                cond_field = 'ID'
                try:
                    lock.acquire()
                    single_data,column_name = self.mysql_conn.get_from_db('*',self.sheet_name,cond_field,row_key)
                    yield single_data,column_name
                except Exception as e:
                    print('MongoDB_To_MySQL get_from_mysql error',e)
                finally:
                    lock.release()
                found += 1
                print('found',found)
            time.sleep(3)
            if finished_abled:
                break


    def run_mysql_to_mongo(self):
        print('{} {} is sending data'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),self.sheet_name))
        i = 0
        #self.get_all_keys(file_path)
        try:
            for data,column_name in self.get_from_mysql():
                item = Row_dict(zip(column_name,data))
                item['_id'] = item['link']
                #if i > 8:
                #    break
                #i=i+1
                #print('item',item)
                #print('key_id',len(self.primary_keys))
                self.send_to_mongo(item)
        except Exception as e:
            print('run_mysql_to_mongo error',e)

if __name__ == '__main__':
    file_path = 'C:\\Users\\Administrator\\Desktop\\error'
    error_instance = ErrorCorrect('beilun')
    error_instance.get_all_keys(file_path)
    error_instance.run_mysql_to_mongo()



#找到link对应的ID
#将与ID对应的条目信息存到mongodb里面
