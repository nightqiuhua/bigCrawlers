# coding:utf-8

from wangban.tasks.main import celery_app
from wangban.task_store.tasksinput import TasksInput
from wangban.spiders.selecrawlers.seledriver import SeleDriver
from celery_once import QueueOnce
import time

@celery_app.task
def send_tasks():
    """向redis插入work_urls"""
    work_schedule = TasksInput()
    work_schedule.running_task()


@celery_app.task
def start_seletask_1(base=QueueOnce, once={'graceful': True}):
    """启动selenium抓取1"""
    time.sleep(5)
    crawling_spider = SeleDriver()
    crawling_spider.webbrowser_execute()
    crawling_spider.driver.quit()

@celery_app.task
def start_seletask_2(base=QueueOnce, once={'graceful': True}):
    """启动selenium抓取2"""
    time.sleep(10)
    crawling_spider = SeleDriver()
    crawling_spider.webbrowser_execute()
    crawling_spider.driver.quit()

#@celery_app.task
#def start_seletask_3(base=QueueOnce, once={'graceful': True}):
#    """启动selenium抓取3"""
#    time.sleep(15)
#    crawling_spider = SeleDriver()
#    crawling_spider.webbrowser_execute()
#    crawling_spider.driver.quit()