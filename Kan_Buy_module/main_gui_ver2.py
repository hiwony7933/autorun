from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random, json, datetime, csv, sys
from bs4 import BeautifulSoup as bs

from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from module.GUI_ver2 import Ui_MainWindow 

class GUI_ver2(QMainWindow,Ui_MainWindow): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.radioButton_kan.clicked.connect(self.radiobt)
        self.radioButton_test.clicked.connect(self.radiobt)
        self.radioButton_edo.clicked.connect(self.radiobt)
        self.radioButton_wonder.clicked.connect(self.radiobt)
        self.radioButton_cafe.clicked.connect(self.radiobt)
        self.show()

    def login(self) : 
        try : 
            self.id = self.lineEdit_id.text()
            self.pw = self.lineEdit_pw.text()
            self.naver_log_in(self.id, self.pw)
        except : 
            self.textBr('id, pw 정보를 확인해주세요')    

    def radiobt(self) : 
        if self.radioButton_kan.isChecked() : 
            self.cafeid = '29118241'
            self.textBr('kan_cafe selected')
        if self.radioButton_test.isChecked() : 
            self.cafeid = '30383037'
            self.textBr('test_cafe selected')
        if self.radioButton_edo.isChecked() : 
            self.cafeid = '28897146'
            self.textBr('이도공감_cafe selected')
        if self.radioButton_wonder.isChecked() : 
            self.cafeid = '30446764'
            self.textBr('Wonderland_cafe selected')
        if self.radioButton_cafe.isChecked() : 
            self.cafeid = self.lineEdit_cafe.text()
            self.textBr('cafe selected')

    def time_event(self) :
        self.time = QTime.currentTime()
        self.now_time = self.time.toString('hh:mm:ss.zzz')
        return self.now_time

    def textBr(self, comment) : 
        self.textBrowser.append(f'[{self.time_event()}] {str(comment)}')

    def resume(self) : 
        try : 
            while True : 
                self.nexted = self.pagechk(self.cafeid, 0.2)
                if self.befor != self.nexted : 
                    self.textBr(self.nexted)
                    self.comment_last()
                    break
        except : 
            self.textBr('순서확인필요')

    def pause(self) : 
        self.driver.quit()

    def comment_last(self) :    
        # self.driver.find_element_by_xpath('//*[@id="ct"]/div/div/ul/li[1]/div/a[2]/div').click()
        self.driver.find_element_by_xpath('//*[@id="ct"]/div/div/ul/li[1]/div/a[2]').click()
        self.driver.implicitly_wait(10)
        self.content_comment('//*[@id="app"]/div/div/div[3]/div/div/div/div/div')


    def content_comment(self, xpath):
        elem = self.driver.find_element_by_xpath(xpath)
        elem.click()
        elem.send_keys('1')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/div/div[3]/div/div[2]/button[2]').click()
        self.textBr('댓글작성완료')

    def titname(self) :
        try : 
            self.befor = self.pagechk(self.cafeid, 2)
            self.textBr(self.befor)
        except :
            self.textBr('cafeid 체크필요')

    def pagechk(self, cafenum, sec) :
        self.driver.get("https://m.cafe.naver.com/ca-fe/web/cafes/" + cafenum) 
        time.sleep(sec)
        self.html = self.driver.page_source   
        self.bs4 = bs(self.html,"html.parser") 
        self.l = self.bs4.findAll("div", {"class":"list_board"})
        try :
            for i in self.l : 
                self.tit = i.find("strong").text
        except : 
            self.textBr('재실행필요')
        return self.tit

    def naver_log_in(self, id, pw) :
        naver_login_url = "https://nid.naver.com/nidlogin.login#none"
        naver_url = 'https://www.naver.com/'
        
        options = webdriver.ChromeOptions()
        options.add_argument('no-sandbox')
        options.add_argument('disable-dev-shm-usage')
        options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome('./driver/chromedriver', options=options)
        self.driver.get(naver_login_url)
        self.driver.implicitly_wait(10)
        time.sleep(random.uniform(0.8,1))

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

app = QApplication([])
main_dialog = GUI_ver2() 
QApplication.processEvents()
app.exit(app.exec_())



