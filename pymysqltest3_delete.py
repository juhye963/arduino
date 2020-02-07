import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='password', db='arduino', charset='utf8')
try:
    cursor = db.cursor()
    for num in range(4,55):
        sql = "DELETE FROM data_tb WHERE id = '%s';" % str(num)
        cursor.execute(sql)
        db.commit()
        print(cursor.rowcount)
finally:
    db.close()