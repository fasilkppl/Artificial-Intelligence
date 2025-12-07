SELECT * FROM movies where industry = "Bollywood";
SELECT DISTINCT industry from movies;
SELECT * FROM movies where title LIKE 'THOR%';
SELECT * FROM movies where title LIKE '%America%';
SELECT * FROM movies where studio = "";
select * from movies where imdb_rating >= 9;
select * from movies where imdb_rating >=6 and imdb_rating <= 8;
select * from movies where imdb_rating between 6 and 8;
select * from movies where release_year = 2022 or release_year = 2019;
select * from movies where release_year in (2018,2019,2022);
select * from movies where studio in ("Marvel Studios", "Zee Studios");

select * 
from movies
where imdb_rating
is null;

select * 
from movies
where imdb_rating
is not null;

select * 
from movies
where industry = "Hollywood" 
order by imdb_rating ASC;


select * 
from movies
where industry = "Hollywood" 
order by imdb_rating DESC;

select * 
from movies
where industry = "Hollywood" 
order by imdb_rating DESC;

select * 
from movies
where industry = "Hollywood" 
order by imdb_rating DESC limit 5; -- GIVES FIRST FIVE

select * 
from movies
where industry = "Hollywood" 
order by imdb_rating DESC limit 5 offset 2; -- starts from 2nd index, avoids 0 and 1 index from 2nd index up to 5 movies it will give.


select count(*) from movies -- count() is a function
where industry = "bollywood"; -- return count of bollywood movies

select max(imdb_rating) from movies;

select avg(imdb_rating) from movies where studio = "Marvel Studios";

select round(avg(imdb_rating), 2) from movies 
where studio = "Marvel Studios"; -- round to 2 decimals

select min(imdb_rating) as min_rating,
max(imdb_rating) as max_rating,
round(avg(imdb_rating), 2) as average_rating
from movies where studio = "Marvel Studios";


select industry, count(*) from movies group by industry;

select studio, count(*) as cnt
from movies 
group by studio
order by cnt desc;

select industry, count(*) as cnt, avg(imdb_rating) as avg_rating
from movies 
group by industry
order by cnt, avg_rating desc;

select studio, count(studio) as cnt, 
round(avg(imdb_rating), 1) as avg_rating
from movies 
where studio != ""
group by studio
order by cnt, avg_rating desc;


select release_year, count(*) as cnt
from movies 
group by release_year
having cnt >= 2 -- to filter groups we use having, to filter single rows we use where
order by cnt desc;
#SQL chronological execution order:
#FROM → WHERE → GROUP BY → AGGREGATE FUNCTIONS (like COUNT, SUM, AVG) → HAVING → SELECT → ORDER BY 




select release_year, count(*) as cnt
from movies 
where studio = "Marvel Studios" 
group by release_year
order by cnt desc;

















