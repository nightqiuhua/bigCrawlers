import os
import subprocess
import schedule
import time
import multiprocessing

def get_work_files(dir_path):
	for root,dirs,files in os.walk(dir_path):
		for file in files:
			if file.endswith('.py'):
				yield file 

def execute_file(filename):
	command = 'python {}'.format(filename)
	print('command',command)
	try:
		os.system(command)
	except Exception as e:
		print('execute_file error',e)

def consequetial_work(dir_path):
	print('begin working {}'.format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
	for filename in get_work_files(dir_path):
		file = os.path.join(dir_path,filename)
		execute_file(file)

def paralell_work(dir_path):
	print('begin working {}'.format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
	print('the dir_path is',dir_path)
	for filename in get_work_files(dir_path):
		file = os.path.join(dir_path,filename)
		print('file',file)
		process = multiprocessing.Process(target=execute_file,args=(file,))
		process.start()


def schedule_task():
	
	dir_path_gong = 'C:\\Users\\Administrator\\Desktop\\wangban\\gong\\update'
	dir_path_wang = 'C:\\Users\\Administrator\\Desktop\\wangban\\wang'
	schedule.every(180).minutes.do(paralell_work,dir_path_gong)
	schedule.every(180).minutes.do(paralell_work,dir_path_wang)
	
	while True:
		schedule.run_pending()
		time.sleep(1)

def start_spider():
	command = 'python {}'.format(os.path.join(os.path.dirname(os.path.abspath(__file__))),'spiders_scheduler.py')
	print('command',command)
	try:
		os.system(command)
	except Exception as e:
		print('execute_file error',e)

if __name__ == '__main__':
	dir_path = 'C:\\Users\\Administrator\\Desktop\\wangban\\wang'	
	#paralell_work(dir_path)
	#schedule_task()
	start_spider()