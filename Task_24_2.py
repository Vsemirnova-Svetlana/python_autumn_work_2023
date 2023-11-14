# create view min_count1 as
# (select book_author,sum(amount) as количество from book6 group by book_author)
# select book_author, sum(amount) from
# author1 inner join book6
# on author1.author_id=book6.author_id
# group by book_author
# having sum(amount) =
# (select min(количество) as min_sum_amount from
# min_count1);