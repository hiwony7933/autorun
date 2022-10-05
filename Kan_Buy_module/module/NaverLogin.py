from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random
from bs4 import BeautifulSoup as bs

class NaverLogin(object):
    def Naver_log_in(self, id, pw) :        
        naver_url = 'https://www.naver.com/'

        # java script login 
        self.driver.find_element_by_xpath('//*[@id="loinid"]').click()
        time.sleep(random.uniform(0.8,1))
        self.driver.execute_script("document.getElementsByName('id')[0].value = \'" + id + "\'")
        time.sleep(random.uniform(0.8,1))
        self.driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
        time.sleep(random.uniform(0.8,1))
        self.driver.find_element_by_css_selector('.btn_login').click()
        time.sleep(2)
        
        # login 검증
        naver_home = self.driver.current_url # 현재 주소 가져오기
        if naver_home == naver_url : 
            self.textBr('로그인성공')
        else :
            self.textBr('로그인실패 : 로그인 정보를 확인해주세요')   
