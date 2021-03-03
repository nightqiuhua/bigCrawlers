import __init__
from mongo_mysql_util import MongoDB_To_MySQL
import time
import os
from redis_util import get_redis_conn
import requests
import re
import urllib.request
from lxml import etree
from lxml.cssselect import CSSSelector
import lxml.html
import string
import requests
import json


HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en',
}
class Error_Reget(MongoDB_To_MySQL):

    #def read_files(self,file_path,sheet_name):
    #    file_name = os.path.join(file_path,'{}_error.txt'.format(sheet_name))
    #    with open(file_name,'r') as file:
    #        content = file.read()
    #        for line in content.split(";"):
    #            if not len(line):
    #                continue
    #            if 'xiangshan' in line:
    #                continue
    #            try:
    #                info =  json.loads(line)
    #            except Exception as e:
    #                print(e,line)
    #                continue
    #            yield info
#
    #def get_ID(self,info,sheet_name):
    #    ID_KEYS = info.get('link_id','NONE')
    #    if ID_KEYS == 'NONE':
    #        link = info.get('id')
    #        ID_KEYS = self.link_to_ID(info,sheet_name)
    #    return ID_KEYS
#
#
    #def link_to_ID(self,info,sheet_name):
    #    ID_KEYS = -10000
    #    sql_sen = "select ID from {} where link = '{}'".format(sheet_name,info['id'])
    #    try:
    #        with self.db.cursor() as cursor:
    #            cursor.execute(sql_sen)
    #            ID_KEYS  = cursor.fetchone()[0]
    #        self.db.commit()
    #    except Exception as e:
    #        print('link_to_ID error',e)
    #    return ID_KEYS
    def get_mongo_primary_key(self,pri_key,cond=''):
        try:
            for item in self.mongo_db.get_all_from_db(self.sheet_name,return_field=pri_key):
                #print(item)
                self.redis_conn.sadd('wangban:{}:mongo_redis'.format(self.sheet_name),item[pri_key])
        except Exception as e:
            print('get mongo primary_key error',e)

    def get_from_mongo(self):
        finished_abled = False
        while True:
            found = 0
            while found <= self.mongo_batch_size:
                row_key = self.redis_conn.spop('wangban:{}:mongo_redis'.format(self.sheet_name))
                if not row_key:
                    finished_abled = True
                    break
                try:
                    row_key = row_key.decode('utf-8')
                    yield row_key
                except Exception as e:
                    print('MySqlDBClass get_from_mongo error',e)
                finally:
                    pass
                found += 1
                print('found',found)
            time.sleep(3)
            if finished_abled:
               break

    def get_result(self,link):
        real_link = link
        try:
            if self.sheet_name == 'beilun':
                try:
                    content = requests.get(link,headers=HEADERS,timeout=15)
                    tree = lxml.html.fromstring(content.text)
                    real_link = tree.xpath('//iframe/@src')[0]
                except Exception as e:
                    raise e
            print('real_link',real_link)
            response = requests.get(real_link,headers=HEADERS,timeout=15)
            result = response.text
        except Exception as e:
            raise e
        return result

    def run_update_mongo(self):
        print('{} {} is sending data'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),self.sheet_name))
        self.get_mongo_primary_key('_id')
        for link in self.get_from_mongo():
            #print('link',link,type(link))
            result = self.get_result(link)
            query_condition={"_id":link}
            new_data={"text":result}
            self.mongo_db.update_data(self.sheet_name,query_condition,new_data)

if __name__ == '__main__':
    err_instance = Error_Reget('beilun')
    err_instance.run_update_mongo()


