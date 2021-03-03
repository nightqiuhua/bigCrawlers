
#from ihome.tasks.sms.tasks import insert_urls

#result = insert_urls.delay()
#print(result.id)
#
import __init__
from wangban.tasks.pour_tasks.tasks import send_tasks,start_seletask_1,start_seletask_2#,start_seletask_3


send_tasks.delay()
start_seletask_1.delay()
start_seletask_2.delay()
#start_seletask_3.delay()