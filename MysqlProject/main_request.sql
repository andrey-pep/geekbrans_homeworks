--Данные по событию и его организатору
select * from Event left join Librarian on (Event.organizer_id = Librarian.id) where Event.id = 1;

--Найти полки по имени автора
select position from Shelf where id in (select shelf_id from Book where author_id in (select id from Author where full_name = "Fidel Bruen"));

--Найти полки по названию книги
select position from Shelf where id in (select shelf_id from Book where name = "laboriosam");
--Выбрать книги на руках пользователей
select * from Book where id in (select book_id from BookOut);

--Сколько книг у каждого должника, основная информация о нем + сумма штрафа
select t1.*, t2.cnt, t3.amount from LibraryCard as t1 join (select library_card_id as id, count(*) as cnt from BookOut group by library_card_id) t2 on (t1.id = t2.id) left join Dept as t3 on (t2.id = t3.library_card_id);
