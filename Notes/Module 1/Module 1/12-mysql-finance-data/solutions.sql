# Challenge 1

SELECT
		district_id,
        COUNT(account_id) as ac_freq

FROM finance.account

GROUP BY district_id

ORDER BY 2 DESC

LIMIT 5;

# Challenge 2

SELECT
		account_id,
        count(distinct amount) as diff,
        group_concat(distinct bank_to) as bank_to,
        group_concat(amount) as rent
FROM finance.order

where k_symbol = 'SIPO'

GROUP BY account_id

HAVING diff > 1;

# Challenge 3

SELECT 
		tr.account_id,
        ac.district_id,
		SUM(tr.amount) as amount
        
 FROM finance.trans as tr
 
 INNER JOIN finance.account as ac ON tr.account_id = ac.account_id

where k_symbol = 'UVER'

GROUP BY
		tr.account_id,
        ac.district_id

ORDER BY amount DESC;

# Challenge 4

SELECT 

        ac.district_id,
		SUM(tr.amount) as amount
        
 FROM finance.trans as tr
 
 INNER JOIN finance.account as ac ON tr.account_id = ac.account_id

where k_symbol = 'UVER'

GROUP BY

        ac.district_id

ORDER BY amount DESC;

# Challenge 5

create table xxx
select l.account_id, district_id, amount
from account a
inner join loan l on a.account_id=l.account_id;

select district_id, amount
from (
SELECT x.district_id, x.amount, count(y.amount) as ranking
from xxx x, xxx y
where x.district_id=y.district_id and x.amount<y.amount
group by x.district_id, x.amount) as ranked_table
where exists(
	select x1.district_id, ceil(count(x1.amount)/2) ranking
	from xxx x1
	group by district_id
    having ranked_table.district_id = x1.district_id and ranked_table.ranking=ranking)
order by 2 desc
limit 5;