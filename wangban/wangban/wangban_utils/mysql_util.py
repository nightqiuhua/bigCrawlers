import pymysql
from scrapy.utils.project import get_project_settings
from sql_sen import all_sql_sentence
from functools import wraps
from .redis_util import get_redis_conn
#from redis_util import get_redis_conn
SETTINGS = get_project_settings()

def get_mysql_conn(**kwargs):
    settings = get_project_settings()
    host = kwargs.get('MYSQL_HOST',settings['MYSQL_HOST'])
    port = kwargs.get('MYSQL_PORT',settings['MYSQL_PORT'])
    user = kwargs.get('MYSQL_USER',settings['MYSQL_USER'])
    db = kwargs.get('MYSQL_DBNAME',settings['MYSQL_DBNAME'])
    password = kwargs.get('MYSQL_PASSWORD',settings['MYSQL_PASSWORD'])
    return pymysql.connect(host=host,port=port,
            user=user,passwd=password,db=db,charset='utf8')

def singleton(cls):
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return get_instance

@singleton
class MySqlDBClass:
    def __init__(self,**kwargs):
        self.host = kwargs.get('MYSQL_HOST',SETTINGS['MYSQL_HOST'])
        self.port = kwargs.get('MYSQL_PORT',SETTINGS['MYSQL_PORT'])
        self.user = kwargs.get('MYSQL_USER',SETTINGS['MYSQL_USER'])
        self.db_name = kwargs.get('MYSQL_DBNAME',SETTINGS['MYSQL_DBNAME'])
        self.password = kwargs.get('MYSQL_PASSWORD',SETTINGS['MYSQL_PASSWORD'])
        #self.mysql_redis_conn = get_redis_conn()
        self.connect_db()

    def connect_db(self):
        self.db = pymysql.connect(host=self.host,port=self.port,
                user=self.user,passwd=self.password,db=self.db_name,charset='utf8')
        return self.db

    def reconn_db(self):
        try:
            self.db.ping(reconnect=True)
        except:
            self.connect_db()

    def create_table(self,sheet_name):
        try:
            self.reconn_db()
            sql_create_table = all_sql_sentence[sheet_name]['create_table']
            self.db.cursor().execute(sql_create_table)
        except Exception as e:
            print('MySqlDB create_table error',e)

    def insert_into_db(self,data,sheet_name):
        self.create_table(sheet_name)
        try:
            self.reconn_db()
            with self.db.cursor() as cursor:
                sql_insert = all_sql_sentence[sheet_name]['sql_insert']
                if sheet_name == "t_notice_grab":
                    cursor.execute(sql_insert,(data['code'],data['an_title'],data['on_date'],
                                    data['an_content'],data['an_url'],data['specific_area'],data['source_website'],data['an_type'],data['crawling_date']))
                else:
                    cursor.execute(sql_insert,(data['source_website'],data['website_area'],data['specific_area'],
                                    data['an_type'],data['an_major'],data['an_sub'],data['project_title'],data['on_date'],data['an_title'],
                                    data['an_content'],data['an_url'],data['crawling_date'],'1'))
                #cursor.execute(sql_insert,(data['sitename'],data['region'],data['county'],
                #                data['type'],data['largeclass'],data['smallclass'],data['title'],data['pubdate'],data['texttitle'],
                #                data['text'],data['link'],data['gettime'],'1'))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print('MySqlDB insert data error',e)
            raise e
            return False
        return True

    def delete_from_db(self,link,sheet_name):
        try:
            delete_sql = "delete from {} where link = '{}'".format(sheet_name,link)
            self.db.cursor().execute(delete_sql)
        except Exception as e:
            print('MySqlDB delete erorr',e)

    #def detect_existence(self,link,sheet_name):
    #    try:
    #        self.reconn_db()
    #        select_sql = "select count(*) from {} where link = '{}'".format(sheet_name,link)
    #        result = self.db.cursor().execute(select_sql)
    #        if result:
    #            return True 
    #        else:
    #            return False
    #    except Exception as e:
    #        print('MySqlDB detect error',e)
    #        return False
    def detect_existence(self,link,sheet_name):
        try:
            self.reconn_db()
            with self.db.cursor() as cursor:
                select_sql = "select 1 from {} where link = '{}' ".format(sheet_name,link)
                result = cursor.execute(select_sql)
                return result
            self.db.commit()
        except Exception as e:
            print('MySqlDB detect error',e)
            return 0

    def add_auto_id(self,sheet_name):
        try:
            with self.db.cursor() as cursor:
                add_auto_id_sql = "alter table {} add id int auto_increment first,add primary key (id)".format(sheet_name)
                cursor.execute(add_auto_id_sql)
            self.db.commit()
        except Exception as e:
            print('MySqlDB add_auto_id error',e)

    def create_new_column(self,sheet_name,column_name):
        add_column_sql = "alter table {} add {} VARCHAR(100)".format(sheet_name,column_name)
        if column_name == 'id':
            self.add_auto_id(sheet_name)
        else:
            try:
                with self.db.cursor() as cursor:
                    cursor.execute(add_column_sql)
                self.db.commit()
            except Exception as e:
                print('create new column',e)

    def detect_column(self,sheet_name,column_name):
        detect_sql = 'select 1 from information_schema.columns where table_schema = database() and table_name = "{}" and column_name = "{}"'.format(sheet_name,column_name)
        #detect_sql = "select 1 from {} where {} = 1".format(sheet_name,column_name)
        try:
            if self.db.cursor().execute(detect_sql):
                return True 
            else:
                return False
        except Exception as e:
            print('detect column error',e)
            return False

    def delete_redundent_data(self,sheet_name):
        if not self.detect_column(sheet_name,'id'):
            self.add_auto_id(sheet_name)
        delete_re_sql = "delete from " + sheet_name + " where id not in (select dt.miid from (select min(id) as miid from "+sheet_name+" group by link) dt )"
        try:
            with self.db.cursor() as cursor:
                cursor.execute(delete_re_sql)
            self.db.commit()
        except Exception as e:
            print('delete_redundent_data error',e)

    def get_from_db(self,col_field,sheet_name,condition_field,chosen_value):
        chosen_str_value = chosen_value.decode('utf-8')
        get_sql = "select {} from {} where link = '{}'".format(col_field,sheet_name,chosen_str_value)
        try:
            self.reconn_db()
            with self.db.cursor() as cursor:
                cursor.execute(get_sql)
                result = cursor.fetchone()
                data = list(result)
                collumn_names = [d[0] for d in cursor.description]
            self.db.commit()
        except Exception as e:
            print('MySqlDBClass get_from_db error',e)
        #print(data,collumn_names)
        return data,collumn_names

    def get_column_data(self,sheet_name,column,condition_key=''):
        #condition_key = "type = '中标公示' "
        if not len(condition_key):
            cond_limit = ''
        else:
            cond_limit = "where {}".format(condition_key)
        column_data_sql = 'select {} from {} '.format(column,sheet_name) + cond_limit
        try:
            with self.db.cursor() as cursor:
                cursor.execute(column_data_sql)
                for single_item in cursor.fetchall():
                    print(single_item)
                    yield single_item
                    #self.mysql_redis_conn.sadd('wangban:{}:mysql_redis'.format(sheet_name),single_item[0])
            self.db.commit()
        except Exception as e:
            print('MySqlDBClass get_column_data',e)

    def get_data_num(self,sheet_name):
        count_sql = "select count(*) from {} ".format(sheet_name)
        try:
            with self.db.cursor() as cursor:
                cursor.execute(count_sql)
                result = cursor.fetchone()[0]
            self.db.commit()
        except Exception as e:
            print('MySqlDBClass get data number',e)
        #print('result',result)
        return result

    def get_column_names(self,sheet_name):
        column_names_sql = "select * from {} limit 1".format(sheet_name)
        try:
            with self.db.cursor() as cursor:
                cursor.execute(column_names_sql)
                column_names = [d[0] for d in cursor.description]
            self.db.commit()
        except Exception as e:
            print('get column names error',e)
        #print(column_names)
        return column_names

    def get_from_local_db(self,col_field,sheet_name):
        get_sql = "select {} from {} limit 1 ".format(col_field,sheet_name)
        try:
            with self.db.cursor() as cursor:
                cursor.execute(get_sql)
                data = list(cursor.fetchone())
                collumn_names = [d[0] for d in cursor.description]
            self.db.commit()
        except Exception as e:
            print('MySqlDBClass get_from_local_db error',e)
        #print(data,collumn_names)
        return data,collumn_names


if __name__ == '__main__':
    worker_mysql = MySqlDBClass()
    worker_mysql.get_column_data('cangnan','max(gettime)')
    #worker_mysql.detect_existence(3000000,'beilun')
#http://www.blztb.gov.cn/show.aspx?nid=11465#