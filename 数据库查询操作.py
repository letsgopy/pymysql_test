import pymysql

db = pymysql.connect(host="localhost", user="root", password="000000", database="moviedata")

cur = db.cursor()

sql = "select * from employee where income > %s" % (1000)

try:
    # 执行sql语句
    cur.execute(sql)
    # 获取所有记录列表
    results = cur.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("name=%s,lname=%s,age=%s,sex=%s,income=%s" % (fname, lname, age, sex, income))
except:
    print("Error:uable to fetch data")

db.close()
