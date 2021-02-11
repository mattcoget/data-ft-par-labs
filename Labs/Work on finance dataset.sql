select * from account;
select * from card;
select * from client;
select * from district;
select * from loan;
select * from finance.order;
select * from trans;


# Count the number of clients per gender
SELECT 
    case type when 'OWNER' then 'MEN' else 'WOMEN' end as 'GENDER',
    COUNT(client_id) as 'COUNT'
FROM
    disp
GROUP BY type;

# Are there any accounts that have more than 2 linked clients?
select account_id, count(client_id) as 'nb_of_clients' from disp
group by account_id
order by 2 desc;

# What is the average transaction amount for each region?
select * from district;

select account.district_id, sum(trans.amount) from trans
left join account on account.account_id = trans.account_id
left join district on district.A1 = account.district_id
group by 1
order by 1 asc;


SELECT 
    distinct district.A3 AS 'REGION',
    ROUND(AVG(trans.amount), 2) AS 'AVG TRANS AMOUNT'
FROM
    trans
        right JOIN
    account ON account.account_id = trans.account_id
        right JOIN
    district ON account.district_id = district.A1
GROUP BY account.account_id , district_id , 1
ORDER BY 2 DESC
LIMIT 10;

# From which region do most of the clients that are account owners come from, 
# that either have finished loan contracts that haven't been paid, or have running contracts 
# but are in debt? Show the top 10 regions including the number of client that are owners.
