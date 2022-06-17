# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enterUser.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from face_detect.face_detect import detect
import cfzWindow 

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(906, 605)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 40, 481, 51))
        self.label.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 170, 471, 351))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(760, 40, 121, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(760, 150, 121, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(760, 260, 121, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.my_scan_face = detect(cfzWindow.id)

        self.Form = Form
        Form.pB = self.pB
        Form.pB1 = self.pB2
        Form.pB2 = self.pB3

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.pB)
        self.pushButton_2.clicked.connect(Form.pB1)
        self.pushButton_3.clicked.connect(Form.pB2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "开始录入"))
        self.pushButton_2.setText(_translate("Form", "确定"))
        self.pushButton_3.setText(_translate("Form", "重试"))

    # 开始录入人脸信息按钮
    def pB(self):
        
        self.my_scan_face.load_new_face(self)    #录入人脸
        self.label.setStyleSheet("background-color: black")

    # 确定按钮，退出当前子窗口:
    def pB2(self):
        self.my_scan_face.bk = True
        self.Form.close()

    # 重试按钮，人脸录入失败时再次进行人脸录入
    def pB3(self):
        self.pB()