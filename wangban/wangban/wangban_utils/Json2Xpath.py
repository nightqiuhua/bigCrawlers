# -*- coding: utf-8 -*-
import json
class XPath:
	def __init__(self,item):
		for key,value in item.items():
			setattr(self,key,value)

class Json2XPath:
	def __init__(self, jsonfile):
		with open(jsonfile,'r',encoding='utf-8') as json_file_data:
			data = json.load(json_file_data)
		item = {}

		for key,value in data["xpath"].items():
			item[key] = value
		self.xp = XPath(item)

	def __str__(self):
		return str(self.xp)

	def get_xpath(self):
		return self.xp

if __name__ == '__main__':
	path = 'G:\\scrapy\\housing\\housingcrawler\\housingcrawler\\json_file\\kejson.json'
	xp = Json2XPath(path).get_xpath()
	print(xp.city_list)