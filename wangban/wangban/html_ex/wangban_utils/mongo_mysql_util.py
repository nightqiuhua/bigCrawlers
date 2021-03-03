import __init__
import pymongo
#from .mysql_util import MySqlDBClass
#from .mongo_util import MongodbClass
from mysql_util import MySqlDBClass
from mongo_util import MongodbClass
from modify_func import all_modify_func
#from sql_sen import all_sql_sentence
import time
import threading
from redis_util import get_redis_conn
from logging_util import update_logging
lock = threading.Lock()
import json
import re 

SETTINGS = {

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

class Row_dict(dict):
    def __getattr__(self,name):
        try:
            return self[name]
        except KeyError:
            raise AttributerError(name)

class MongoDB_To_MySQL:
    def __init__(self,sheet_name,settings=SETTINGS):
        self.mongo_db = MongodbClass()
        self.mysql_conn = MySqlDBClass(settings)
        self.sheet_name = sheet_name
        self.primary_keys = []
        self.mongo_batch_size = 400
        self.mysql_batch_size = 200
        self.redis_conn = get_redis_conn()
        self.def_logger = update_logging()
        self.file_path = 'C:\\Program Files (x86)\\crawling_server\\wangban_utils'

    def get_mysql_primary_key(self,mongo_sheet_name,pri_key,cond=''):
        try:
            for item in self.mysql_conn.get_column_data(self.sheet_name,pri_key,cond):
                self.redis_conn.sadd('wangban:{}:mysql_redis'.format(mongo_sheet_name),item)
        except Exception as e:
            print('get mysql primary_key error',e)

    def get_mongo_primary_key(self,pri_key,cond=''):
        try:
            for item in self.mongo_db.get_all_from_db(self.sheet_name,return_field=pri_key):
                #print(item)
                self.redis_conn.sadd('wangban:{}:mongo_redis'.format(self.sheet_name),item[pri_key])
        except Exception as e:
            print('get mongo primary_key error',e)


    def get_from_mysql(self,mongo_sheet_name):
        finished_abled = False
        while True:
            found = 0
            while found <= self.mysql_batch_size:
                row_key = self.redis_conn.spop('wangban:{}:mysql_redis'.format(mongo_sheet_name))
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

    def get_from_mongo(self):
        finished_abled = False
        while True:
            found = 0
            #self.get_mongo_primary_key("_id")
            while found <= self.mongo_batch_size:
                row_key = self.redis_conn.spop('wangban:{}:mongo_redis'.format(self.sheet_name))
                if not row_key:
                    finished_abled = True
                    break
                try:
                    cond_field = 'ID'
                    row_key = row_key.decode('utf-8')
                    data_item = self.mongo_db.get_from_db(self.sheet_name,condition={"_id":row_key})
                    #print(data_item)
                    yield data_item
                except Exception as e:
                    print('MySqlDBClass get_from_mongo error',e)
                finally:
                    pass
                found += 1
            time.sleep(3)
            if finished_abled:
               break

    def get_from_local_mysql(self):
        found = 0 
        while found <= self.mysql_batch_size:
            try:
                lock.acquire()
                single_data,column_name = self.local_mysql_conn.get_from_local_db('*',self.sheet_name)
                yield single_data,column_name
            except Exception as e:
                print('MySqlDBClass get_from_local_mysql error',e)
            finally:
                lock.release()
            found += 1


    def send_to_mongo(self,data,sheet_name):
        try:
            self.mongo_db.insert_into_db(data,sheet_name)
        except Exception as e:
            print('MongoDB_To_MySQL send to mongo error',e)

    def send_to_mysql(self,data,sheet_name,sheet_name_table):
        try:
            input_item = data
            #input_item = self.data_modify_func(sheet_name,data)
            self.mysql_conn.insert_into_db(input_item,sheet_name_table)
            print('{} Sending data to mysql'.format(sheet_name))
        except Exception as e:
            print('pipeline error_reason',e)
            self.def_logger.logging_info({'id':data['link'],'link_id':data["ID"]},sheet_name,self.file_path,'error')
            return False 
        return True

    def data_modify_func(self,sheet_name,data):
        func_chosen =all_modify_func[sheet_name]
        item = func_chosen(data)
        return item

    def run_mongo_to_mysql(self,sheet_name,sheet_name_table):
        print('{} {} is sending data'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),sheet_name))
        i = 0
        self.get_mongo_primary_key("_id")
        for item in self.get_from_mongo():
            try:
                input_item = item
                self.send_to_mysql(input_item,sheet_name,sheet_name_table)
                self.mongo_db.delete_from_db(input_item['_id'],sheet_name)
            except Exception as e:
                print('MongoDB_To_MySQL run_mongo_to_mysql error',e)
            finally:
                pass

    def data_process(self,data):
        item_result = {}
        item_result['_id'] = data["_id"]
        item_result['provine'] = data["provine"]
        item_result['city'] = data["city"]
        item_result['county'] = data["county"]
        item_result['year'] = str(data["year"])
        item_result['month'] = str(data["month"])
        item_result['num'] = str((data["page"]-1)*100 + int(data["num"]))
        item_result['name'] = re.sub(r'\s+','',data["name"])
        item_result['model'] = re.sub(r'\s+','',data["model"])
        item_result['specification'] = re.sub(r'\s+','',data["specification"])
        item_result['unit'] = re.sub(r'\s+','',data["unit"])
        item_result['after_tax_price'] = str(re.sub(r'\s+','',data["after_tax_price"]))
        item_result['tax_price'] = str(re.sub(r'\s+','',data["tax_price"]))
        item_result['tax_rate'] = str(re.sub(r'\s+','',data["tax_rate"]))
        item_result['note'] = re.sub(r'\s+','',data["note"])
        return item_result


    def run_mysql_to_mongo(self,mongo_sheet_name,cond=''):
        print('{} {} is sending data'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),mongo_sheet_name))
        self.get_mysql_primary_key(mongo_sheet_name,'ID',cond='ZBR = "浙江大学"')
        #i = 0
        try:
            for data,column_name in self.get_from_mysql(mongo_sheet_name):
                item = Row_dict(zip(column_name,data))
                item['_id'] = item['LINK']
                #print(item)
                #break
                self.send_to_mongo(item,mongo_sheet_name)
        except Exception as e:
            print('run_mysql_to_mongo error',e)


if __name__ == '__main__':
    util_conn = MongoDB_To_MySQL('t_zhaobiao_data')
    util_conn.run_mysql_to_mongo('t_zhaobiao_data')