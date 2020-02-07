# python3 -m pip install PyMySQL 로 설치부터
import pymysql
 
# 접속
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='password', db='arduino', charset='utf8')

## CRUD : Create
try:
    cursor = db.cursor()
    for num in range(200, 210):
        sql = "INSERT INTO data_tb(light) values("+str(num)+");"
        print(sql)
        cursor.execute(sql)
        db.commit()
finally:
    print(cursor.lastrowid)

## CRUD : Read
try:
    cursor = db.cursor()
    sql = "SELECT * FROM data_tb;"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row_data in result:
        print(row_data)       
finally:
    db.close()

## CRUD : Update

## CRUD : Delete
try:
    cursor = db.cursor()
    for num in range(4,54):
        sql = "DELETE FROM data_tb WHERE id = '%s';" % str(num)
        cursor.execute(sql)
        db.commit()
        print(cursor.rowcount)
finally:
    db.close()

## 오류
## pymysql.err.InterfaceError: (0, '')
## -> conn 했으면 짝 맞춰서 close 똑바로 해줘라

##https://www.fun-coding.org/mysql_basic6.html
##https://pymysql.readthedocs.io/en/latest/user/examples.html