select *
from titleauthor;

select *
from authors;

select *
from titles;

select count(distinct title_id)
from titleauthor;


#Challenge 1 - Who Have Published What At Where?
SELECT 
    authors.au_id AS 'AUTHOR ID',
    authors.au_lname AS 'LAST NAME',
    authors.au_fname AS 'FIRST NAME',
    titles.title AS 'TITLE',
    publishers.pub_name AS 'PUBLISHERS'
FROM
    publications.authors
    inner JOIN titleauthor ON authors.au_id = titleauthor.au_id
        inner JOIN
    titles ON titleauthor.title_id = titles.title_id
        inner JOIN
    publishers ON publishers.pub_id = titles.pub_id
    order by 2, 3, 1;
 
 
#Challenge 2 - Who Have Published How Many At Where?
SELECT 
    authors.au_id AS 'AUTHOR ID',
    authors.au_lname AS 'LAST NAME',
    authors.au_fname AS 'FIRST NAME',
    publishers.pub_name AS 'PUBLISHERS',
    count(*) as 'TITLE COUNT'
FROM
    publications.authors
        INNER JOIN
    titleauthor ON authors.au_id = titleauthor.au_id
        INNER JOIN
    titles ON titleauthor.title_id = titles.title_id
        INNER JOIN
    publishers ON publishers.pub_id = titles.pub_id
group by 1, 2, 3, 4;
    
    
#Challenge 3 - Best Selling Authors
SELECT 
    authors.au_id AS 'AUTHOR ID',
    authors.au_lname AS 'LAST NAME',
    authors.au_fname AS 'FIRST NAME',
    sum(qty) as 'TOTAL'
FROM
    publications.authors
        INNER JOIN
    titleauthor ON authors.au_id = titleauthor.au_id
        INNER JOIN
    titles ON titleauthor.title_id = titles.title_id
        INNER JOIN
    publishers ON publishers.pub_id = titles.pub_id
		inner join
	sales on titles.title_id = sales.title_id
group by 1, 2, 3
order by 4 desc
limit 3;


#Challenge 4 - Best Selling Authors Ranking
SELECT 
    authors.au_id AS 'AUTHOR ID',
    authors.au_lname AS 'LAST NAME',
    authors.au_fname AS 'FIRST NAME',
    COALESCE(sum(qty), 0) as 'TOTAL'
FROM
    publications.authors
        left JOIN
    titleauthor ON authors.au_id = titleauthor.au_id
        left JOIN
    titles ON titleauthor.title_id = titles.title_id
        left JOIN
	sales on titles.title_id = sales.title_id
group by 1, 2, 3
order by 4 desc
;


select *
from authors;
