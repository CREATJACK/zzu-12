import pymysql
import cfzWindow

# 连接数据库
con = pymysql.connect(host='112.124.17.13', user='root', password='Victory&40413', database='scsi',
                      charset='utf8')

print("数据库连接成功")
# 创建游标
cursor = con.cursor()


# 新增用户
def insertUser(id, pop3):
    r = selectUser(id, pop3)
    if r == 1:
        return -1  # 已经存在该用户
    sql = "insert into user (id, pop3) values ('{}', '{}')".format(id, pop3)
    cursor.execute(sql)
    con.commit()
    return 1  # 返回1代表插入成功


#  查询用户名和密码是否正确
def selectUser(id, password):
    sql = "select * from user where id='{}' and pop3='{}'".format(id, password)
    cursor.execute(sql)
    result = cursor.fetchall()
    if result == ():
        return -1  # 不存在该用户或者密码错误，返回-1
    return 1


# 查询是否存在某用户
def isExistUser(id):
    sql = "select * from user where id='{}'".format(id)
    cursor.execute(sql)
    result = cursor.fetchall()
    if result == ():
        return -1  # 不存在该用户，返回-1
    return 1


# 获得用户的全部信息
def getInformation():
    sql = "select * from user where id='{}'".format(cfzWindow.id)
    cursor.execute(sql)
    result = cursor.fetchall()
    if result == ():
        return None
    return result[0]


# 获取用户的密码
def getPassword():
    sql = "select pop3, imap from user where id='{}'".format(cfzWindow.id)
    cursor.execute(sql)
    result = cursor.fetchall()
    if result == ():
        return None
    return result[0]


# 设置用户的imap授权码
def setPop3andImap(pop3, imap):
    print(pop3, imap, cfzWindow.id)
    if pop3 == '' and imap == '':
        return
    if pop3 != '' and imap != '':
        sql = "update user set pop3='{}', imap='{}' where id= '{}'".format(pop3, imap, cfzWindow.id)
        cursor.execute(sql)
        con.commit()
        return
    if pop3 != '' and imap == '':
        sql = "update user set pop3='{}' where id= '{}'".format(pop3, cfzWindow.id)
        cursor.execute(sql)
        con.commit()
        return
    if pop3 == '' and imap != '':
        sql = "update user set imap='{}' where id= '{}'".format(imap, cfzWindow.id)
        cursor.execute(sql)
        con.commit()
        return
