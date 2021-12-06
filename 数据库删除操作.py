import pymysql

db = pymysql.connect(host="localhost",user="root",password="000000",database="moviedata")

cur = db.cursor()

sql = "delete from employee where age> %s" % (20)

try:
    cur.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()