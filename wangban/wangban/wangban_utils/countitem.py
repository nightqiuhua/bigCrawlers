import redis
from wangban_utils.single_mode import singleton
from wangban_utils.redis_util import get_redis_conn,acquire_lock,release_lock
import json

@singleton
class CountIitem:
    """
    计算每个网站当日获取的公告数目
    """
    def __init__(self):
        self.redis_conn = get_redis_conn()


    def __setitem__(self,key,value):
        """
        设置网站抓取的数目
        """
        try:
            identifier = acquire_lock(self.redis_conn,'countIitem')
            self.redis_conn.hset('wangban:daily:countIitem',key,value)
        except Exception as e:
            raise e
        finally:
            release_lock(self.redis_conn,'countIitem',identifier)

    def incr(self,key,increment=1):
        """为哈希表 key 中的指定字段的整数值加上增量 increment """
        try:
            identifier = acquire_lock(self.redis_conn,'countIitem')
            self.redis_conn.hincrby('wangban:daily:countIitem',key,increment)
        except Exception as e:
            raise e
        finally:
            release_lock(self.redis_conn,'countIitem',identifier)

    def get(self,key):
        """返回值"""
        value = self.redis_conn.hget('wangban:daily:countIitem',key)
        output = value.decode('utf-8')
        return output

    def gkeys(self):
        """返回所有键
        return output list
        """
        output = []
        values = self.redis_conn.hkeys('wangban:daily:countIitem')
        output = [value.decode('utf-8') for value in values]
        return output


    def clear(self):
        self.redis_conn.delete('wangban:daily:countIitem')

