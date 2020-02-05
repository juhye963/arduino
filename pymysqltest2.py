# python3 -m pip install PyMySQL 로 설치부터
import pymysql
 
# 접속
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='password', db='arduino', charset='utf8')
 
# 커서 가져오기
cursor = db.cursor()
 
# SQL 문 만들기
sql = '''insert into data_tb(light) values('555');'''
 
# 실행하기
result=cursor.execute(sql)
 
# DB에 Complete 하기
db.commit()
 
# DB 연결 닫기
db.close()


if result:
    cursor = db.cursor()
    query = '''select * from data_tb;'''
    cursor.execute(query)
    db.commit()
    db.close()
else:
    print("unsuccessful")

##https://www.fun-coding.org/mysql_basic6.html
##https://pymysql.readthedocs.io/en/latest/user/examples.html


