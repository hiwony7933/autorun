import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("./imjin.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 할당하는 코드

        self.name_Input.returnPressed.connect(self.printTextFunction)
        self.Phone_Input.returnPressed.connect(self.printTextFunction)
        self.Mail_Input.returnPressed.connect(self.printTextFunction)
        self.Number_Input.returnPressed.connect(self.printTextFunction)
        self.CarNumber_input.returnPressed.connect(self.printTextFunction)
        self.ZoneNumber.returnPressed.connect(self.printTextFunction)

        self.Date_Input.returnPressed.connect(self.printTextFunction)
        self.Adult_Input.returnPressed.connect(self.printTextFunction)
        self.Children_Input.returnPressed.connect(self.printTextFunction)

        self.Camping.clicked.connect(self.groupboxRadFunction)
        self.CaravanA.clicked.connect(self.groupboxRadFunction)
        self.CaravanB.clicked.connect(self.groupboxRadFunction)

    def printTextFunction(self) :
        #self.lineedit이름.text()
        #Lineedit에 있는 글자를 가져오는 메서드
        driver.find_element_by_name('r_name').send_keys(self.name_Input.text())
        driver.find_element_by_name('r_hp').send_keys(self.Phone_Input.text())
        driver.find_element_by_name('r_email').send_keys(self.Mail_Input.text())
        driver.find_element_by_name('r_jumin1').send_keys(self.Number_Input.text())
        driver.find_element_by_name('r_car[]').send_keys(self.CarNumber_Input.text()) 

    def groupboxRadFunction(self) :
        if self.Camping.isChecked() : print("Camping Chekced")
        elif self.CaravanA.isChecked() : print("CaravanA Checked")
        elif self.CaravanB.isChecked() : print("CaravanB Checked")


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()