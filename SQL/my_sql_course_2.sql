select *, YEAR(CURDATE()) - birth_year as age 
FROM actors;

select * from financials;

select *, (revenue - budget) as profit 
from financials;


select *,
#IF(condition, what to do when condition is true, what to do when condition is false)
IF (currency='USD', revenue*88.63, revenue) 
as revenue_inr
from financials;

select distinct unit
from financials;

select *,
case
	when unit = 'thousand' then revenue/1000
	when unit = 'billions' then revenue*1000
	when unit = 'millions' then revenue
end as revenue_in_millions
from financials;


select * from financials;
select * from movies;

#joining 2 tables using common id on both tables( default is inner join)
select movies.movie_id, title, budget, revenue, currency, unit
from movies # table 1
join financials #table 2
on movies.movie_id = financials.movie_id;

#to make the above query shorter
select m.movie_id, title, budget, revenue, currency, unit
from movies m # table 1
inner join financials f #table 2
on m.movie_id = f.movie_id;

select m.movie_id, title, budget, revenue, currency, unit
from movies m # table 1
left join financials f #table 2
on m.movie_id = f.movie_id;

#right join
select f.movie_id, title, budget, revenue, currency, unit
from movies m # table 1
right join financials f #table 2
on m.movie_id = f.movie_id;


#full join 
select m.movie_id, title, budget, revenue, currency, unit 
from movies m # table 1
left join financials f 
on m.movie_id = f.movie_id

union

select f.movie_id, title, budget, revenue, currency, unit 
from movies m
right join financials f 
on m.movie_id = f.movie_id;


#if both tables have same common column names ,this case movie_id

select movie_id, title, budget, revenue, currency, unit 
from movies
left join financials
using(movie_id); # we can also merge two tables using 2 same columns or 3 same coulmns etc.. using(movie_id, name of second same column)
#if two colums have same name we can use using function.



