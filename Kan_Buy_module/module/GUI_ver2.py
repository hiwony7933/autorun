# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gan_GUI_BUY_ver2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(549, 389)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(275, 80, 241, 171))
        self.textBrowser.setObjectName("textBrowser")
        self.label_kan_name = QtWidgets.QLabel(self.centralwidget)
        self.label_kan_name.setGeometry(QtCore.QRect(60, 20, 191, 21))
        self.label_kan_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kan_name.setObjectName("label_kan_name")

        self.lable_id = QtWidgets.QLabel(self.centralwidget)
        self.lable_id.setGeometry(QtCore.QRect(50, 70, 61, 41))
        self.lable_id.setObjectName("lable_id")
        self.label_pw = QtWidgets.QLabel(self.centralwidget)
        self.label_pw.setGeometry(QtCore.QRect(50, 100, 61, 41))
        self.label_pw.setObjectName("label_pw")
        self.label_cafe = QtWidgets.QLabel(self.centralwidget)
        self.label_cafe.setGeometry(QtCore.QRect(50, 220, 61, 41))
        self.label_cafe.setObjectName("label_Cafe_ID")

        self.lineEdit_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_id.setGeometry(QtCore.QRect(120, 80, 113, 21))
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.lineEdit_pw = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pw.setGeometry(QtCore.QRect(120, 110, 113, 21))
        self.lineEdit_pw.setObjectName("lineEdit_pw")
        self.lineEdit_cafe = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cafe.setGeometry(QtCore.QRect(140, 230, 113, 21))
        self.lineEdit_cafe.setObjectName("lineEdit_cafeid")

        self.label_display = QtWidgets.QLabel(self.centralwidget)
        self.label_display.setGeometry(QtCore.QRect(280, 40, 61, 41))
        self.label_display.setObjectName("label_display")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(280, 270, 121, 61))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setGeometry(QtCore.QRect(20, 270, 121, 61))
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_titname = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_titname.setGeometry(QtCore.QRect(140, 270, 121, 61))
        self.pushButton_titname.setObjectName("pushButton_titname")
        self.pushButton_start_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start_2.setGeometry(QtCore.QRect(400, 270, 121, 61))
        self.pushButton_start_2.setObjectName("pushButton_start_2")

        self.radioButton_test = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_test.setGeometry(QtCore.QRect(120, 150, 100, 20))
        self.radioButton_test.setObjectName("radioButton_test")
        self.radioButton_kan = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_kan.setGeometry(QtCore.QRect(120, 170, 100, 20))
        self.radioButton_kan.setObjectName("radioButton_kan")
        self.radioButton_edo = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_edo.setGeometry(QtCore.QRect(120, 190, 100, 20))
        self.radioButton_edo.setObjectName("radioButton_test")
        self.radioButton_wonder = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_wonder.setGeometry(QtCore.QRect(120, 210, 100, 20))
        self.radioButton_wonder.setObjectName("radioButton_test")

        self.radioButton_cafe = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_cafe.setGeometry(QtCore.QRect(120, 230, 100, 20))
        self.radioButton_cafe.setObjectName("radioButton_test")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 549, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.pushButton_start.clicked.connect(MainWindow.resume)
        self.pushButton_start_2.clicked.connect(MainWindow.pause)
        self.pushButton_titname.clicked.connect(MainWindow.titname)
        self.pushButton_login.clicked.connect(MainWindow.login)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_kan_name.setText(_translate("MainWindow", "공구"))
        self.lable_id.setText(_translate("MainWindow", "아이디"))
        self.label_pw.setText(_translate("MainWindow", "비밀번호"))
        self.label_display.setText(_translate("MainWindow", "상태창"))
        self.pushButton_start.setText(_translate("MainWindow", "시작"))
        self.pushButton_login.setText(_translate("MainWindow", "로그인"))
        self.pushButton_titname.setText(_translate("MainWindow", "최근 게시물"))
        self.pushButton_start_2.setText(_translate("MainWindow", "중지"))
        self.radioButton_kan.setText(_translate("MainWindow", "kan_cafe"))
        self.radioButton_test.setText(_translate("MainWindow", "test_cafe"))

        self.radioButton_edo.setText(_translate("MainWindow", "이도공감"))
        self.radioButton_wonder.setText(_translate("MainWindow", "wonderland"))
        self.label_cafe.setText(_translate("MainWindow", "수동cafeID"))
        
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
