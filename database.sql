create database arduino default character set= utf8 collate utf8_general_ci ;
use arduino;

create table data(
	date date,
    time time,
    light integer
);
