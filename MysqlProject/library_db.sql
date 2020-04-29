create database library;
use library;

DROP TABLE IF EXISTS Shelf;
CREATE TABLE Shelf(
	id int unsigned not null AUTO_INCREMENT primary key,
	position varchar(255)
);

DROP TABLE IF EXISTS Category;
CREATE TABLE Category(
	id int unsigned not null AUTO_INCREMENT primary key,
	name varchar(255) not null default ''
);


DROP TABLE IF EXISTS Category2Shelf;
CREATE TABLE Category2Shelf(
	shelf_id int unsigned not null,
	category_id int unsigned not null,
	foreign key(shelf_id) REFERENCES Shelf(id),
	foreign key(category_id) REFERENCES Category(id)
);

DROP TABLE IF EXISTS Author;
CREATE TABLE Author (
	id int unsigned not null AUTO_INCREMENT primary key,
	day_birth date,
	day_death date,
	country_birth varchar(255) not null default '',
	full_name varchar(255) not null default ''
);

DROP TABLE IF EXISTS Author2Shelf;
CREATE TABLE Author2Shelf(
	author_id int unsigned not null,
	shelf_id int unsigned not null,
	foreign key(author_id) REFERENCES Author(id),
	foreign key(shelf_id) REFERENCES Shelf(id)
);

DROP TABLE IF EXISTS Book;
CREATE TABLE Book(
	id int unsigned not null AUTO_INCREMENT primary key,
	author_id int unsigned not null,
	category_id int unsigned not null,
	shelf_id int unsigned not null,
	year smallint not null default 0,
	name varchar(255) not null default '',
	foreign key(author_id) REFERENCES Author(id),
	foreign key(category_id) REFERENCES Category(id),
	foreign key(shelf_id) REFERENCES Shelf(id)
);

DROP TABLE IF EXISTS LibraryCard;
CREATE TABLE LibraryCard(
	id int unsigned not null AUTO_INCREMENT primary key,
	full_name varchar(255) not null default '',
	day_birth date
);

DROP TABLE IF EXISTS Librarian;
CREATE TABLE Librarian(
	id int unsigned not null AUTO_INCREMENT primary key,
	work_start_day date,
	work_end_day date,
	fullname varchar(255) not null default ''
);

DROP TABLE IF EXISTS BookOut;
CREATE TABLE BookOut(
	book_id int unsigned not null,
	library_card_id int unsigned not null,
	librarian_id int unsigned not null,
	date_till date,
	foreign key(book_id) REFERENCES Book(id),
	foreign key(library_card_id) REFERENCES LibraryCard(id),
	foreign key(librarian_id) REFERENCES Librarian(id)
);

DROP TABLE IF EXISTS Event;
CREATE TABLE Event(
	id int unsigned not null AUTO_INCREMENT primary key,
	date_start date,
	organizer_id int unsigned not null,
	foreign key(organizer_id) REFERENCES Librarian(id),
	name varchar(255) not null default '',
	description mediumtext
);
