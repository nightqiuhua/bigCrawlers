import pymongo
from scrapy.utils.project import get_project_settings
SETTINGS = get_project_settings()

def get_mongodb_conn(**kwargs):
    settings = get_project_settings()
    db_host = kwargs.get('host',settings['MONGODB_HOST'])
    db_port = kwargs.get('port',settings['MONGODB_PORT'])
    db_name = kwargs.get('db_name',settings['MONGODB_DBNAME'])
    mongo_client = pymongo.MongoClient(host = db_host,port = db_port)
    mongo_db = mongo_client[db_name]
    return mongo_db

class MongodbClass:
    def __init__(self,**kwargs):
        self.host = kwargs.get('host',SETTINGS['MONGODB_HOST'])
        self.port = kwargs.get('port',SETTINGS['MONGODB_PORT'])
        self.name = kwargs.get('db_name',SETTINGS['MONGODB_DBNAME'])
        self.duplicate_count = 0
        self.connect_db()

    def connect_db(self):
        self.mongo_client = pymongo.MongoClient(host = self.host,port = self.port)
        self.mongo_db = self.mongo_client[self.name]
        return self.mongo_db

    def insert_into_db(self,data,sheet_name):
        try:
            self.mongo_db[sheet_name].insert(data)
            print('Processing item')
        except pymongo.errors.DuplicateKeyError as e:
            #pass
            #self.duplicate_count += 1
            print('_id',data['_id'])
            print('DuplicateKey number')
            raise e

    def get_from_db(self,sheet_name,condition = None,return_field=None):
        if return_field:
            return_field = {return_field:1}
        if not condition:
            condition = {}
        try:
            data = self.mongo_db[sheet_name].find_one(condition,return_field)
            if not data:
                return False
        except Exception as e:
            print('get from mongo error',e)
            return False
        #print(data)
        return data

    def get_all_from_db(self,sheet_name,condition = None,return_field=None):
        if return_field:
            return_field = {return_field:1}
        if not condition:
            condition = {}
        try:
            for single_one in self.mongo_db[sheet_name].find(condition,return_field):
                yield single_one
        except Exception as e:
            print('MongodbClass get_all_from_db',e)

    def update_data(self,sheet_name,query_condition,new_data):
        try:
            self.mongo_db[sheet_name].update(query_condition,{'$set':new_data})
        except Exception as e:
            print('MongodbClass update_data error',e)

    #def get_column_names(self,sheet_name):
    #    try:
    #        
    #    except Exception as e:
    #        raise e
    def detect_from_db(self,sheet_name,select_conditions):
        try:
            detect_num = self.mongo_db[sheet_name].find(select_conditions).count()
            #print(detect_num)
        except Exception as e:
            print('MongodbClass detect_from_db error',e)
            return 0
        #print(detect_num)
        return detect_num


    def delete_from_db(self,data,sheet_name):
        try:
            self.mongo_db[sheet_name].delete_one(data)
        except Exception as e:
            print('delete from mongo error',e)

if __name__ == '__main__':
    mongo_instance = MongodbClass()
    mongo_instance.get_from_db('zhuji',return_field='_id')