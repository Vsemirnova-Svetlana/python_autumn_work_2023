create table book2(book_id int, book_title text, book_author text, publisher_id int);
insert into book2 values
(1, 'Королева Марго', 'Дюма А.', 164),
(2, 'Всадник без головы', 'Рид М.',702),
(3, 'Маятник Фуко', 'Эко У.', 403),
(4, 'Лунный камень', 'Коллинз У.',256),
(5, 'Карма','Садхгуру', 700)
select * from book2 order by book_title
select * from book2 order by book_id
select publisher_id,book_author, book_title from book2
select * from book2 where book_title like 'К%'
select book_author,book_title from book2