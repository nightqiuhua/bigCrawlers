import __init__
import multiprocessing
from seledriver import SeleDriver
from wangban_utils.redis_util import get_redis_conn
import json
import time

class MultiSeleCrawler:
    def __init__(self,concurrency=2):
        self.concurrency = concurrency

    def run(self):
        self.create_process()

    def create_process(self):
        p = multiprocessing.Pool(processes=self.concurrency)
        try:
            for _ in range(self.concurrency):
                process = p.apply_async(func=self.worker)
            p.close()
            p.join()
        except Exception as e:
            print('create_process error',e)

    def worker(self):
        try:
            self.start_crawling()
        except Exception as e:
            print('worker error reason :',e)

    def start_crawling(self):
        crawling_spider = SeleDriver()
        crawling_spider.webbrowser_execute()
        crawling_spider.webbrowser_close()


if __name__ == '__main__':
    jiande_sele = MultiSeleCrawler()
    jiande_sele.run()
    #time.sleep(45