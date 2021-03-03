import __init__
from redis_util import get_redis_conn
from tasks import all_tasks
redis_conn = get_redis_conn()
def yield_from_redis(redis_conn):
    empty_enabled = False
    while True:
        found = 0
        while found < 200:
            data = redis_conn.blpop(all_tasks['wencheng']['task_check'],timeout = 100)
            if not data:
                empty_enabled = True
                break
            yield data
            found += 1
        if empty_enabled:
            break

def get_data(redis_conn):
    for data in yield_from_redis(redis_conn):
        #print('data=',data)
        data = data[1]
        redis_conn.lpush(all_tasks['wencheng']['task_queue'],data)
get_data(redis_conn)