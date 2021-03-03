# coding:utf-8
#import __init__
from celery import Celery
from wangban.tasks import config


# 定义celery对象
celery_app = Celery("wangban")

# 引入配置信息
celery_app.conf.ONCE = {
  'backend': 'celery_once.backends.Redis',
  'settings': {
    'url': 'redis://127.0.0.1:6379/2',
    'default_timeout': 480*60
  }
}

celery_app.config_from_object(config)


# 自动搜寻异步任务
celery_app.autodiscover_tasks(["wangban.tasks.pour_tasks","wangban.tasks.countinfo"])
