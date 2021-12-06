# 导入pymysql库
import pymysql

# 连接数据库，创建连接对象connection
connection = pymysql.connect(host="localhost",user="root",password="000000",db="moviedata")

# 创建光标对象，一个连接可以有很多光标，一个光标跟踪一种数据状态
cur = connection.cursor()


