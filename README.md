Arduino Mini Project - 데이터의 활용
===================
의도(개발계기)
----------
* LCD나 시리얼모니터의 센서값을 활용할 방법 모색
* 텍스트(csv,exel)로 데이터저장, 혹은 DB에 축적, 시각화, 데이터분석 등의 방향으로 확장 가능성
* 텍스트로 데이터를 저장하는 것부터 시작
***
개발환경
-------
* Windows 환경
* 아나콘다(python)
  * 링크 : https://www.anaconda.com/distribution/#download-section (Python 3.7 version)
* mysql 5.7 (workbench)
* XAMPP

***

개발과정 : 2020.01.31~2020.02.07 (작업기간 : 6일, 주말제외)
--------
> ### 01.31~02.03 : 아두이노 회로구성
* 파일명 **_sensor_**
* 조도센서의 값을 LCD로 출력하는 아두이노 회로
  * https://www.facebook.com/doyouknowarduino/videos/491839614333641/
  ![arduino_light_lcd](https://user-images.githubusercontent.com/59054012/75941865-2da3ab00-5ed4-11ea-8d39-08ccaf42f05e.gif)
* CoolTermWin과 디지털 오실로스코프 프로그램 이용하여 데이터 txt로 축적
  * 데이터를 저장할 때 일일이 버튼 눌러야함
  * 실시간으로 데이터 쌓이지 않음

***

> ### 02.04 : python으로 실시간 데이터 그래프
* 파일명 **_getdata.py_**
* pyserial과 matplotlib 이용하여 실시간 데이터 그래프 구현

![python_graph](https://user-images.githubusercontent.com/59054012/75942033-b3bff180-5ed4-11ea-9be0-ee7518817881.png)

* 문제점 : 실시간으로 시각화는 하였으나 데이터를 저장(축적)하지 못함.

***

> ### 02.05~02.06 : python으로 DB연결 공부, 실습
* 파일명 **_database.sql pymysqltest2.py pymysqltest3.py_**
* 위의 문제 해결을 위해 DB에 데이터를 저장하고 웹에서 시각화하는 플랜
* Python으로 아두이노에서 가져온 데이터를 DB에 저장하기 위해 pymysql 모듈에 대해 공부
```
python3 -m pip install PyMySQL ## 파이선에 모듈 설치
```
* 실습 위해 간단한 DB테이블 생성하고 더미데이터 CRUD연습
***
> ### 02.07 : DB에 실제 데이터 축적, PHP로 웹에 시각화(표)
* 파일명 **_savedata.py index.php_**
* 실습한 내용 토대로 DB에 실제 센서데이터 받아서 넣음(데이터베이스에 들어가는 모습 아래에서 확인)  

![realdata_dbconnect](https://user-images.githubusercontent.com/59054012/75942058-c63a2b00-5ed4-11ea-816d-fb4f449e3201.png)  

* 데이터베이스에 저장한 데이터들을 PHP에서 PDO객체를 사용하여 가져와서 talbe 태그를 이용하여 표로 시각화하였다.  
  
  ![web_visualize](https://user-images.githubusercontent.com/59054012/75942072-cdf9cf80-5ed4-11ea-8cd5-9171fca1b1bc.png)  
  
