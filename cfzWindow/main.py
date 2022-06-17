# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import pickle
import poplib
import re
import shutil
import smtplib
import time
import threading
from email.header import decode_header, Header
from email.mime.text import MIMEText
from email.parser import Parser
from email.utils import parseaddr, formataddr

import jieba
from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup

import core.database
import cfzWindow
from cfzWindow import  modify, enterUser
from cfzWindow.moveMail import EmailUtil


class Ui_Main(object):
    def __init__(self):
        self.good = []
        self.bad = []
        self.emailUtil = EmailUtil('imap.qq.com', '993')
        self.emailUtil.login(cfzWindow.id, cfzWindow.imap)


    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1031, 719)
        self.label = QtWidgets.QLabel(Main)
        self.label.setGeometry(QtCore.QRect(60, 20, 91, 81))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Main)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 461, 81))
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Main)
        self.pushButton.setGeometry(QtCore.QRect(840, 20, 141, 81))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "       text-decoration:none;  \n"
                                      "    background:#05B8CC;\n"
                                      "    color:#f2f2f2;    \n"
                                      "    font-size:20px;  \n"
                                      "    font-family: 微软雅黑,宋体,Arial,Helvetica,Verdana,sans-serif;  \n"
                                      "    font-weight:bold; \n"
                                      "    border-radius:3px;\n"
                                      "}\n"
                                      "QPushButton::pressed{ background: #3C79F2; border-color: #11505C; font-weight: bold; font-family:Microsoft YaHei; }")
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Main)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 220, 93, 61))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "       text-decoration:none;  \n"
                                        "    background:#05B8CC;\n"
                                        "    color:#f2f2f2;    \n"
                                        "    font-size:20px;  \n"
                                        "    font-family: 微软雅黑,宋体,Arial,Helvetica,Verdana,sans-serif;  \n"
                                        "    font-weight:bold; \n"
                                        "    border-radius:3px;\n"
                                        "}\n"
                                        "QPushButton::pressed{ background: #3C79F2; border-color: #11505C; font-weight: bold; font-family:Microsoft YaHei; }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Main)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 310, 93, 61))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "       text-decoration:none;  \n"
                                        "    background:#05B8CC;\n"
                                        "    color:#f2f2f2;    \n"
                                        "    font-size:20px;  \n"
                                        "    font-family: 微软雅黑,宋体,Arial,Helvetica,Verdana,sans-serif;  \n"
                                        "    font-weight:bold; \n"
                                        "    border-radius:3px;\n"
                                        "}\n"
                                        "QPushButton::pressed{ background: #3C79F2; border-color: #11505C; font-weight: bold; font-family:Microsoft YaHei; }")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Main)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 400, 93, 61))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "       text-decoration:none;  \n"
                                        "    background:#05B8CC;\n"
                                        "    color:#f2f2f2;    \n"
                                        "    font-size:20px;  \n"
                                        "    font-family: 微软雅黑,宋体,Arial,Helvetica,Verdana,sans-serif;  \n"
                                        "    font-weight:bold; \n"
                                        "    border-radius:3px;\n"
                                        "}\n"
                                        "QPushButton::pressed{ background: #3C79F2; border-color: #11505C; font-weight: bold; font-family:Microsoft YaHei; }")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(Main)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 130, 811, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.verticalLayoutWidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.listWidget = QtWidgets.QListWidget(self.page)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 811, 541))
        self.listWidget.setObjectName("listWidget")
        self.stackedWidget.addWidget(self.page)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.listWidget_2 = QtWidgets.QListWidget(self.page_5)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 0, 811, 541))
        self.listWidget_2.setObjectName("listWidget_2")
        self.stackedWidget.addWidget(self.page_5)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.page_3)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 100, 781, 441))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.formLayoutWidget = QtWidgets.QWidget(self.page_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 0, 361, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.pushButton_6 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_6.setGeometry(QtCore.QRect(700, 60, 93, 28))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
                                        "       text-decoration:none;  \n"
                                        "    background:#05B8CC;\n"
                                        "    color:#f2f2f2;    \n"
                                        "    font-size:20px;  \n"
                                        "    font-family: 微软雅黑,宋体,Arial,Helvetica,Verdana,sans-serif;  \n"
                                        "    font-weight:bold; \n"
                                        "    border-radius:3px;\n"
                                        "}\n"
                                        "QPushButton::pressed{ background: #3C79F2; border-color: #11505C; font-weight: bold; font-family:Microsoft YaHei; }")
        self.pushButton_6.setObjectName("pushButton_6")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.page_4)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 801, 431))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_9.setGeometry(QtCore.QRect(520, 450, 111, 51))
        self.pushButton_9.setStyleSheet("QPushButton{\n"
                                        "       text-decoration:none;  \n"
                                        "    background:#05B8CC;\n"
                                        "    color:#f2f2f2;    \n"
                                        "    font-size:20px;  \n"
                                        "    font-family: 微软雅黑,宋体,Arial,Helvetica,Verdana,sans-serif;  \n"
                                        "    font-weight:bold; \n"
                                        "    border-radius:3px;\n"
                                        "}\n"
                                        "QPushButton::pressed{ background: #3C79F2; border-color: #11505C; font-weight: bold; font-family:Microsoft YaHei; }")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_10.setGeometry(QtCore.QRect(670, 450, 111, 51))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
                                         "       text-decoration:none;  \n"
                                         "    background:#05B8CC;\n"
                                         "    color:#f2f2f2;    \n"
                                         "    font-size:20px;  \n"
                                         "    font-family: 微软雅黑,宋体,Arial,Helvetica,Verdana,sans-serif;  \n"
                                         "    font-weight:bold; \n"
                                         "    border-radius:3px;\n"
                                         "}\n"
                                         "QPushButton::pressed{ background: #3C79F2; border-color: #11505C; font-weight: bold; font-family:Microsoft YaHei; }")
        self.pushButton_10.setObjectName("pushButton_10")
        self.stackedWidget.addWidget(self.page_4)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser.setGeometry(QtCore.QRect(-5, 1, 811, 431))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_7.setGeometry(QtCore.QRect(530, 460, 111, 51))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
                                        "       text-decoration:none;  \n"
                                        "    background:#05B8CC;\n"
                                        "    color:#f2f2f2;    \n"
                                        "    font-size:20px;  \n"
                                        "    font-family: 微软雅黑,宋体,Arial,Helvetica,Verdana,sans-serif;  \n"
                                        "    font-weight:bold; \n"
                                        "    border-radius:3px;\n"
                                        "}\n"
                                        "QPushButton::pressed{ background: #3C79F2; border-color: #11505C; font-weight: bold; font-family:Microsoft YaHei; }")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_8.setGeometry(QtCore.QRect(680, 460, 101, 51))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
                                        "       text-decoration:none;  \n"
                                        "    background:#05B8CC;\n"
                                        "    color:#f2f2f2;    \n"
                                        "    font-size:20px;  \n"
                                        "    font-family: 微软雅黑,宋体,Arial,Helvetica,Verdana,sans-serif;  \n"
                                        "    font-weight:bold; \n"
                                        "    border-radius:3px;\n"
                                        "}\n"
                                        "QPushButton::pressed{ background: #3C79F2; border-color: #11505C; font-weight: bold; font-family:Microsoft YaHei; }")
        self.pushButton_8.setObjectName("pushButton_8")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.pushButton_5 = QtWidgets.QPushButton(Main)
        self.pushButton_5.setGeometry(QtCore.QRect(670, 20, 151, 81))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
                                        "       text-decoration:none;  \n"
                                        "    background:#05B8CC;\n"
                                        "    color:#f2f2f2;    \n"
                                        "    font-size:20px;  \n"
                                        "    font-family: 微软雅黑,宋体,Arial,Helvetica,Verdana,sans-serif;  \n"
                                        "    font-weight:bold; \n"
                                        "    border-radius:3px;\n"
                                        "}\n"
                                        "QPushButton::pressed{ background: #3C79F2; border-color: #11505C; font-weight: bold; font-family:Microsoft YaHei; }")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_11 = QtWidgets.QPushButton(Main)
        self.pushButton_11.setGeometry(QtCore.QRect(50, 130, 91, 61))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
                                         "       text-decoration:none;  \n"
                                         "    background:#05B8CC;\n"
                                         "    color:#f2f2f2;    \n"
                                         "    font-size:20px;  \n"
                                         "    font-family: 微软雅黑,宋体,Arial,Helvetica,Verdana,sans-serif;  \n"
                                         "    font-weight:bold; \n"
                                         "    border-radius:3px;\n"
                                         "}\n"
                                         "QPushButton::pressed{ background: #3C79F2; border-color: #11505C; font-weight: bold; font-family:Microsoft YaHei; }")
        self.pushButton_11.setObjectName("pushButton_11")


        self.Main = Main
        face = QtGui.QPixmap("./personal/face.png")
        self.label.setPixmap(face)
        self.label_2.setText("当前用户: " + cfzWindow.id)
        Main.setStyleSheet("background-color: white")
        Main.PB1 = self.PB1
        Main.pB2 = self.PB2
        Main.pB3 = self.PB3
        Main.pB4 = self.PB4
        Main.pB5 = self.PB5
        Main.pB6 = self.PB6
        Main.pB7 = self.PB7
        Main.pB8 = self.PB8
        Main.pB9 = self.PB9
        Main.pB10 = self.PB10
        Main.pB11 = self.PB11
        self.listWidget.doubleClicked.connect(self.dc_listWidget)
        self.listWidget_2.doubleClicked.connect(self.dc_listWidget2)

        # 如果存放邮件的目录不存在，先建立目录
        if not os.path.exists('./file/email/' + cfzWindow.id):
            os.mkdir('./file/email/' + cfzWindow.id)
        if not os.path.exists('./file/email/'+cfzWindow.id+'/good/'):
            os.mkdir('./file/email/'+cfzWindow.id+'/good/')
        if not os.path.exists('./file/email/'+cfzWindow.id+'/bad/'):
            os.mkdir('./file/email/'+cfzWindow.id+'/bad/')

        # 判断距离上次读取的间隔是否大于12小时
        if os.path.exists('./personal/last.txt'):
            f = open('./personal/last.txt', 'r')
            last = eval(f.readline())
            now = time.time()
            if (now - last) / 3600000 > 12:
                self.getEmail()  # 调用self.getEmail()的地方，也需要调用self.handleEmails()
                self.handleEmails()
        else:
            f = open('./personal/last.txt', 'w')
            now = time.time()
            f.write(str(now))
            f.flush()
            f.close()
            self.getEmail()
            self.handleEmails()

        # 初始化self.good和self.bad
        self.initGood()
        self.initBad()

        self.retranslateUi(Main)
        self.stackedWidget.setCurrentIndex(1)
        self.pushButton_2.clicked.connect(Main.pB2)
        self.pushButton_3.clicked.connect(Main.pB3)
        self.pushButton_4.clicked.connect(Main.pB4)
        self.pushButton.clicked.connect(Main.PB1)
        self.pushButton_5.clicked.connect(Main.pB5)
        self.pushButton_6.clicked.connect(Main.pB6)
        self.pushButton_9.clicked.connect(Main.pB9)
        self.pushButton_10.clicked.connect(Main.pB10)
        self.pushButton_7.clicked.connect(Main.pB7)
        self.pushButton_8.clicked.connect(Main.pB8)
        self.pushButton_11.clicked.connect(Main.pB11)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Form"))
        self.pushButton.setText(_translate("Main", "修改个人资料"))
        self.pushButton_2.setText(_translate("Main", "收件箱"))
        self.pushButton_3.setText(_translate("Main", "垃圾箱"))
        self.pushButton_4.setText(_translate("Main", "写邮件"))
        self.label_3.setText(_translate("Main", "收件人"))
        self.label_4.setText(_translate("Main", "发件昵称"))
        self.label_5.setText(_translate("Main", "邮件主题"))
        self.pushButton_6.setText(_translate("Main", "发送"))
        self.pushButton_9.setText(_translate("Main", "移到收件箱"))
        self.pushButton_10.setText(_translate("Main", "返回"))
        self.pushButton_7.setText(_translate("Main", "移到垃圾箱"))
        self.pushButton_8.setText(_translate("Main", "返回"))
        self.pushButton_5.setText(_translate("Main", "录入人脸信息"))
        self.pushButton_11.setText(_translate("Main", "手动收取"))

    # listWidget双击事件
    def dc_listWidget(self, e):
        b = self.listWidget.selectedIndexes()
        target = b[0].row()
        cfzWindow.currentFile = self.good[target]
        f = open(self.good[target], 'r', encoding='utf-8')
        content = f.read()
        self.textBrowser.setText(content)
        self.stackedWidget.setCurrentIndex(4)

    # listWidget_2双击事件
    def dc_listWidget2(self, e):
        b = self.listWidget_2.selectedIndexes()
        target = b[0].row()
        cfzWindow.currentFile = self.bad[target]
        f = open(self.bad[target], 'r', encoding='utf-8')
        content = f.read()
        self.textBrowser_2.setText(content)
        self.stackedWidget.setCurrentIndex(3)

    # 修改个人信息槽函数
    def PB1(self):
        self.dialog = QtWidgets.QDialog()
        d_ui = modify.Ui_Dialog()
        d_ui.setupUi(self.dialog)
        self.dialog.father = self
        self.dialog.show()

    # 收件箱槽函数
    def PB2(self):
        print("显示收件箱")#调试信息
        self.initGood()
        self.stackedWidget.setCurrentIndex(0)
        # 加载前先删除上一次列出的数据
        count = self.listWidget.count()
        for i in range(count):
            item = self.listWidget.takeItem(0)
            self.listWidget.removeItemWidget(item)
        formation = []
        for f in self.good:
            fin = open(f, 'r', encoding="utf-8")
            content = fin.read(50)
            formation.append(content)
        self.listWidget.addItems(formation)

    # 垃圾箱槽函数
    def PB3(self):
        print("显示垃圾箱")#调试信息
        self.initBad()
        self.stackedWidget.setCurrentIndex(1)
        # 加载前先删除上一次列出的数据
        count = self.listWidget_2.count()
        for i in range(count):
            item = self.listWidget_2.takeItem(0)
            self.listWidget_2.removeItemWidget(item)
        formation = []
        for f in self.bad:
            fin = open(f, 'r', encoding="utf-8")
            content = fin.read(50)
            formation.append(content)
        self.listWidget_2.addItems(formation)

    # 写邮件槽函数
    def PB4(self):
        self.stackedWidget.setCurrentIndex(2)

    # 录入人脸信息槽函数
    def PB5(self):
        self.capture = QtWidgets.QWidget()
        c_ui = enterUser.Ui_Form()
        c_ui.setupUi(self.capture)
        self.capture.show()


    # 发送邮件的接口
    # cfzWindow.id: 发送者邮箱
    # cfzWindow.password: 发送者邮箱密码
    # self.lineEdit.text(): 接收者邮箱
    # self.lineEdit_2.text(): 发送者昵称
    # self.lineEdit_3.text(): 邮件主题
    # self.plainTextEdit.toPalinText(): 发送内容
    def PB6(self):
        try:
            msg = MIMEText(self.plainTextEdit.toPlainText(), 'plain', 'utf-8')
            msg["From"] = formataddr([self.lineEdit_2.text(), cfzWindow.id])
            msg["To"] = Header(self.lineEdit.text())

            msg['Subject'] = Header(self.lineEdit_3.text(), 'utf-8')
            # 发送邮件
            smtp_server = "smtp.qq.com"
            server = smtplib.SMTP_SSL(smtp_server)
            server.connect(smtp_server, 465)
            server.login(cfzWindow.id, cfzWindow.pop3)
            server.sendmail(cfzWindow.id, self.lineEdit.text(), msg.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print(f"无法发送邮件, 失败原因{e}")
        finally:
            # 关闭服务器
            server.quit()

    def PB7(self):
        tempPath, tempName = os.path.split(cfzWindow.currentFile)
        # qq邮箱服务器端移动
        # self.emailUtil.movetoJunk(cfzWindow.currentFile)
        # 本地移动
        shutil.move(cfzWindow.currentFile, './file/email/' + cfzWindow.id + "/bad/" + tempName)
        QtWidgets.QMessageBox.information(self.Main,
                                          "",
                                          "移动成功",
                                          QtWidgets.QMessageBox.Yes)


    def PB8(self):
        self.PB2()

    def PB9(self):
        tempPath, tempName = os.path.split(cfzWindow.currentFile)
        # qq邮箱服务器端移动
       # self.emailUtil.movetoINBOX(cfzWindow.currentFile)
        # 本地移动
        shutil.move(cfzWindow.currentFile, './file/email/' + cfzWindow.id + "/good/" + tempName)
        QtWidgets.QMessageBox.information(self.Main,
                                          "",
                                          "移动成功",
                                          QtWidgets.QMessageBox.Yes)

    def PB10(self):
        self.PB3()

    def PB11(self):
        # 收取前先重置self.good和self.bad
        self.good=[]
        self.bad=[]
        print("----------手动收取----------")
        goodPath = './file/email/'+cfzWindow.id+"/good/"
        badPath = './file/email/'+cfzWindow.id+'/bad/'
        goodList = os.listdir(goodPath)
        badList = os.listdir(badPath)
        for e in goodList:
            os.remove(goodPath+e)
        for e in badList:
            os.remove(badPath+e)

        p = threading.Thread(target=self.handle_email_tread)
        p.setDaemon(True)
        p.start()

        # # 重新收取邮件
        # self.getEmail()
        # # 进行垃圾邮件识别
        # self.handleEmails()

    def handle_email_tread(self):
        self.getEmail()
        # 进行垃圾邮件识别
        self.handleEmails()

    # 初始化self.good
    def initGood(self):
        # 先把self.good清空
        self.good = []
        # 非垃圾邮件的目录
        goodPath = "./file/email/" + cfzWindow.id + "/good/"
        fileList = os.listdir(goodPath)
        for x in fileList:
            self.good.append(goodPath + x)

    # 初始化self.bad
    def initBad(self):
        # 先把self.bad清空
        self.bad = []
        # 垃圾邮件的目录
        badPath = "./file/email/" + cfzWindow.id + "/bad/"
        fileList = os.listdir(badPath)
        for x in fileList:
            self.bad.append(badPath + x)

    # 爬取邮件的槽函数，并存放到 ./file/email/用户id 目录下
    # cfzWindow.id: 发送者邮箱
    # cfzWindow.password: 发送者邮箱密码
    def getEmail(self):
        # 再次收取文件前，先把存放邮件目录中的所有文件删除掉
        rootPath = './file/email/' + cfzWindow.id + "/"
        goodPath = rootPath + 'good/'
        badPath = rootPath + 'bad/'
        goodList = os.listdir(goodPath)
        badList = os.listdir(badPath)
        for e in goodList:
            os.remove(goodPath + e)
        for e in badList:
            os.remove(badPath + e)
        user = cfzWindow.id
        password = cfzWindow.pop3
        pop3_server = 'pop.qq.com'
        # 连接到POP3服务器
        server = poplib.POP3(pop3_server)
        server.user(user)
        server.pass_(password)
        email_num, email_size = server.stat()
        print("消息的数量: {0}, 消息的总大小: {1}".format(email_num, email_size))
        # # 使用list()返回所有邮件的编号，默认为字节类型的串
        rsp, msg_list, rsp_siz = server.list()
        # 循环遍历每个邮件
        for i in range(0, len(msg_list)):
            filename = './file/email/' + cfzWindow.id + '/邮件%d.txt' % i
            file = open(filename, 'w', encoding='utf-8')
            print("%d==================" % i)
            # 获取一封邮件，索引号从1开始
            index = len(msg_list) - i
            resp, lines, octets = server.retr(index)
            # lindes存储了邮件的原始文本的每一行
            # 可以获得整个邮件的原始文本
            # print(lines)
            msg_content = b'\r\n'.join(lines).decode('utf-8', 'ignore')
            # 解析出邮件：
            msg = Parser().parsestr(msg_content)
            self.print_info(msg, file)
            file.close()
        server.quit()

    # 爬邮件子函数
    def print_info(self, msg, file, indent=0):
        if indent == 0:
            sub = ''
            shoujianren = ''
            fajianren = ''
            for header in ['From', 'To', 'Subject', 'Date']:
                value = msg.get(header, '')
                if value:
                    if header == 'Date':
                        time4 = msg.get("Date") + '\n'
                        time3 = msg.get("Date").split('+')[0]
                        time2 = time3.split('-')[0]
                        # print("time2===============",time2)
                        time1 = time.strptime(time2, '%a, %d %b %Y %H:%M:%S ')
                        # print(time4)
                        file.write(time4)
                        # file.write("时间：%d年%d月%d日 %d:%d:%d\n" % (time1.tm_year, time1.tm_mon, time1.tm_mday, time1.tm_hour, time1.tm_min, time1.tm_sec))
                        break
                    elif header == 'Subject':
                        value = self.decode_str(value)
                        sub = '主题: %s\n' % value

                    elif header == 'From':
                        hdr, addr = parseaddr(value)
                        name = self.decode_str(hdr)
                        value = u'%s <%s>' % (name, addr)
                        # print('%s%s: %s' % ('  ' * indent, header, value))
                        fajianren = '%s: %s\n' % (header, value)
                    else:
                        hdr, addr = parseaddr(value)
                        name = self.decode_str(hdr)
                        value = u'%s <%s>' % (name, addr)
                        # print('%s%s: %s' % ('  ' * indent, header, value))
                        shoujianren = '%s: %s\n' % (header, value)
            file.write(fajianren)
            file.write(shoujianren)
            file.write(sub)
        if msg.is_multipart():

            parts = msg.get_payload()
            for n, part in enumerate(parts):
                self.print_info(part, file, indent + 1)
                if part.get_content_type() == 'text/plain':
                    return

        else:
            content_type = msg.get_content_type()
            if content_type == 'text/plain':
                content = msg.get_payload(decode=True)
                charset = self.guess_charset(msg)
                if charset:
                    content = content.decode(charset)
                if "".join([s for s in content.splitlines(True) if s.strip()]):
                    file.write('Text: %s' % ("".join([s for s in content.splitlines(True) if s.strip()])))
            elif content_type == 'text/html':
                content = msg.get_payload(decode=True)
                charset = self.guess_charset(msg)
                if charset:
                    content = content.decode(charset, 'ignore')
                soup = BeautifulSoup(content, "html.parser")
                if "".join([s for s in soup.text.splitlines(True) if s.strip()]):
                    file.write(('Text: %s' % "".join([s for s in soup.text.splitlines(True) if s.strip()])))
            else:
                filename = msg.get_filename()
                if self.decode_str(filename):
                    file.write('Attachment: %s' % (self.decode_str(filename)))

    # 爬邮件子函数
    def decode_str(self, s):
        value, charset = decode_header(s)[0]
        if charset:
            value = value.decode(charset)
        return value

    # 爬邮件子函数
    def guess_charset(self, msg):
        charset = msg.get_charset()
        if charset is None:
            content_type = msg.get('Content-Type', '').lower()
            pos = content_type.find('charset=')
            if pos >= 0:
                charset = content_type[pos + 8:].split(';')[0]
        return charset

    # 依次处理每一封邮件，判断其是否是垃圾邮件
    def handleEmails(self):
        print("--------开始进行垃圾邮件识别--------")
        filePath = './file/email/' + cfzWindow.id + "/"
        allFile = os.listdir(filePath)
        for x in allFile:
            if os.path.isdir(filePath + x):
                continue
            print(os.path.exists(filePath + x))
            result = self.judgeEmail(filePath + x)
            if result == 1:
                shutil.move(filePath + x, filePath + "good/" + x)
            else:
                shutil.move(filePath + x, filePath + "bad/" + x)

    # 垃圾邮件识别 path是待识别文件的路径 返回-1代表是垃圾邮件，返回1代表是正常邮件
    def judgeEmail(self, path):
        # 加载文件，读取文本内容
        with open(path, "r", encoding="utf8", errors='ignore') as file:
            file_str = file.read()
            index = file_str.find("Text")
            text = file_str[index + 6:]
        # 加载停用词
        with open('./spam_detection/stopwords.txt', encoding='utf8') as file:
            file_str = file.read()
            stopword_list = file_str.split('\n')
        # 加载训练好的逻辑回归模型参数
        with open('./spam_detection/all_model.pickle', 'rb') as file:
            model_para = pickle.load(file)
            cv = model_para['CountVectorizer']
            tfidf = model_para['TfidfTransformer']
            lr = model_para['LogisticRegressionCV']
        # 去除文本中的多个空格和换行
        text = re.sub('\s+', '', re.sub("\n", "", text))
        # 进行分词
        cutwords = [item for item in jieba.lcut(text) if item not in set(stopword_list)]
        text_list = [' '.join(cutwords)]
        # 计算词频
        count = cv.transform(text_list)
        # 计算逆文本词频
        tfidf_matrix = tfidf.transform(count)
        # 得到预测结果（1：spam, 0：ham）
        res = lr.predict(tfidf_matrix)[0]
        # 返回需要的结果
        if res == 1:
            return -1
        else:
            return 1
