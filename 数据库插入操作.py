import pymysql

connection = pymysql.connect(host="localhost",user="root",password="000000",database="moviedata")

cur = connection.cursor()

sql = """insert into employee(first_name,last_name,age,sex,income)
        values ('Mac','Mohan',20,'M',2000)"""

try:
    cur.execute(sql)
    connection.commit()
except:
    # 如果发生错误则回滚
    connection.rollback()

connection.close()