#
from lxml import etree
import pymysql
import re
import time
from lxml.html import fromstring,tostring
#from scrapy.utils.project import get_project_settings
from sql_sen import all_sql_sentence
#from ningboshi import sql_ningboshi_insert
from zhejiang import sql_zhejiang_insert
from functools import wraps
from mongo_util import MongodbClass
from urllib.parse import urljoin
from itertools import chain
from lxml.html.clean import Cleaner

#from redis_util import get_redis_conn

#SETTINGS = get_project_settings()

SETTINGS = {
#'MYSQL_HOST' : '127.0.0.1',
#'MYSQL_PORT' : 3306,
#'MYSQL_USER' :"root",
#'MYSQL_PASSWORD':"123456",
#'MYSQL_DBNAME' :"zhaobiao",

#'MYSQL_HOST' : "rm-bp1347o8ygf2t265vho.mysql.rds.aliyuncs.com",
#'MYSQL_PORT' : 3306,
#'MYSQL_USER' :"wbpmzb",
#'MYSQL_PASSWORD':"123456789Wbpm",
#'MYSQL_DBNAME' :"wpzb",
#
#'MONGODB_HOST' : '127.0.0.1',
#'MONGODB_PORT' : 27017,
#'MONGODB_DBNAME' : 'wangban',
#'MONGODB_SHEETNAME' : '',
#
'MYSQL_HOST' : "rm-bp1347o8ygf2t265vho.mysql.rds.aliyuncs.com",
'MYSQL_PORT' : 3306,
'MYSQL_USER' :"wbpmzb",
'MYSQL_PASSWORD':"123456789Wbpm",
'MYSQL_DBNAME' :"wpzb",
}


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

AREA_BASE = {
'杭州':['杭州','上城','下城','江干','拱墅','西湖','滨江','萧山','余杭','富阳','临安','桐庐','淳安','建德'],
'宁波':['宁波','海曙','江北','北仑','镇海','鄞州','奉化','余姚','慈溪','象山','宁海','国家高新区','大榭开发区','杭州湾新区','保税区'],
'温州':['温州','鹿城','龙湾','瓯海','洞头','瑞安','乐清','永嘉','平阳','苍南','文成','泰顺',],
'绍兴':['越城','柯桥','上虞','新昌','嵊州','诸暨'],
'金华':['婺城','金东','兰溪','义乌','东阳','永康','浦江','武义','磐安',],
'嘉兴':['嘉兴','南湖','秀洲','嘉善','海盐','海宁','平湖','桐乡',],
'湖州':['湖州','吴兴','南浔','德清','长兴','安吉',],
'衢州':['衢州','柯城','衢江','龙游','江山','常山','开化',],
'舟山':['定海','普陀','岱山','嵊泗',],
'台州':['椒江','黄岩','路桥','临海','温岭','玉环','天台','仙居','三门',],
'丽水':['莲都','龙泉','青田','云和','景宁畲族自治','庆元','缙云','遂昌','松阳']
}

#@singleton
class MySqlDBClass:
    def __init__(self,kwargs):
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

    def mysql_done(self,sql_sen):
        try:
            self.reconn_db()
            with self.db.cursor() as cursor:
                result = cursor.execute(sql_sen)
                #print('modify mysql')
            self.db.commit()
            time.sleep(0.1)
        except Exception as e:
            print('MySqlDBClass update_table error',e)
            return False
        return True

    def create_table(self,sheet_name):
        try:
            self.reconn_db()
            sql_create_table = all_sql_sentence[sheet_name]['create_table']
            self.db.cursor().execute(sql_create_table)
        except Exception as e:
            print('MySqlDB create_table error',e)

    def insert_into_db(self,data,sheet_name):
        #self.create_table(sheet_name)
        try:
            self.reconn_db()
            with self.db.cursor() as cursor:
                sql_insert = all_sql_sentence['t_zhaobiao']['sql_insert']
                #sql_insert =sql_zhejiang_insert
                #if data.get('COUNTY',0):
                #cursor.execute(sql_insert,(data['source_website'],data['website_area'],data['specific_area'],
                #                data['an_type'],data['an_major'],data['an_sub'],data['project_title'],data['on_date'],data['an_title'],
                #                data['an_content'],data['an_url'],data['crawling_date'],'1'))
                #cursor.execute(sql_insert,(data['sitename'],data['region'],data['county'],
                #                data['type'],data['largeclass'],data['smallclass'],data['title'],data['pubdate'],data['texttitle'],
                #                data['text'],data['link'],data['gettime'],'1'))
                cursor.execute(sql_insert,(data['SITENAME'],data['REGION'],data['COUNTY'],
                                data['TYPE'],data['LARGECLASS'],data['SMALLCLASS'],data['TITLE'],data['PUBDATE'],data['TEXTTITLE'],
                                data['TEXT'],data['LINK'],data['GETTIME'],'1'))           
                #cursor.execute(sql_insert,(data['class_1'],data['class_2'],data['class_3'],
                #                data['province'],data['city'],data['mt_name'],data['link'],data['mt_html'],data['pubdate'],
                #                data['gettime']))
                #cursor.execute(sql_insert,(data['provine'],data['city'],data['county'],
                #                data['year'],data['month'],data['num'],data['name'],data['model'],
                #                data['specification'],data['unit'],data['after_tax_price'],data['tax_price'],data['tax_rate'],
                #                data['note']))
            self.db.commit()
        except Exception as e:
            print('MySqlDB insert data error',e)
            raise e


    def detect_existence(self,link,sheet_name):
        try:
            select_sql = "select count(*) from {} where link = '{}'".format(sheet_name,link)
            result = self.db.cursor().execute(select_sql)
        except Exception as e:
            print('MySqlDB detect error',e)
            return False
        return result

#delete_re_sql = "delete from " + sheet_name + " where id not in (select dt.miid from (select min(id) as miid from "+sheet_name+" group by link) dt )"
    def get_from_db(self,col_field,sheet_name,condition_field,chosen_value):
        chosen_str_value = chosen_value.decode('utf-8')
        get_sql = "select {} from {} where ID = '{}'".format(col_field,sheet_name,chosen_str_value)
        #get_sql = "select ID from xunjia where gettime > '2019-04-14 09:01:37'"
        try:
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


    def get_column_data(self,sheet_name,column,cond_limit=''):
        if len(cond_limit):
            cond_limit = 'where '+ cond_limit
        column_data_sql = 'select {} from {} '.format(column,sheet_name) + cond_limit
        try:
            with self.db.cursor() as cursor:
                cursor.execute(column_data_sql)
                for single_item in cursor.fetchall():
                    yield single_item[0]
                    #self.mysql_redis_conn.sadd('wangban:{}:mysql_redis'.format(sheet_name),single_item[0])
                    #self.mysql_redis_conn.lpush('wangban:{}:mysql_redis'.format(sheet_name),single_item[0])
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
        print(column_names)
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

    def get_mysql_sth(self,sql_sen):
        items = []
        try:
            with self.db.cursor() as cursor:
                cursor.execute(sql_sen)
                #return cursor.fetchone()
                for single_item in cursor.fetchall():
                    print(single_item[0])
                    #items.extend(list(single_item))
                    yield single_item[0]
            self.db.commit()

            #return items
        except Exception as e:
            print('MySqlDBClass get_from_local_db error',e)

    def update_table(self,sql_sen):
        mongo_conn = MongodbClass()
        for item in mongo_conn.get_all_from_db('yuhang_clean'):
            #sql_sen = "UPDATE {table_name} SET title ='{new_title}',texttitle='{new_title}' where id='{_id}' ".format(
            #                  table_name='t_zhaobiao',new_title=item['TITLE'],_id=item['ID'])
            #item['PUBDATE'] = re.findall(r'(\d+-\d+-\d+)',item['PUBDATE'])[0]
            sql_sen = "UPDATE {table_name} SET TEXT ='{text}' where id='{_id}' ".format(
                              table_name='t_zhaobiao',_id=item['ID'],text=item['TEXT'])
            if item['TEXT'] == '':
                print('kong',item['ID'])
                continue
            result = self.mysql_done(sql_sen)


    def delete_by_id(self):
        get_id_sql = "select ID from t_xxj_original where CL_MONTH = 12 and CL_YEAR = 2019"
        for _id in self.get_mysql_sth(get_id_sql):
            delete_sql = "delete from t_xxj_original where ID ='{}' ".format(str(_id))
            self.mysql_done(delete_sql)


if __name__ == '__main__':
    sql_sen_1 = 'select region from t_zhaobiao_2 group by region'
    sql_sen_2 = 'select largeclass from t_zhaobiao_2 where region = "南浔" group by largeclass'
    sql_sen_3 = 'select type from t_zhaobiao_2 where region = "南浔" and largeclass= "{}" group by type'
    sql_sen_4 = 'select smallclass from t_zhaobiao_2 where region = "南浔" and largeclass= "{}" group by smallclass'
    sql_sen_5='select * from t_zhaobiao where sitename = "嘉兴市公共资源交易网" and largeclass= "工程建设" and smallclass= "招标公告" limit 1'
    worker_mysql = MySqlDBClass(SETTINGS)
    worker_mysql.delete_by_id()
#
    #worker_mysql.get_mysql_sth('select id from t_zhaobiao where link = "http://ggzy.wuxing.gov.cn/jyxx/zfcg/jggg/20190712/i2243645.html"')
    #worker_mysql.get_mysql_sth('select gettime from t_zhaobiao where id = "2001101"')
    #sql_sen = "select text from t_zhaobiao where id = '2220606'"
    #db_result = worker_mysql.get_mysql_sth(sql_sen)
    ##浙江省公共资源交易网

