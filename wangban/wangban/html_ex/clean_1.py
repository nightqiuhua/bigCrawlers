from  pyhanlp import *
import zipfile
import os
import re

with open('NLP.txt','r',encoding='utf-8') as fp:
	content = fp.read()
	for line in content.split(';'):
		if '招标人' in line:
			result = line
		elif '元' in line:
			result = line
		else:
			continue
		with open('NLP_1.txt','a') as fp_1:
			fp_1.write(result+';')

