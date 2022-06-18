import imaplib
import email
import datetime
import shutil
import os
import cfzWindow
from imap_tools import MailBox, AND


class EmailUtil:
    """
    Email帮助类
    """
    host = 'imap.qq.com'  # 主机IP或者域名
    port = '993'  # 端口
    username = '1784880259@qq.com'  # 用户名
    password = 'ybkphpqpmxwngiaf'  # 密码是授权码
    imap = None  # 邮箱连接对象

    # 查看了一下qq邮箱的，由输出结果可得,包含的文件夹有：
    # 'INBOX'            收件箱
    # 'Sent Messages'    已发送邮件
    # 'Drafts'           草稿箱
    # 'Deleted Messages' 已删除邮件
    # 'Junk'             垃圾邮件
    # mail_box = '**************'  # 邮箱名

    # 初始化
    # 参数：host='imap.qq.com' ; port='993'
    def __init__(self, host, port):
        """初始化方法"""
        self.host = host
        self.port = port
        # 初始化一个邮箱链接对象
        self.mailbox = MailBox(host=self.host)

    # 登陆邮箱
    # 参数：username='....@qq.com' ; password='授权码'
    def login(self, username, password):
        """登录"""
        # print(self.mailbox.fetch())
        self.username = username
        self.password = password
        self.mailbox.login(username=self.username, password=self.password, initial_folder="INBOX")
        # for it in self.mailbox.fetch():
        # print(it.date)
        #   pass

    # 邮件移入垃圾箱
    # 参数：dates[]:需要移入垃圾箱的邮件的邮件发送时间字符串（作为唯一标识符）列表
    # 示例dates=['2022-06-14 09:47:56+08:00', '2022-06-14 09:48:06+08:00']

    # 本地移动：邮件文件名——邮件发送时间字符串（作为唯一标识符）
    def movetoJunk(self, fileName):
        # 切换工作文件夹
        self.mailbox.folder.set('INBOX')
        date = self.date_by_fileName(fileName, "good")
        for it in self.mailbox.fetch():
            if date == it.date_str:  # (str)(it.date)形式示例：2022-06-14 09:48:06+08:00
                uid = it.uid  # 获取该邮件的uid
                # MOVE操作：将当前选择的邮件移动到指定文件夹中
                self.mailbox.move(uid, 'Junk')  # 根据邮件参数uid进行移动

                # 本地操作
                src = "./file/email/" + cfzWindow.id + "/good/" + fileName
                dst = "./file/email/" + cfzWindow.id + "/bad/" + fileName
                shutil.move(src, dst)  # 移动到bad目录

                # 结束
                break

    # 邮件从垃圾箱移入收件箱
    # 参数：dates[]:需要移出垃圾箱的邮件的邮件发送时间字符串（作为唯一标识符）列表
    # 示例dates=['2022-06-14 09:47:56+08:00', '2022-06-14 09:48:06+08:00']
    def movetoINBOX(self, fileName):
        # 切换工作文件夹
        self.mailbox.folder.set('Junk')
        date = self.date_by_fileName(fileName, "bad")
        for it in self.mailbox.fetch():
            if date == it.date_str:  # (str)(it.date)形式示例：2022-06-14 09:48:06+08:00
                uid = it.uid  # 获取该邮件的uid
                # MOVE操作：将当前选择的邮件移动到指定文件夹中
                self.mailbox.move(uid, 'INBOX')  # 根据邮件参数uid进行移动

                # 本地操作
                src = "./file/email/" + cfzWindow.id + "/bad/" + fileName
                dst = "./file/email/" + cfzWindow.id + "/good/" + fileName
                shutil.move(src, dst)  # 移动到good目录
                # 结束
                break

    # 关闭邮箱链接
    def close(self):
        self.mailbox.logout()

    # 读取fileName文件中的第一行，即发送时间，fileName文件名，dir：good正常邮件，bad垃圾邮件
    def date_by_fileName(self, fileName, dir):
        if dir == "good":
            filePath = "./file/email/" + cfzWindow.id+"/good/"+ fileName
        else:
            filePath = "./file/email/" + cfzWindow.id + "/bad/" + fileName
        f = open(filePath, "r", encoding='utf-8')
        lines = f.readlines()
        res = lines[0].replace("\n", "")
        return res

    # 恢复所有垃圾邮件
    def recvAll(self):
        spam_path = "./file/email/" + cfzWindow.id + "/bad/"
        fileNames = os.listdir(spam_path)  # 当前用户下spam_path下的所有文件名
        for fileName in fileNames:
            #
            self.movetoINBOX(fileName)

            """
            date = self.date_by_fileName(fileName,"bad")
            self.mailbox.folder.set('Junk')
            list = self.mailbox.fetch()
            for it in list:
                if date==it.date_str:
                    # 远程
                    uid = it.uid
                    self.mailbox.move(uid, 'INBOX')
                    # 本地
                    src = "./file/email/"+window.id+"/bad/"+fileName
                    dst = "./file/email/"+window.id+"/good/"+fileName
                    shutil.move(src,dst)
                    break
            """

    # 将所有正常邮件都移到垃圾箱
    def moveSpam(self):
        normal_path = "./file/email/" + cfzWindow.id + "/good/"
        fileNames = os.listdir(normal_path)
        for fileName in fileNames:
            #
            self.movetoJunk(fileName)

    # 清理一个指定的垃圾邮件
    def cleanup_by_fileName(self, fileName):
        spam_path = "./file/email/" + cfzWindow.id + "/bad/"
        date = self.date_by_fileName(fileName, "bad")
        for it in self.mailbox.fetch():
            if date == it.date_str:
                uid = it.uid
                self.mailbox.delete(uid)
        # 本地
        filePath = spam_path + fileName
        os.remove(filePath)

    # 清理所有垃圾邮件：
    def clearup(self):
        spam_path = "./file/email/" + cfzWindow.id + "/bad/"
        fileNames = os.listdir(spam_path)
        self.mailbox.folder.set('Junk')
        for fileName in fileNames:
            # 远程
            date = self.date_by_fileName(fileName, "bad")
            for it in self.mailbox.fetch():
                if date == it.date_str:
                    uid = it.uid
                    self.mailbox.delete(uid)
            # 本地
            filePath = spam_path + fileName
            os.remove(filePath)


# 测试
if __name__ == '__main__':
    host = 'imap.qq.com'  # 主机IP或者域名
    port = '993'  # 端口
    username = '1784880259@qq.com'  # 用户名
    password = 'ybkphpqpmxwngiaf'  # 密码
    mail_box = '1784880259@qq.com'  # 邮箱名
    email_util = EmailUtil(host=host, port=port)
    email_util.login(username=username, password=password)
    # list =['2022-06-15 19:39:19-08:00', '2020-09-29 22:19:58-05:00']
    # email_util.movetoJunk(list)
    # email_util.movetoINBOX(list)
    # email_util.close()
    # email_util.date_by_fileName("邮件1","good")
    # email_util.movetoJunk("邮件1")
    # email_util.movetoINBOX("邮件1")
    # email_util.moveSpam()
    # email_util.recvAll()
    # 先将所有邮件移动到垃圾箱，然后再清理
    email_util.moveSpam()
    email_util.clearup()
    print('done')
