# python3 -m pip install PyMySQL 로 설치부터
import pymysql
 
# 접속
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='password', db='arduino', charset='utf8')

try:
    cursor = db.cursor()
    for num in range(200, 210):
        sql = "INSERT INTO data_tb(light) values("+str(num)+");"
        print(sql)
        cursor.execute(sql)
    db.commit()
finally:
    db.close()

try:
    cursor = db.cursor()
    sql = "SELECT * FROM data_tb"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row_data in result:
        print(row_data[0])
        print(row_data[1])
        print(row_data[2])
        print(row_data[3])        
finally:
    db.close()

##https://www.fun-coding.org/mysql_basic6.html
##https://pymysql.readthedocs.io/en/latest/user/examples.html