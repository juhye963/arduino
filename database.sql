drop database if exists arduino;
create database arduino default character set= utf8 collate utf8_general_ci ;
DROP USER IF EXISTS  sample@localhost;
create user sample@localhost identified by 'password';
grant all privileges on arduino.* to 'sample'@'localhost';
use arduino;

create table data_tb(
	id		int primary key not null auto_increment,
	light 	integer,
	dt		TIMESTAMP not null DEFAULT NOW()
);

#더미데이터
#insert into data_tb(light) values('234');
#insert into data_tb(light) values('6');