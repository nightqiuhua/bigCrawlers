# -*- coding: utf-8 -*-

# Scrapy settings for wangban project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import datetime
import os

BOT_NAME = 'wangban'

SPIDER_MODULES = ['wangban.spiders']
NEWSPIDER_MODULE = 'wangban.spiders'
#SPLASH_URL = 'http://localhost:8050'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER'
# Obey robots.txt rules
#ROBOTSTXT_OBEY = True

BASE_JSONFILE_PATH = 'E:\\工作\\万邦\\工作成果\\crawler_project\\wangban\\wangban\\config'
BASE_LOGFILE_PAHT = 'E:\\工作\\万邦\\工作成果\\crawler_project\\wangban\\wangban\\log'
SPIEDE_FILE_PATH = 'E:\\工作\\万邦\\工作成果\\crawler_project\\wangban\\wangban\\spiders'
CHROME_PATH = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver'
CDATA_FILE_PATH ='E:\\工作\\万邦\\工作成果\\crawler_project\\wangban\\wangban\\data_update\\CORRECT'
EDATA_FILE_PATH ='E:\\工作\\万邦\\工作成果\\crawler_project\\wangban\\wangban\\data_update\\ERROR'
BASE_SELE_LOG_PAHT = 'E:\\工作\\万邦\\工作成果\\crawler_project\\wangban\\wangban\\log\\sele_log'
IMGPATH = 'E:\\工作\\万邦\\工作成果\\crawler_project\\wangban\\wangban\\cleaner\\{}\\{}\\img'


# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 3

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings ansd docs

DOWNLOAD_DELAY =0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'wangban.middlewares.HangzhouSpiderMiddleware': 543,
#    'scrapy_splash.SplashDeduplicateArgsMiddleware':100,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'wangban.middlewares.HangzhouDownloaderMiddleware': 543,
#    #'scrapy_splash.SplashCookiesMiddleware': 723,
#    #'scrapy_splash.SplashMiddleware':725,
#    #'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware':8
}
#DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'


# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    'scrapy.extensions.telnet.TelnetConsole': None,
}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'wangban.pipelines.HangzhouPipeline': 300,
    #'wangban.pipelines.WangBanPipeline':300,
    #'wangban.pipelines.HangzhouPipeline':300
}
#MONGODB_HOST = '127.0.0.1'
#MONGODB_PORT = 27017
#MONGODB_DBNAME = 'gongshu'
#MONGODB_SHEETNAME = 'gongshu'
#

#MYSQL_HOST = "rm-bp1k68h2lq872j040mo.mysql.rds.aliyuncs.com"
#MYSQL_PORT = 3306
#MYSQL_USER ="root"
#MYSQL_PASSWORD="N5QjbPu097Kuz4BV"
#MYSQL_DBNAME ="zhaobiao"

#MYSQL_HOST = "rm-bp1aj66015accj2ojqo.mysql.rds.aliyuncs.com"
#MYSQL_PORT = 3306
#MYSQL_USER ="yc_03"
#MYSQL_PASSWORD="123456789_yc"
#MYSQL_DBNAME ="zhaobiao"
#
MYSQL_HOST = "rm-bp1347o8ygf2t265vho.mysql.rds.aliyuncs.com"
MYSQL_PORT = 3306
MYSQL_USER ="wbpmzb"
MYSQL_PASSWORD="123456789Wbpm"
MYSQL_DBNAME ="wpzb"
#
#MYSQL_HOST = '127.0.0.1'
#MYSQL_PORT = 3306
#MYSQL_USER ="root"
#MYSQL_PASSWORD="123456"
#MYSQL_DBNAME ="zhaobiao"
#HTTPCACHE_STORAGE ='scrapy_splash.SplashAwareFSCacheStorage'
to_day = datetime.datetime.now()
log_file_path = os.path.join(BASE_LOGFILE_PAHT,'{}_{}_{}_.log'.format(to_day.year,to_day.month,to_day.day))
LOG_LEVEL = 'INFO'
LOG_ENCODING = 'utf-8'
LOG_ENABLED = True
LOG_FILE=log_file_path


MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'wangban'
MONGODB_SHEETNAME = ''


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
#------------------------------------------------
SUB_SELE_TASKS = 'wangban:sub_sele_tasks:urls'
URLS_CHECK_TASKS = 'wangban:task_check:urls'
URLS_WORK_TASKS = 'wangban:task_work:urls'
URLS_TEMPHASH_URLS = 'wangban:temp_hash:urls'

#------------------------------------------------
#爬虫路径and任务库
SPIDER_MODULES_LIST = [
{'scr_spider':'ZheJiang','path':'.zhejiang.zhejiang'},
{'scr_spider':'ZheJiangZFCG','path':'.zhejiang.zhejiangzfcg'},
{'scr_spider':'ZheJiangJT','path':'.zhejiang.zhejiangjt'},
{'scr_spider':'ZheJiangSJ','path':'.zhejiang.zhejiangsj'},
{'scr_spider':'JinHua','path':'.jinhua.jinhua'},
{'scr_spider':'JinHhua_Ajax','path':'.jinhua.jinhua_ajax'},
{'scr_spider':'LiShui','path':'.lishui.lishui'},
{'scr_spider':'JiaXing','path':'.jiaxing.jiaxing'},
{'scr_spider':'JiaShan','path':'.jiaxing.jiashan'},
{'scr_spider':'PingHu','path':'.jiaxing.pinghu'},
{'scr_spider':'TongXiang','path':'.jiaxing.tongxiang'},
{'scr_spider':'HaiNing','path':'.jiaxing.haining'},
{'scr_spider':'HaiYang','path':'.jiaxing.haiyang'},
{'scr_spider':'TongLu','path':'.hangzhou.tonglu'},
{'scr_spider':'JianDe','path':'.hangzhou.jiande'},
{'scr_spider':'ChunAn','path':'.hangzhou.chunan'},
{'scr_spider':'FuYang','path':'.hangzhou.fuyang'},
{'scr_spider':'XiHuQu','path':'.hangzhou.xihuqu'},
{'scr_spider':'XiaoShan','path':'.hangzhou.xiaoshan'},
{'scr_spider':'YuHang','path':'.hangzhou.yuhang'},
{'scr_spider':'LinAn','path':'.hangzhou.linan'},
{'scr_spider':'GongShu','path':'.hangzhou.gongshu'},
{'scr_spider':'JiangGan','path':'.hangzhou.jianggan'},
#{'scr_spider':'DaJiangDong','path':'.hangzhou.dajiangdong'},
{'scr_spider':'HangZhou','path':'.hangzhou.hangzhou'},
{'scr_spider':'CiXi','path':'.ningbo.cixi'},
{'scr_spider':'FengHua','path':'.ningbo.fenghua'},
{'scr_spider':'HaiShu','path':'.ningbo.haishu'},
{'scr_spider':'XiangShan','path':'.ningbo.xiangshan'},
{'scr_spider':'XiangShan_Ajax','path':'.ningbo.xiangshan_ajax'},
{'scr_spider':'NiBoBSQ','path':'.ningbo.ningbobaoshuiqu'},
{'scr_spider':'BeiLun','path':'.ningbo.beilun'},
{'scr_spider':'JiangBei','path':'.ningbo.jiangbei'},
{'scr_spider':'NingHai','path':'.ningbo.ninghai'},
{'scr_spider':'YinZhou','path':'.ningbo.yinzhou'},
{'scr_spider':'YuYao','path':'.ningbo.yuyao'},
{'scr_spider':'ZhenHai','path':'.ningbo.zhenhai'},
{'scr_spider':'DaXieKaiFaQu','path':'.ningbo.daxiekaifaqu'},
{'scr_spider':'GuoJiaGaoXinQu','path':'.ningbo.guojiagaoxinqu'},
{'scr_spider':'HangZhouWanXinQu','path':'.ningbo.hangzhouwanxinqu'},
{'scr_spider':'NingHai_Ajax','path':'.ningbo.ninghai_ajax'},
{'scr_spider':'YuYao_Ajax','path':'.ningbo.yuyao_ajax'},
{'scr_spider':'NingBo','path':'.ningbo.ningboshi'},
{'scr_spider':'XinChang','path':'.shaoxing.xinchang'},
{'scr_spider':'ShangYu','path':'.shaoxing.shangyu'},
{'scr_spider':'ShengZhou','path':'.shaoxing.shengzhou'},
{'scr_spider':'ZhuJi','path':'.shaoxing.zhuji'},
{'scr_spider':'YueCheng','path':'.shaoxing.yuecheng'},
{'scr_spider':'ShaoXing','path':'.shaoxing.shaoxing'},
{'scr_spider':'KeQiao','path':'.shaoxing.keqiao'},
#{'scr_spider':'HuangYan','path':'.taizhou.huangyan'},
#{'scr_spider':'LinHai','path':'.taizhou.linhai'},
#{'scr_spider':'LuQiao','path':'.taizhou.luqiao'},
#{'scr_spider':'TianTai','path':'.taizhou.tiantai'},
#{'scr_spider':'XianJu','path':'.taizhou.xianju'},
#{'scr_spider':'WenLing','path':'.taizhou.wenling'},
#{'scr_spider':'YuHuan','path':'.taizhou.yuhuan'},
#{'scr_spider':'YuHuan_Ajax','path':'.taizhou.yuhuan_ajax'},
{'scr_spider':'TaiZhou','path':'.taizhou.taizhou'},
{'scr_spider':'CangNan','path':'.wenzhou.cangnan'},
{'scr_spider':'DongTou','path':'.wenzhou.dongtou'},
{'scr_spider':'LeQing','path':'.wenzhou.leqing'},
{'scr_spider':'LongWan','path':'.wenzhou.longwan'},
{'scr_spider':'LuCheng','path':'.wenzhou.lucheng'},
{'scr_spider':'OuHai','path':'.wenzhou.ouhai'},
{'scr_spider':'PingYang','path':'.wenzhou.pingyang'},
{'scr_spider':'RuiAn','path':'.wenzhou.ruian'},
{'scr_spider':'TaiShun','path':'.wenzhou.taishun'},
{'scr_spider':'WenCheng','path':'.wenzhou.wencheng'},
{'scr_spider':'YongJia','path':'.wenzhou.yongjia'},
{'scr_spider':'WenZhou','path':'.wenzhou.wenzhou'},
{'scr_spider':'JJJSKFQ','path':'.wenzhou.jjjskfq'},
{'scr_spider':'PuTuo','path':'.zhoushan.putuo'},
{'scr_spider':'DaiShan','path':'.zhoushan.daishan'},
{'scr_spider':'DingHaiQu','path':'.zhoushan.dinghaiqu'},
{'scr_spider':'ShengSi','path':'.zhoushan.shengsi'},
{'scr_spider':'ZhouShan','path':'.zhoushan.zhoushan'},
{'scr_spider':'AnJi','path':'.huzhou.anji'},
{'scr_spider':'NanXun','path':'.huzhou.nanxun'},
{'scr_spider':'WuXing','path':'.huzhou.wuxing'},
{'scr_spider':'ChangXing','path':'.huzhou.changxing'},
{'scr_spider':'DeQing','path':'.huzhou.deqing'},
{'scr_spider':'HuZhou','path':'.huzhou.huzhou'},
#{'scr_spider':'HaiNing','path':'.quzhou.haining'},
#{'scr_spider':'QuJiang','path':'.quzhou.qujiang'},
#{'scr_spider':'KaiHua','path':'.quzhou.kaihua'},
#{'scr_spider':'JiangShan','path':'.quzhou.jiangshan'},
#{'scr_spider':'ChangShan','path':'.quzhou.changshan'},
#{'scr_spider':'LongYou','path':'.quzhou.longyou'},
#{'scr_spider':'KeCheng','path':'.quzhou.kecheng'},
{'scr_spider':'QuZhou','path':'.quzhou.quzhou'},
]
#------------------------------------------------
#sql语句
SQL_MODULE_LIST = [
    '.t_zhaobiao',
    '.t_notice_grab'
]
