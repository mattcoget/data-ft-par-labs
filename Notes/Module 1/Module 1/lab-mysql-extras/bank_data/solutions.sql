USE finance;

SELECT client_id FROM client WHERE district_id=1 ORDER BY client_id LIMIT 5;

SELECT client_id FROM client WHERE district_id=72 ORDER BY client_id DESC LIMIT 1;

SELECT amount FROM loan ORDER BY amount LIMIT 3;

SELECT DISTINCT status FROM loan ORDER BY status;

SELECT loan_id FROM loan ORDER BY payments DESC LIMIT 1;

SELECT account_id, amount FROM loan ORDER BY account_id LIMIT 5;

SELECT account_id FROM loan WHERE duration=60 ORDER BY amount LIMIT 5;

SELECT DISTINCT k_symbol FROM finance.order;

SELECT order_id FROM finance.order WHERE account_id=34;

SELECT DISTINCT account_id FROM finance.order WHERE order_id BETWEEN 29540 AND 29560;

SELECT amount FROM finance.order WHERE account_to=30067122;

SELECT trans_id, date, type, amount FROM trans WHERE account_id=793 ORDER BY date DESC LIMIT 10;

SELECT district_id, COUNT(district_id) FROM client GROUP BY district_id HAVING district_id < 10 ORDER BY district_id ;

SELECT type, COUNT(type) FROM card GROUP BY type ORDER BY COUNT(type) DESC;

SELECT account_id, SUM(amount) FROM loan GROUP BY account_id ORDER BY SUM(amount) DESC LIMIT 10;

SELECT date, COUNT(loan_id) FROM loan GROUP BY date HAVING date < 930907 ORDER BY date DESC;

SELECT date, duration, COUNT(loan_id) FROM loan GROUP BY date, duration HAVING date LIKE "9712%" ORDER BY date, duration;

SELECT account_id, type, SUM(amount) AS total_amount FROM                                    trans WHERE account_id=396 GROUP BY type ORDER BY type;

SELECT account_id, 
CASE type
WHEN "VYDAJ" THEN "Outgoing" 
WHEN "PRIJEM" THEN "Incoming"
END,
SUM(amount) AS total_amount FROM trans WHERE account_id=396 GROUP BY type ORDER BY type;


select account_id,
(case 
when type='PRIJEM' then 'Incoming' 
when type='VYDAJ' then 'Outgoing'
else 'Blah' 
end) type, 
SUM(amount) AS total_amount 
FROM trans WHERE account_id=396 GROUP BY type ORDER BY type;

SELECT account_id, incoming, outgoing, incoming-outgoing AS difference FROM
(SELECT i.account_id, incoming, SUM(amount) AS outgoing FROM trans
JOIN
(SELECT account_id, SUM(amount) AS incoming FROM trans WHERE account_id=396 GROUP BY type HAVING type="PRIJEM") i
ON trans.account_id= i.account_id
WHERE i.account_id=396 GROUP BY type HAVING type="VYDAJ") AS summary;



SELECT account_id, incoming-outgoing AS difference FROM
(SELECT i.account_id, incoming, SUM(amount) AS outgoing FROM trans
JOIN
(SELECT account_id, SUM(amount) AS incoming FROM trans WHERE account_id=396 GROUP BY type HAVING type="PRIJEM") i
ON trans.account_id= i.account_id
GROUP BY type HAVING type="VYDAJ") AS summary
ORDER BY difference DESC LIMIT 10;

select account_id, 
round(sum(if(type="PRIJEM", amount,0)),2) AS "Incoming", 
round(sum(if(type="VYDAJ", amount,0)),2) AS "Outgoing", 
round(sum(if(type="PRIJEM", amount,-amount)),2) AS "Difference"
from trans
where account_id=396
group by account_id;

select account_id, 
round(sum(if(type="PRIJEM", amount,0)),2) AS "Incoming", 
round(sum(if(type="VYDAJ", amount,0)),2) AS "Outgoing", 
round(sum(if(type="PRIJEM", amount,-amount)),2) AS "Difference"
from trans
group by account_id
order by difference desc limit 10;