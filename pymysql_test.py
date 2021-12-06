# 导入pymysql库
import pymysql

# 连接数据库，创建连接对象connection
connection = pymysql.connect(host="localhost",user="root",password="000000",db="moviedata")

# 创建光标对象，一个连接可以有很多光标，一个光标跟踪一种数据状态
cur = connection.cursor()

# 使用execute()方法执行SQL查询
print(cur.execute("select version()"))

# 使用fetchone()方法获取单条数据
data = cur.fetchone()

print("database version:%s" % data)

# 使用预处理语句创建表
sql = "create table employee(first_name char(20) not null, last_name char(20),age int,sex char(1),income float )"

# 使用execute方法执行sql语句
cur.execute("drop table if exists employee")
cur.execute(sql)

# 关闭数据库连接
connection.close()