import os
import re


#data = re.findall(r'\[(.*)\]/nw',"E3300000001000445113001/nx ,/w 车站/n （/w 含/v 区间/n ）/w 设备/n 安装/vn 及/c 装修/vn 工程施工/nz 监理/vn Ⅰ标/n ,/w [浙江/ns 江南/ns 工程/n 管理/vn 股份有限公司/nis]/nw ,/w 段/Ng 红文/n ,/w 2422500.00/m 元/q ,/w 1035/m;")
#print(data)
with open('right_nm.txt','r',encoding='utf-8') as fp:
	content = fp.read()
	count = 0
	for line in content.split(';'):
		data = re.findall(r'\[(.*)\]/nw',line)
		count += 1
		print(data)
	print(count)