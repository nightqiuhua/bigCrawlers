import pymongo
import requests
from lxml import etree
import re
import lxml.html
from lxml.html.clean import Cleaner
#from scrapy.utils.project import get_project_settings
#SETTINGS = get_project_settings()

SETTINGS = {
#'MYSQL_HOST' : '127.0.0.1',
#'MYSQL_PORT' : 3306,
#'MYSQL_USER' :"root",
#'MYSQL_PASSWORD':"123456",
#'MYSQL_DBNAME' :"zhaobiao",

'MYSQL_HOST' : "rm-bp1k68h2lq872j040mo.mysql.rds.aliyuncs.com",
'MYSQL_PORT' : 3306,
'MYSQL_USER' :"root",
'MYSQL_PASSWORD':"N5QjbPu097Kuz4BV",
'MYSQL_DBNAME' :"zhaobiao",


'MONGODB_HOST' : '127.0.0.1',
'MONGODB_PORT' : 27017,
'MONGODB_DBNAME' : 'wangban',
'MONGODB_SHEETNAME' : '',
}


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
            result = self.mongo_db[sheet_name].insert(data)
        except pymongo.errors.DuplicateKeyError as e:
            self.duplicate_count += 1
            #print('_id',data['_id'])
            print('DuplicateKey number',self.duplicate_count)
            return False
        return result

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
            print('num',detect_num)
        except Exception as e:
            print('MongodbClass detect_from_db error',e)
            return 0
        #print(detect_num)
        return detect_num

    def delete_from_db(self,_id,sheet_name):
        try:
            self.mongo_db[sheet_name].remove({'_id':_id})
            print('delete successfully')
        except Exception as e:
            print('delete from mongo error',e)

if __name__ == '__main__':
    from redis_util import get_redis_conn
    import json
    mongo_instance = MongodbClass()
    redis_conn = get_redis_conn()
    #mongo_instance.get_from_db('zhuji',return_field='_id')
    #select_conditions = {'an_major':'其他交易'}
    ##select_conditions = {'an_major':'工程建设','an_type':"招标公告"}
    ##mongo_instance.detect_from_db('beilun',select_conditions)
    cleaner = Cleaner(page_structure=False, links=False,style=True,scripts=True)
    for data in mongo_instance.get_all_from_db('linan_clean'):
        print(data['ID'])
        #if not data['PUBDATE'].startswith('2019'):
        #    continue
        
        input_value = {}
        input_value[data['LINK']] = {}
        input_value[data['LINK']]['an_county']= data['COUNTY']
        input_value[data['LINK']]['an_type']=data['TYPE']
        input_value[data['LINK']]['an_major']=data['LARGECLASS']
        input_value[data['LINK']]['an_sub']=data['SMALLCLASS']
        input_value[data['LINK']]['an_refer_url']='NONE'
        input_value[data['LINK']]['an_title']=data['TEXTTITLE']
        input_value[data['LINK']]['on_date']=data['PUBDATE']
        print(input_value[data['LINK']]['on_date'])
        input_value[data['LINK']]['type']= 'content'
        input_value[data['LINK']]['name']= 'linan'

        #input_value[data['NG_URL']] = {}
        #input_value[data['NG_URL']]['an_county']= data['NG_AREA']
        #input_value[data['NG_URL']]['an_type']=data['NG_TYPE']
        #input_value[data['NG_URL']]['an_major']='SHEJI'
        #input_value[data['NG_URL']]['an_sub']='NONE'
        #input_value[data['NG_URL']]['an_refer_url']='NONE'
        #input_value[data['NG_URL']]['an_title']=data['NG_TITLE']
        #input_value[data['NG_URL']]['on_date']=str(data["NG_PUBLISH_TIME"])
        #print(input_value[data['NG_URL']]['on_date'])
        #input_value[data['NG_URL']]['type']= 'content'
        #input_value[data['NG_URL']]['name']= 'zhejiangsj'






        dict_value = json.dumps(input_value)
        #关联达
        #input_value = {}
        #input_value[data['_id']] = {}
        #input_value[data['_id']]['title'] ='NONE'
        #input_value[data['_id']]['type'] ='content'
        #input_value[data['_id']]['page'] ='1'
        #dict_value = json.dumps(input_value)
        redis_conn.lpush('wangban:linan:an_url_works',dict_value)
    #count = 0
    #for data in mongo_instance.get_all_from_db('huixunwang_4'):
    #    #if data['_id'] == "http://www.iccchina.com/cost_target/detail/zeegec":
    #    count += 1
    #    filename = 'huixunwang_{}.json'.format(count)
    #    with open(filename,"w",encoding="utf-8") as file:
    #        json.dump(data,file,indent=4,ensure_ascii=False,sort_keys=True)
        

        #text = cleaner.clean_html(data['TEXT'])
        #tree = lxml.html.fromstring(text)
        #tree.make_links_absolute('http://new.zmctc.com/')
        #etree.strip_elements(tree,"script","style","title")
        #element = tree.xpath('//tbody[@type="text/javatbody"]')
        #for ele in element:
        #    ele.clear()
        #content=etree.tostring(tree,encoding='utf-8').decode('utf-8')
        #
        #text = cleaner.clean_html(data['TEXT'])
        #tree = lxml.html.fromstring(text)
        ##淳安 
        ##tree.make_links_absolute('http://www.hzxh.gov.cn/')
        ##etree.strip_elements(tree,"script","style","title")
        ##del_eles = tree.xpath('//font[@class="webfont"]')
        ##for ele in del_eles:
        ##    ele.clear()
        ##西湖
        #tree.make_links_absolute('http://www.hzxh.gov.cn/')
        #etree.strip_elements(tree,"script","style","title")
#
#
        #content=etree.tostring(tree,encoding='utf-8').decode('utf-8')
        #print(data['ID'])
        #print(content)
        #杭州
        #body = lxml.html.fromstring(data['TEXT'])
        #elements = re.findall(r'onclick="DownLoad\((.*?)\)"',data['TEXT'])
        ##print(data['TEXT'])
        #del_ele = tree.xpath('//div[@class="MainTitle"]')
        #for ele in del_ele:
        #    ele.clear()
        #node_elems = tree.xpath('//div/ul/li/a[@title=""]')
        ##print(node_elems)
        #for element,node_elem in zip(elements,node_elems):
        #    str_list = element.replace('\'','')
        #    link_str_1,link_str_2 = str_list.split(',')
        #    href = 'http://file.hzctc.cn/UService/DownLoadFile.aspx?dirtype=3&filepath={}&showName={}'.format(link_str_2,link_str_1)
        #    href = re.sub(r'\s+','',href)
        #    #print('href',href)
        #    node_elem.set('href',href)
        #
        ##element_2 = tree.xpath('//div[@class="content"]')[0]
        #tree.make_links_absolute('http://www.hzctc.cn/')
        #etree.strip_elements(tree,"script","style","title")
        #
        #for ele in tree.xpath('//a[@target="_blank"]'):
        #    #print(ele)
        #    ele.set('title','投标人平台用户请登录投标人平台下载，其他用户请到交易中心窗口领取')
        #    ele.set('href','http://app1.hzctc.cn/')
        ##print(etree.tostring(element_2,encoding='utf-8').decode('utf-8'))
        #content = etree.tostring(tree,encoding='utf-8').decode('utf-8')
        ##content=content.replace('\'','')
        #content = cleaner.clean_html(content)

#
#
        #mongo_instance.update_data('fuyang_clean',{'LINK':data['LINK']},{'TEXT':content})



#http://www.iccchina.com/cost_target/detail/axssuu

