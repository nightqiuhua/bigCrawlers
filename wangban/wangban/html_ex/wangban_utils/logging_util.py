#from scrapy.utils.project import get_project_settings
#SETTINGS = get_project_settings()
import time
import os
import json

class update_logging:
    #def __init__(self):
    #    #self.filepath = SETTINGS['DATA_FILE_PATH']
        
    def record_data(self,data,filepath,spider_name):
        update_date = time.strftime("%Y_%m_%d", time.localtime())
        filename = '{}_{}.txt'.format(spider_name,update_date)
        file = os.path.join(filepath,filename)
        try:
            with open(file,'a') as f:
                f.write('GET_TIME:{get_time};ONLINE_DATE:{date};NEW_URL:{url};AN_TITLE:{title}; TYPE:{an_type};LARGECLASS:{largeclass};SMALLCLASS:{smallclass};\n'.format(
                            get_time=data['crawling_date'],url= data['an_url'],date=data['on_date'],title=data['an_title'],an_type=data['an_type'],
                                        largeclass=data['an_major'],smallclass=data['an_sub']))
        except Exception as e:
            print('record data error',e)

    def logging_info(self,info,sheet_name,file_path,info_type='default'):
        file_name = sheet_name +'_'+info_type + '.txt'
        filepath = os.path.join(file_path,file_name)
        try:
            with open(filepath,'a',encoding='utf-8') as file:
                one_jsonobj = json.dumps(info,ensure_ascii=False,indent=4) +";\n"
                file.write(one_jsonobj)
        except Exception as e:
            print('logging_info error',e)
            raise e
