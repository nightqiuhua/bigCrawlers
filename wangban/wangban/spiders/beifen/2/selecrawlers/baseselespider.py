import os
from scrapy.utils.project import get_project_settings
from wangban_utils.Json2Xpath import Json2XPath
SETTINGS = get_project_settings()
BASE_JSONFILE_PATH = SETTINGS['BASE_JSONFILE_PATH']

class BaseSeleSpider:
    def __init__(self):
        self.refined_totalpage = 2
        jsonfile = os.path.join(BASE_JSONFILE_PATH,'{}.json'.format(self.name))
        self.xp = Json2XPath(jsonfile).get_xpath()


    def county_modify(self,item):
        return 'NONE'

    def get_totalpage(self,driver):
        #获取总页数，没有总页数，设置总页数为1
        try:
            total_page = driver.find_element_by_xpath(self.xp.total_page).text
            total_page = re.findall(r'1 / (\d+)',total_page,re.I)[0]
            int(total_page)
        except ValueError:
           total_page = '1'
        total_page = self.set_totalpage(total_page)
        return total_page


    def service_able_check(self,driver):
        return True

    def set_totalpage(self,orignal):
        if int(orignal) > self.refined_totalpage:
            orignal = self.refined_totalpage
        return orignal


    def presence_elements(self,driver):
        return self.xp.column

    def get_elements(self,driver):
        try:
            elements = driver.find_elements_by_xpath(self.xp.column)
        except Exception as e:
            print('get_elements error',e)
            elements = []
        return elements

    def get_an_title(self,element,driver):
        an_title = 'NONE'
        try:
            an_title = element.find_element_by_xpath(self.xp.an_title).get_attribute('title')
        except Exception as e:
            print('get an title error',e)
        if not an_title:
            an_title = 'NONE'
        return an_title

    def get_on_date(self,element,driver):
        on_date = 'NONE'
        try:
            on_date = element.find_element_by_xpath(self.xp.on_date).text
        except Exception as e:
            print('get on date error',e)
        if not on_date:
            on_date = 'NONE'
        return on_date

    def get_an_sub(self,an_sub,element,driver):
        
        return an_sub

    def get_an_county(self,element,driver):
        an_county = 'NONE'
        return an_county

    def get_elem_url(self,elem,driver):
        element_url = self.source_url
        try:
            element_url = elem.find_element_by_xpath(self.xp.an_url).get_attribute('href')
        except Exception as e:
            print('get elem url error',e)
        if not element_url:
            element_url = self.source_url
        return element_url

    def click_next_page(self,driver,**kwgs):
        try:
            driver.find_element_by_xpath(self.xp.next_page).click()#点击翻页
            time.sleep(7)
        except Exception as e:
            driver.find_element_by_xpath(self.xp.next_page).click()#点击翻页
            time.sleep(7)


    def county_modify(self,item):
        return 'NONE'
        
    def get_content(self,driver):
        content = driver.find_element_by_xpath('//body').get_attribute('innerHTML')#获取网页html
        return content