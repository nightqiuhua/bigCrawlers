# coding:utf-8

from celery.schedules import crontab
broker_url = "redis://127.0.0.1:6379/1"
result_backend = 'redis://127.0.0.1:6379/2'
worker_concurrency = 3


timezone = 'UTC'
beat_schedule = {
    'test1': {
        'task': 'wangban.tasks.pour_tasks.tasks.send_tasks',
        'schedule': crontab(minute=0, hour="*/8"),
        'args': ()
    },
    'task2': {
        'task': 'wangban.tasks.pour_tasks.tasks.start_seletask_1',
        'schedule': crontab(minute=0, hour="*/8"),
        'args': ()
    },
    'task3': {
        'task': 'wangban.tasks.pour_tasks.tasks.start_seletask_2',
        'schedule': crontab(minute=0, hour="*/8"),
        'args': ()
    },
    'task4': {
        'task': 'wangban.tasks.countinfo.tasks.send_anounce_info',
        'schedule': crontab(minute=0, hour=8),
        'args': ()
    },
}