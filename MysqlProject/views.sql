--представление книга/автор
create view BookAuthor as select Book.*, Author.full_name from Book join Author on (Book.author_id = Author.id);

--представление для библиотекаря и его рабочих дней
create view LibrarianSchedule as select Schedule.*, Librarian.fullname from Schedule join Librarian on (Schedule.librarian_id = Librarian.id);
