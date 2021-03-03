import __init__
import os
import pymongo
import lxml.html
from mysql_util import MySqlDBClass
from mongo_util import MongodbClass
import requests

import time
import threading
import json
from redis_util import get_redis_conn
import json
import re
from pyhanlp import *
import os
#训练模型
#保存模型
#加载模型
#预测
#
#
# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-07-29 23:24
# 《自然语言处理入门》8.6 自定义领域命名实体识别
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
# 
from pyhanlp import *
import os
from pyhanlp.static import download, remove_file, HANLP_DATA_PATH
import zipfile

AbstractLexicalAnalyzer = JClass('com.hankcs.hanlp.tokenizer.lexical.AbstractLexicalAnalyzer')
PerceptronSegmenter = JClass('com.hankcs.hanlp.model.perceptron.PerceptronSegmenter')
PerceptronPOSTagger = JClass('com.hankcs.hanlp.model.perceptron.PerceptronPOSTagger')
PerceptronNERecognizer = JClass('com.hankcs.hanlp.model.perceptron.PerceptronNERecognizer')

PLANE_ROOT = 'E:\\工作\\万邦\\工作成果\\crawler_project\\wangban\\wangban\\html_ex'
PLANE_CORPUS = os.path.join(PLANE_ROOT, 'NLP_sample.txt')
PLANE_MODEL = os.path.join(PLANE_ROOT, 'model.bin')


recognizer = PerceptronNERecognizer(os.path.join(PLANE_ROOT, 'model.bin')) #加载命令实体分词模型
CWS_MODEL = os.path.join(PLANE_ROOT, 'cws.bin')
analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(CWS_MODEL), PerceptronPOSTagger(), recognizer)


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

HEADERS = {'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',

}

def get_ori_data(mongo_conn,sheet_name):
    for item in mongo_conn.get_all_from_db(sheet_name):
        yield item

def process_item(key_list,item):
    new_item = {}
    new_item['_id'] = item['_id']
    result = data_process(item)
    new_item.update(result)
    return new_item

def data_process(item):
    resp = item['TEXT']
    tree = lxml.html.fromstring(resp)
    zbr = ''
    tbr = ''
    total_m = ''
    for tr in tree.xpath(".//tr"):
        try:
            tr.xpath(".//tr")[0]
        except Exception as e:
            content = tr.xpath(".//text()")
        else:
            content = None
            continue
        if not content:
            continue
        content = ','.join(content)
        content = re.sub(r'\s+','',content)
        content = re.sub(r',+',',',content)
        if not content:
            continue
        #print(analyzer.analyze(content))
        if '招标人' in content:
            zbr = get_zbr(content)
        if '元' in content:
            tbr = get_tbr(content)
            total_m = get_total_money(content)
    result = {'ZBR':zbr,'GYS':tbr,'TOTAL_MONEY':total_m}
    return result

def get_zbr(content):
    zbr = str(analyzer.analyze(content))
    #print(zbr)
    zbr_list = ['浙江大学医学院附属第一医院','杭州电子科技大学','浙江工商大学','浙江师范大学',
    '浙江工业大学','浙江警察学院','浙江省立同德医院','浙江大学医学院附属儿童医院','浙江大学医学院附属邵逸夫医院',
    '浙江大学医学院附属妇产科医院','浙江大学']
    for item in zbr_list:
        if item in zbr:
            return item
    try:
        zbr = re.findall(r'\[(.*?)\]/nw',zbr)[0]
        zbr = re.sub(r'\s',';',zbr)
        zbr = re.sub(r'/.*?;','',zbr)
        zbr = re.sub(r'/.*','',zbr)
    except Exception as e:
        zbr = None
    return zbr

def get_tbr(content):

    tbr_list = ['厦门航空有限公司','国义招标股份有限公司','中铁一局集团有限公司',
    '中兴通讯股份有限公司','中国建筑第八工程局有限公司','中国建筑第七工程局有限公司',
    '中铁二十局集团有限公司','中铁建工集团有限公司','中设设计集团股份有限公司',
    '中交第一公路工程局有限公司','中建钢构有限公司','西南交通大学','珠海格力电器股份有限公司',
    '特变电工股份有限公司','中铁隧道集团有限公司'.'华春建设工程项目管理有限责任公司','许继集团有限公司','丰和营造集团股份有限公司']
    for item in tbr_list:
        if item in content:
            return item
    tbr = str(analyzer.analyze(content))
    print(tbr)
    try:
        tbr = re.findall(r'\[(.*?)\]/nw',tbr)[0]
        tbr = re.sub(r'\s',';',tbr)
        tbr = re.sub(r'/.*?;','',tbr)
        tbr = re.sub(r'/.*','',tbr)
    except Exception as e:
        tbr = None
    return tbr

def get_total_money(content):
    try:
        total_m = re.findall(r',(\d+.?\d+).*元',content)[0]
    except Exception as e:
        total_m = None
    return total_m


def check_result(result):
    for key,value in result.items():
        if not value:
            return False
    return True


def save_result(res,_id,mongo_conn):
    mongo_conn.update_data('t_zhaobiao_data',{'_id':_id},res)
    

def save_error(result):
    pass


def run(ori_sheet):
    mongo_conn = MongodbClass()
    count = 0
    for item in get_ori_data(mongo_conn,ori_sheet):
        #time.sleep(1)
        #if item['_id'] == "http://new.zmctc.com/zjgcjy/InfoDetail/?InfoID=395495c3-dc86-4b20-9671-1104a32ecfed&CategoryNum=004010001":
        #    res = data_process(item)
        res = data_process(item)
        #print(item['ID'],item['LINK'],res)
        #if not res['TOTAL_MONEY']:
        #    mongo_conn.delete_from_db(item['_id'],'t_zhaobiao_data')
        if check_result(res):
            print(res)
            save_result(res,item['_id'],mongo_conn)



if __name__ == '__main__':
    mongo_conn = MongodbClass()
    mysql_conn = MySqlDBClass(SETTINGS)
    ori_sheet = 't_zhaobiao_data'
    run(ori_sheet)
    #zbr

    #tbr


    for item in get_ori_data(mongo_conn,ori_sheet):
        send_able = True
        key_list = ['TOTAL_MONEY','ZBR','GYS']
    #    if not item['TOTAL_MONEY']:
    #        mongo_conn.delete_from_db(item['_id'],'t_zhaobiao_data')
        for key in key_list:
            if not item[key]:
                send_able = False
                break
        if send_able:
        #    print(item['_id'])
        #    mongo_conn.delete_from_db(item['_id'],'t_zhaobiao_data')
            try:
                sql_sen = "UPDATE {table_name} SET ZBR = '{zbr}',GYS = '{tbr}',TOTAL_MONEY='{total_m}' where id='{_id}' ".format(
                                  table_name='t_zhaobiao_data',_id=item['ID'],zbr=item['ZBR'],tbr=item['GYS'],total_m=float(item['TOTAL_MONEY']))
            except Exception as e:
                mongo_conn.update_data('t_zhaobiao_data',{'_id':item['LINK']},{'ZBR':None,'GYS':None,'TOTAL_MONEY':None})
                continue
            print(item['ID'])
            mysql_conn.mysql_done(sql_sen)
        #    #
        #    #
