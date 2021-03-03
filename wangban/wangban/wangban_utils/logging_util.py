from scrapy.utils.project import get_project_settings
SETTINGS = get_project_settings()
import time
import os
import json

class update_logging:
    def __init__(self):
        self.filepath = SETTINGS['CDATA_FILE_PATH']
        self.error_filepath = SETTINGS['EDATA_FILE_PATH']
        
    def record_data(self,data,spider_name):
        update_date = time.strftime("%Y_%m_%d", time.localtime())
        filename = '{}_{}.txt'.format(spider_name,update_date)
        file = os.path.join(self.filepath,filename)
        try:
            with open(file,'a') as f:
                f.write('GET_TIME:{get_time};ONLINE_DATE:{date};NEW_URL:{url};AN_TITLE:{title}; TYPE:{an_type};LARGECLASS:{largeclass};SMALLCLASS:{smallclass};\n'.format(
                            get_time=data['crawling_date'],url= data['an_url'],date=data['on_date'],title=data['an_title'],an_type=data['an_type'],
                                        largeclass=data['an_major'],smallclass=data['an_sub']))
        except Exception as e:
            print('record data error',e)

    def record_error_data(self,data,spider_name):
        update_date = time.strftime("%Y_%m_%d", time.localtime())
        filename = '{}_{}_erorr.txt'.format(spider_name,update_date)
        file = os.path.join(self.error_filepath,filename)
        try:
            with open(file,'a',encoding='utf-8') as f:
                one_jsonobj = json.dumps(data,ensure_ascii=False,indent=4) +";\n"
                f.write(one_jsonobj)
        except Exception as e:
            print('record data error',e)

    def logging_info(self,info,sheet_name,file_path,info_type='default'):
        clean_path = file_path.format(sheet_name)
        file_name = sheet_name +'_'+info_type + '.txt'
        filepath = os.path.join(clean_path,file_name)
        try:
            with open(filepath,'a',encoding='utf-8') as file:
                one_jsonobj = json.dumps(info,ensure_ascii=False,indent=4) +";\n"
                file.write(one_jsonobj)
        except Exception as e:
            print('logging_info error',e)
            raise e