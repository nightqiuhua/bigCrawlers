from redis_util import get_redis_conn
import re
import json

redis_conn = get_redis_conn()
with open("E:\\工作\\万邦\\工作成果\\crawler_project\\wangban_utils\\慧讯网\\处理\\clean.json","r") as file:
	content = file.read()
	content = re.sub(r'\s+','',content)
	for item in content.split(';'):
		print(item)
		data = json.loads(item)
		redis_conn.lpush('wangban:hxw:work_url',data)

