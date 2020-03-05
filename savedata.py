import serial
import pymysql
#from time import localtime,strftime

getdata = serial.Serial('COM7',9600)

def getAverage():
    num = 10
    i=0
    result=0
    while(i<num):
        light=getdata.readline()
        light=light[:-2]
        light=eval(light)
        i=i+1
        result+=light
    result=result/float(num)
    return light

while True:
    data=0
    data=getAverage()
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='password', db='arduino', charset='utf8')

    cursor = db.cursor()
    sql = "INSERT INTO data_tb(light) values("+str(data)+");"
    cursor.execute(sql)
    db.commit()




#https://miscel.tistory.com/6