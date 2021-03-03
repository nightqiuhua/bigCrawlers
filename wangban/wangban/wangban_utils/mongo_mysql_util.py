import pymongo
from .mysql_util import MySqlDBClass
from .mongo_util import MongodbClass
#from mysql_util import MySqlDBClass
#from mongo_util import MongodbClass
#from sql_sen import all_sql_sentence
import time
import threading
from .redis_util import get_redis_conn
#from redis_util import get_redis_conn
lock = threading.Lock()

class Row_dict(dict):
    def __getattr__(self,name):
        try:
            return self[name]
        except KeyError:
            raise AttributerError(name)

class MongoDB_To_MySQL:
    def __init__(self,sheet_name):
        self.mongo_db = MongodbClass()
        self.mysql_conn = MySqlDBClass()
        self.sheet_name = sheet_name
        self.primary_keys = []
        self.mongo_batch_size = 15
        self.mysql_batch_size = 15
        self.mongo_redis_conn = get_redis_conn()
        #self.local_mysql_conn = MySqlDBClass(MYSQL_HOST='localhost',
        #                MYSQL_PORT=3306,MYSQL_USER ="root",MYSQL_PASSWORD="123456",MYSQL_DBNAME ="zhaobiao")
        self.get_mysql_primary_key('link')

    def get_from_mongo(self):
        found = 0
        while found <= self.mongo_batch_size:
            try:
                data = self.mongo_db.get_from_db(self.sheet_name)
                if not data:
                    break
            except Exception as e:
                print('get from mongo error',e)
            yield data
            found += 1

    def get_mysql_primary_key(self,pri_key,cond=''):
        cond = "type = '采购中标公示'"
        try:
            self.mysql_conn.get_column_data(self.sheet_name,pri_key,cond)
        except Exception as e:
            print('get mysql primary_key error',e)

    def get_from_mysql(self):
        fininsh_symbol = False
        while True:
            found = 0 
            while found <= self.mysql_batch_size:
                row_key = self.mongo_redis_conn.spop('wangban:{}:mysql_redis'.format(self.sheet_name))
                if not row_key:
                    fininsh_symbol = True
                    break
                cond_field = 'link'
                try:
                    lock.acquire()
                    single_data,column_name = self.mysql_conn.get_from_db('*',self.sheet_name,cond_field,row_key)
                    yield single_data,column_name
                except Exception as e:
                    print('MySqlDBClass get_from_mysql error',e)
                finally:
                    lock.release()
                found += 1
                print('found',found)
            if fininsh_symbol:
                break
            time.sleep(3)

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


    def send_to_mongo(self,data):
        try:
            self.mongo_db.insert_into_db(data,self.sheet_name)
        except Exception as e:
            print('MongoDB_To_MySQL send to mongo error',e)

    def send_to_mysql(self,data):
        try:
            self.mysql_conn.insert_into_db(data,self.sheet_name)
            print('{} Sending data to mysql'.format(self.sheet_name))
        except Exception as e:
            print('pipeline error_reason',e)
            return False 
        return True

    def run_mongo_to_mysql(self):
        print('{} {} is sending data'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),self.sheet_name))
        for item in self.get_from_mongo():
            try:
                lock.acquire()
                success_enabled = self.send_to_mysql(item)
                if success_enabled:
                    self.mongo_db.delete_from_db(item,self.sheet_name)
            except Exception as e:
                print('MongoDB_To_MySQL run_mongo_to_mysql error',e)
            finally:
                lock.release()

    def run_mysql_to_mongo(self):
        print('{} {} is sending data'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),self.sheet_name))
        try:
            for data,column_name in self.get_from_mysql():
                item = Row_dict(zip(column_name,data))
                item['_id'] = item['link']
                #print('item',item)
                #print('key_id',len(self.primary_keys))
                self.send_to_mongo(item)
        except Exception as e:
            print('run_mysql_to_mongo error',e)
        return True

    #def run_mysql_to_mysql(self):
    #    print('{} {} is sending data'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),self.sheet_name))
    #    for single_data,column_name in self.get_from_local_mysql():
    #        try:
    #            item = Row_dict(zip(column_name,single_data))
    #            item['_id'] = item['link']
    #            success_enabled = self.send_to_mongo(item)
    #            if success_enabled:
    #                self.local_mysql_conn.delete_from_db(item['link'],self.sheet_name)
    #        except Exception as e:
    #            print('run_mysql_to_mongo error',e)


if __name__ == '__main__':
    m_to_m_instance= MongoDB_To_MySQL('dajiangdong')
    m_to_m_instance.run_mysql_to_mongo()