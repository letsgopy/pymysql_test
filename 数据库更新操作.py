import pymysql

db = pymysql.connect(host="localhost",user="root",password="000000",database="moviedata")

cur = db.cursor()

sql="update employee set age=age+1 where sex='M'"

try:
    cur.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()