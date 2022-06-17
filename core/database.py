import pymysql

# 连接数据库
import window

con = pymysql.connect(host='112.124.17.13', user='xiaoming', password='123456', database='shengchanshixi',
                      charset='utf8')

# 创建游标
cursor = con.cursor()


# 新增用户
def insertUser(id, password):
    r = selectUser(id, password)
    if r == 1:
        return -1  # 已经存在该用户
    sql = "insert into user (id, password) values ('{}', '{}')".format(id, password)
    cursor.execute(sql)
    con.commit()
    return 1  # 返回1代表插入成功


# 查询用户
def selectUser(id, password):
    sql = "select * from user where id='{}' and password='{}'".format(id, password)
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
    sql = "select * from user where id='{}'".format(window.id)
    cursor.execute(sql)
    result = cursor.fetchall()
    if result == ():
        return None
    return result[0]

# 获取用户的密码
def getPassword():
    sql = "select password from user where id='{}'".format(window.id)
    cursor.execute(sql)
    result = cursor.fetchall()
    if result == ():
        return None
    return result[0][0]

# 获取头像
def getHead():
    sql = "select head from user where id='{}'".format(window.id)
    cursor.execute(sql)
    result = cursor.fetchall()
    if result == ():
        return -1
    else:
        return result


# 设置头像
def setHead(head):
    pass
