from selenium import webdriver
import time, random
from bs4 import BeautifulSoup as bs

from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from module.GUI_ver2 import Ui_MainWindow 
from module.NaverLogin import NaverLogin
from module.Comment import Comment

class GUI_ver2(QMainWindow,Ui_MainWindow, NaverLogin, Comment): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.radioButton_kan.clicked.connect(self.radiobt)
        self.radioButton_test.clicked.connect(self.radiobt)
        self.radioButton_edo.clicked.connect(self.radiobt)
        self.radioButton_wonder.clicked.connect(self.radiobt)
        self.radioButton_cafe.clicked.connect(self.radiobt)
        self.show()

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

    def textBr(self, comment) : 
        self.textBrowser.append(f'[{self.time_event()}] {str(comment)}')

    def time_event(self) :
        self.time = QTime.currentTime()
        self.now_time = self.time.toString('hh:mm:ss.zzz')
        return self.now_time

    def login(self) : 
        get_naver_url = "https://nid.naver.com/nidlogin.login"
        options = webdriver.ChromeOptions()
        options.add_argument('no-sandbox')
        options.add_argument('disable-dev-shm-usage')
        options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome('./driver/chromedriver', options=options)
        self.driver.get(get_naver_url)
        self.driver.implicitly_wait(10)
        time.sleep(random.uniform(0.8,1))

        try : 
            self.id = self.lineEdit_id.text()
            self.pw = self.lineEdit_pw.text()
            self.Naver_log_in(self.id, self.pw)
        except : 
            self.textBr('id, pw 정보를 확인해주세요')    

    def titname(self) :
        try : 
            self.befor = self.pagechk(self.cafeid, 2)
            self.textBr(self.befor)
        except :
            self.textBr('cafeid 체크필요')

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

    def pagechk(self, cafenum, sec) :
        self.driver.get("https://m.cafe.naver.com/ca-fe/web/cafes/" + cafenum) 
        time.sleep(sec)
        self.html = self.driver.page_source   # 현재 페이지 소스 가져오기
        self.bs4 = bs(self.html,"html.parser") # BeautifulSoup로 페이지 소스 파싱
        self.l = self.bs4.findAll("div", {"class":"list_board"})
        try :
            for i in self.l : 
                self.tit = i.find("strong").text
                # self.textBr(self.tit)
        except : 
            self.textBr('재실행필요')
        return self.tit

    def pause(self) : 
        self.driver.quit()

app = QApplication([])
main_dialog = GUI_ver2() 
QApplication.processEvents()
app.exit(app.exec_())