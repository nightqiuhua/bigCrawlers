#一个用来处理数据的接口
#输入数据为从mongodb中导出的json数据
#json数据含有的关键信息是link,text
#输出数据是字典类型，含有的关键信息是link,purchaser,supplier,money,rate
#本接口的主要作用是用来导入json数据供，清洗脚本使用，
#然后再将得到的purchaser,supplier,money,rate 等信息输入mongodb数据库中
#
from byte_dict_covertion import byte_to_dict,dict_to_byte
from redis_util import get_redis_conn 
from mongo_util import MongodbClass
from datetime import datetime

class DataCleanConnection:
    def __init__(self,sheet_name):
        self.mongo_conn = MongodbClass()
        self.redis_conn = get_redis_conn()
        self.sheet_name = sheet_name
        #self.redis_queue = 'wanbang:{}:data_clean_queue'.format(sheet_name)

    def get_one_from_mongo(self,condition=None,field=None):
        data = self.mongo_conn.get_from_db(self.sheet_name,condition=condition,return_field=field)
        return data

    def get_all_from_mongo(self,condition=None,field=None):
        for single_data in self.mongo_conn.get_all_from_db(self.sheet_name,condition=condition,return_field=field)
            yield single_data

    def update_from_mongo(self,sheet_name,query,new_info):
        try:
            self.mongo_conn.update_data(self.sheet_name,query_condition=query,new_data=new_info)
        except Exception as e:
            print('DataCleanConnection update_from_mongo error',e)

    def put_to_mongo(self,data):
        self.mongo_conn.insert_into_db(self,data,self.sheet_name)

    def put_to_redis(self,queue,link_dict):
        data = dict_to_byte(link_dict)
        self.redis_conn.lpush(queue,data)

    def get_from_redis(self,queue):
        data = self.redis_conn.rpop(queue)
        link_dict = byte_to_dict(data)
        return data



