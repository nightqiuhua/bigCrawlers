import requests 
import os 
from wangban_utils.single_mode import singleton
import urllib.parse 
import time
@singleton
class PicHandler:
    def __init__(self):
        self.headers = {'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',}
        
        #self.

    def pic_download(self,img_url):
        img_body = requests.get(img_url,headers=self.headers)
        time.sleep(1)
        return img_body

#self.source_url = 'http://www.daxie.gov.cn/'
    def pic_save(self,filepath,html_url,img_body):
        img_name = self.name_convertion(html_url)
        img_file = os.path.join(filepath,img_name+'.jpg')
        with open(img_file,'wb') as file:
            file.write(img_body.content)

    def name_convertion(self,input_name,url_to_img =True):
        mark_list = [(':','@'),('/','$'),('.','&')]
        if url_to_img:
            for il_mark,le_mark in mark_list:
                input_name = input_name.replace(il_mark,le_mark)
        else:
            for il_mark,le_mark in mark_list:
                input_name = input_name.replace(le_mark,il_mark)
        return input_name

    def run(self,filepath,html_url,img_url):
        img_body = self.pic_download(img_url)
        self.pic_save(filepath,html_url,img_body)

if __name__ == '__main__':
    filepath = 'C:\\Users\\Administrator\\Desktop\\1'
    img_url = 'http://www.daxie.gov.cn/uploads/f5579f8dbcf244d5be06140d5f57660b.jpg'
    html_url = 'http://www.daxie.gov.cn/art/2015/6/24/art_85336_5497627.html'
    img_hand = PicHandler()
    img_hand.run(filepath,html_url,img_url)

