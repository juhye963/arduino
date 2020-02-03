drop database if exists arduino;
create database arduino default character set= utf8 collate utf8_general_ci ;
DROP USER IF EXISTS  sample@localhost;
create user sample@localhost identified by 'password';
grant all privileges on arduino.* to 'sample'@'localhost';
use arduino;

create table data_tb(
	light 	integer,
	dt		datetime
);

#더미데이터
insert into data_tb(light,dt) values('234',now());
select * from data_tb;