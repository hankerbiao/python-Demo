# MySql
import pymysql

id = '1707100220'
name = 'yxx'
age = 20

# 创建数据库
db = pymysql.connect(host='localhost', user='root', password='*', port=3306, db='spiders')  # db：所使用哪个数据库
cursor = db.cursor()
sql = 'INSERT INTO student(id,name,age)values(%s,%s,%s)'

try:
    cursor.execute(sql, (id, name, age))
    print("插入成功")
    db.commit()
except:
    print("插入失败")
    db.rollback()
db.close()
