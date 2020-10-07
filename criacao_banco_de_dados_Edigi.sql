CREATE database DBEdigi;
SHow databases;
use DBEdigi;
drop table book;
drop table category;
drop table author;
create table author(
	id_author int auto_increment not null,
	fullname varchar(50) not null,
    email varchar(50)  not null unique,
    instant date not null,
    primary key (id_author)
);
create table category(
	id_category int auto_increment not null,
	name varchar(50) not null unique,    
    instant date not null,
    primary key (id_category)
);
alter table category modify column name varchar(50) not null unique;
create table book(
	id_book int auto_increment not null,
	title varchar(50) not null unique,
	abstract varchar(1000) not null,
	summary varchar(1000) not null,
	num_pages int not null,
	isbn varchar(17) not null,
	edition int not null,
	price float not null,
    instant date not null,
    primary key (id_book),
    id_author int not null,
	id_category int not null
);
alter table book modify column title varchar(50) not null unique;
ALTER TABLE `book` ADD CONSTRAINT `fk_category` FOREIGN KEY ( `id_category` ) REFERENCES `category` ( `id_category` );
ALTER TABLE `book` ADD CONSTRAINT `fk_author` FOREIGN KEY ( `id_author` ) REFERENCES `author` ( `id_author` );
SHOW TABLES;
insert into author (fullname, email, instant) values ('Igor Alves','igor.nascimento@caelum.com','2020-12-24');
SELECT * FROM author;
insert into category (name, instant) values ('ML com Python','2020-12-24');
SELECT * FROM category;
insert into book (title, abstract,summary,num_pages,
	isbn ,	edition ,	price ,    instant , id_author,	id_category) 
    values ("Python to ML",'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
            "introduction to python to ML",50,"978–85–33302-27–3",11,20.00,'2020-12-24', 1,	1);
SELECT * FROM book;
