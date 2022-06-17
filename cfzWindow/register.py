# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import cfzWindow
import cfzWindow.face
from cfzWindow.dialog import Ui_Dialog
from cfzWindow.main import Ui_Main
from core.database import insertUser, selectUser


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1020, 581)
        Form.setWindowTitle("")
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(590, 130, 411, 341))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton_4 = QtWidgets.QPushButton(self.page)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 180, 93, 28))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"border: 1px solid;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.page)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 180, 93, 28))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"border: 1px solid;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.radioButton = QtWidgets.QRadioButton(self.page)
        self.radioButton.setGeometry(QtCore.QRect(0, 140, 141, 19))
        self.radioButton.setObjectName("radioButton")
        self.formLayoutWidget = QtWidgets.QWidget(self.page)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 50, 301, 65))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 321, 271))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.page_4)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 80, 291, 61))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_3.setStyleSheet("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.pushButton_8 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_8.setGeometry(QtCore.QRect(210, 190, 93, 28))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"border: 1px solid;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 190, 93, 28))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"border: 1px solid;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.stackedWidget.addWidget(self.page_4)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 90, 501, 401))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(590, 70, 91, 28))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(85, 170, 255);\n"
"border: 1px solid;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 70, 111, 29))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border: 1px solid;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(830, 70, 81, 29))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"border: 1px solid;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")

        import os
        if os.path.exists('./personal/individual.txt'):
            self.radioButton.setChecked(True)
            file = open('./personal/individual.txt', 'r')
            id = file.readline()[:-1]
            password = file.readline()
            self.lineEdit_4.setText(id)
            self.lineEdit_5.setText(password)
        self.Form = Form
        Form.setFixedSize(1020, 581)
        Form.face = self.face
        Form.password = self.password
        Form.register = self.register
        Form.pb4 = self.pushButton4
        Form.pb5 = self.pushButton5
        Form.pb6 = self.pushButton6
        Form.pb8 = self.pushButton8
        pixmap = QtGui.QPixmap("./picture/log.png")
        self.label.setPixmap(pixmap)
        self.label_3.setStyleSheet("background-color: #000000")
        self.pushButton.setFixedSize(93, 28)
        self.pushButton_2.setFixedSize(99, 28)
        self.pushButton_3.setFixedSize(93, 28)
        self.pushButton_2.clicked.connect(Form.face)
        self.pushButton.clicked.connect(Form.password)
        self.pushButton_3.clicked.connect(Form.register)
        self.pushButton_4.clicked.connect(Form.pb4)
        self.pushButton_5.clicked.connect(Form.pb5)
        self.pushButton_6.clicked.connect(Form.pb6)
        self.pushButton_8.clicked.connect(Form.pb8)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_4.setText(_translate("Form", "登录"))
        self.pushButton_5.setText(_translate("Form", "清空"))
        self.radioButton.setText(_translate("Form", "记住用户和密码"))
        self.label_2.setText(_translate("Form", "用户ID"))
        self.label_7.setText(_translate("Form", "pop授权码"))
        self.label_6.setText(_translate("Form", "用户ID"))
        self.label_5.setText(_translate("Form", "pop3授权码"))
        self.pushButton_8.setText(_translate("Form", "清空"))
        self.pushButton_6.setText(_translate("Form", "注册"))
        self.pushButton.setText(_translate("Form", "密码登录"))
        self.pushButton_2.setText(_translate("Form", "人脸识别登录"))
        self.pushButton_3.setText(_translate("Form", "注册"))

    # 人脸识别方式登录接口  self.face.label变量用来显示摄像头捕获的数据，self.face.label_2用来显示提示信息
    def face(self):
        self.pushButton_2.setStyleSheet('background-color: rgb(85, 170, 255); border: 1px solid;')
        self.pushButton.setStyleSheet('border: 1px solid;')
        self.pushButton_3.setStyleSheet('border: 1px solid;')
        self.stackedWidget.setCurrentIndex(1)
        self.fWidget = QtWidgets.QWidget()
        face = cfzWindow.face.Ui_Form()
        face.setupUi(self.fWidget)
        face.label_2.setText("欢迎使用人脸识别登陆系统")
        self.fWidget.father = self.Form
        self.fWidget.show()


    # 密码登录方式
    def password(self):
        self.pushButton.setStyleSheet('background-color: rgb(85, 170, 255); border: 1px solid;')
        self.pushButton_2.setStyleSheet('border: 1px solid;')
        self.pushButton_3.setStyleSheet('border: 1px solid;')
        self.stackedWidget.setCurrentIndex(0)

    # 注册按钮
    def register(self):
        self.pushButton_3.setStyleSheet('background-color: rgb(85, 170, 255); border: 1px solid;')
        self.pushButton.setStyleSheet('border: 1px solid;')
        self.pushButton_2.setStyleSheet('border: 1px solid;')
        self.stackedWidget.setCurrentIndex(2)

    # 清空按钮的响应事件
    def pushButton8(self):
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")

    # 登录按钮的响应事件
    def pushButton4(self):
        id = self.lineEdit_4.text()
        password = self.lineEdit_5.text()
        result = selectUser(id, password)
        if result == -1:
            self.d = QtWidgets.QDialog()
            selfd_ui = Ui_Dialog()
            selfd_ui.setupUi(self.d)
            selfd_ui.label.setText("登录失败!")
            self.d.show()
        else:
            cfzWindow.id = id
            cfzWindow.pop3 = password
            if self.radioButton.isChecked():
                file = open("./personal/individual.txt", 'w')
                file.write(self.lineEdit_4.text())
                file.write("\n")
                file.write(self.lineEdit_5.text())
                file.close()
            self.w = QtWidgets.QWidget()
            w_ui = cfzWindow.main.Ui_Main()
            w_ui.setupUi(self.w)
            w_ui.label.show()
            self.w.show()
            self.Form.close()
            cfzWindow.main = self.w

    # 清空按钮的响应事件
    def pushButton5(self):
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")

    # 注册按钮的响应事件
    def pushButton6(self):
        id = self.lineEdit_3.text()
        password = self.lineEdit_2.text()
        result = insertUser(id, password)
        print(result)
        if result == -1:
            d = QtWidgets.QDialog()
            d_ui = Ui_Dialog()
            d_ui.setupUi(d)
            d_ui.label.setText("注册失败!")
            d.show()
        else:
            d = QtWidgets.QDialog()
            d_ui = Ui_Dialog()
            d_ui.setupUi(d)
            d_ui.label.setText("注册成功!")
            d.show()
