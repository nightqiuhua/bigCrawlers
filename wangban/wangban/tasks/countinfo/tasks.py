# coding:utf-8
from wangban.tasks.main import celery_app
from wangban.task_store.tasksinput import TasksInput
from wangban.spiders.selecrawlers.seledriver import SeleDriver
from celery_once import QueueOnce
import time

@celery_app.task
def send_anounce_info():
    from wangban.wangban_utils.countitem import CountIitem
    from wangban.wangban_utils.send_email import send_email
    from wangban.work_urls import all_work_urls
    """计算抓取到的网站公告信息数据，并将一天内没有公告的网站信息发送过来"""
    count_obj = CountIitem()
    no_anouncement_web = []
    for key in count_obj.gkeys():
        value = count_obj.get(key):
        if not int(value):
            no_anouncement_web.append(key)

    to_addr = '1320551630@qq.com'
    title = '万邦招投标信息'
    msg_body = ''

    if len(no_anouncement_web):
        msg_body = '{} 未抓取到信息'.format(','.join(no_anouncement_web))
    else:
        msg_body = " 所有网站都有信息 "
    
    send_email(to_addr,title,msg_body)
    count_obj.clear()
    for key in list(all_work_urls.keys()):
        count_obj.incr(key)





