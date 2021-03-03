import __init__
#from spiders import all_spiders
from spiders.redisspider import RedisSpider
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
import time
import schedule
import os
from threading import Thread
SETTINGS = get_project_settings()
from wangban_utils.updatefilterfunc import UpdateFilterClass
#第一步，先将不同爬虫的task放入redis数据库中，并命名为不同的列表，
#例如，安吉爬虫的任务列表wanbang：anji:an_work_urls.wanbang为工程名，anji为爬虫名,
#an_work_urls为工作列表，爬虫从这里抓取任务,完成数据爬取
#第二步，启动一个或多个爬虫
#第三步，当爬虫空抓的时候，即没有抓取任务时，检查数据是否有缺失，
#并将缺失的数据连接放入对应爬虫的an_work_urls中，让爬虫抓取缺失的数据链接
#第四步，每间隔1个小时，对网页进行问询，爬取新增的信息
#1.数据抓取完毕后，爬虫不需要关闭，让其保持idle状态
#2.每隔一个小时，将任务重新放入缓存数据库当中，进行问询，抓取工作
#3.设定终止条件，判断是否有新条目，设定终止抓取条件，
#终止抓取条件为在前3页当中没有日期新于设定日期
#把实时调度模块独立出来，实时调度模块主要操作tasks库，检查redis_spider返回的response里的日期，
#符合终止条件就停止实时调度模块，
#实时调度模块将一个tasks的url放入缓存数据库的队列中，spider从队列中提取url并开始爬取,
#spider返回一个招投标列表，实时调度模块检查招投标列表中每一个
#招投标的日期，以此来判断是否要抓取该数据。实时调度模块再判断是否满足终止调度条件


def run_spiders():
    settings = get_project_settings()
    configure_logging(settings)
    runner = CrawlerRunner(settings)
    runner.crawl(RedisSpider)
    d = runner.join()
    d.addBoth(lambda _:reactor.stop())
    reactor.run()


if __name__ == '__main__':
    run_spiders()