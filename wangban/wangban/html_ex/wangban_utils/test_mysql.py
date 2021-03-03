import __init__
from mongo_mysql_util import MongoDB_To_MySQL
import time
import os

NEW_SETTINGS = {
'MYSQL_HOST' : "rm-bp1aj66015accj2ojqo.mysql.rds.aliyuncs.com",
'MYSQL_PORT' : 3306,
'MYSQL_USER' :"yc_03",
'MYSQL_PASSWORD':"123456789_yc",
'MYSQL_DBNAME' :"zhaobiao",
'MONGODB_HOST' : '127.0.0.1',
'MONGODB_PORT' : 27017,
'MONGODB_DBNAME' : 'wangban',
'MONGODB_SHEETNAME' : '',
}
class Test_Mongo(MongoDB_To_MySQL):

    def send_to_mysql(self,data,sheet_name,sheet_name_table):
        try:
            data = self.data_modify_func(sheet_name,data)
            print('data',data)
            #self.mysql_conn.insert_into_db(data,sheet_name_table)
            print('{} Sending data to mysql'.format(sheet_name))
        except Exception as e:
            print('pipeline error_reason',e)
            self.def_logger.logging_info({'id':data['link']},sheet_name,self.file_path,'error')
            return False 
        return True

    def run_mongo_to_mysql(self,sheet_name,sheet_name_table):
        print('{} {} is sending data'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),sheet_name))
        i = 0
        for item in self.get_from_mongo():
            try:
                print(item)
                success_enabled = self.send_to_mysql(item,sheet_name,sheet_name_table)
                #print('mongo working')
                if i > 8:
                    break
                i=i+1
            except Exception as e:
                print('MongoDB_To_MySQL run_mongo_to_mysql error',e)
            finally:
                #self.mongo_db.delete_from_db(item,sheet_name)
                pass



def mongo_to_mysql_function(sheet_name,settings):
    test_instance= Test_Mongo(sheet_name,settings)
    test_instance.run_mongo_to_mysql(sheet_name,'t_zhaobiao_2')

if __name__ == '__main__':
    mongo_to_mysql_function('beilun',NEW_SETTINGS)