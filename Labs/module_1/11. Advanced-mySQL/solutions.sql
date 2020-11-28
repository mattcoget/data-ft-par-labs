# Challenge 1 - Most Profiting Authors
select *
from sales;

select *
from roysched;

select * 
from authors;

select count(*)
from authors;

select * 
from titles;

select *
from titleauthor;

select *
from sales;

#Step1
SELECT 
    titleauthor.title_id AS 'TITLE ID',
    titleauthor.au_id AS 'AUTHOR ID',
    COALESCE(ROUND(titles.advance * titleauthor.royaltyper / 100, 2), 0) AS 'ADVANCE',
    COALESCE(ROUND((titles.price * sales.qty * titles.royalty / 100) * (titleauthor.royaltyper / 100), 2), 0) AS 'ROYALTIES'
FROM
    titleauthor
        LEFT JOIN
    titles ON titleauthor.title_id = titles.title_id
        LEFT JOIN
    sales ON titles.title_id = sales.title_id
;

#Step2
SELECT 
    titleauthor.title_id AS 'TITLE ID',
    titleauthor.au_id AS 'AUTHOR ID',
    SUM(COALESCE(ROUND(titles.price * sales.qty * (titles.royalty / 100) * (titleauthor.royaltyper / 100), 2), 0)) AS 'ROYALTIES'
FROM
    titleauthor
        LEFT JOIN
    titles ON titleauthor.title_id = titles.title_id
        LEFT JOIN
    sales ON titles.title_id = sales.title_id
GROUP BY 1 , 2
;

#Step3 work in progress
SELECT au_id AS 'AUTHOR ID', sum(ADVANCE + ROYALTIES) as 'PROFITS'
from (
select titleauthor.title_id , titleauthor.au_id, 
	COALESCE(ROUND(titles.advance * titleauthor.royaltyper / 100, 2), 0) AS 'ADVANCE',
 SUM(COALESCE(ROUND(titles.price * sales.qty * (titles.royalty / 100) * (titleauthor.royaltyper / 100), 2), 0)) AS 'ROYALTIES'
from titleauthor
        LEFT JOIN
    titles ON titleauthor.title_id = titles.title_id
        LEFT JOIN
    sales ON titles.title_id = sales.title_id
    group by 2, 1) as table_royalties
group by 1
order by 2 DESC
limit 3;



#Challenge 2 - Alternative Solution
#create a temporary table 

Create temporary table_advance_and_royalties_per_author 
select titleauthor.title_id , titleauthor.au_id, 
	COALESCE(ROUND(titles.advance * titleauthor.royaltyper / 100, 2), 0) AS 'ADVANCE',
 SUM(COALESCE(ROUND(titles.price * sales.qty * (titles.royalty / 100) * (titleauthor.royaltyper / 100), 2), 0)) AS 'ROYALTIES'
from titleauthor
        LEFT JOIN
    titles ON titleauthor.title_id = titles.title_id
        LEFT JOIN
    sales ON titles.title_id = sales.title_id
    group by 2, 1;
