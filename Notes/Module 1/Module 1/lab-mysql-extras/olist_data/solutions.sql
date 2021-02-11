use olist;
# 1. From the order_items table, find the price of the highest priced order item and lowest price order item.
SELECT MAX(price), MIN(price) FROM order_items;

# 2. From the order_items table, what is range of the shipping_limit_date of the orders?
SELECT 
    CONCAT(MIN(shipping_limit_date),
            ' to ',
            MAX(shipping_limit_date)) AS range_of_date
FROM
    order_items;

# 3. From the customers table, find the 3 states with the greatest number of customers.
SELECT 
    customer_state
FROM
    customers
GROUP BY 1
ORDER BY COUNT(*) DESC
LIMIT 3;

# 4. From the customers table, within the state with the greatest number of customers, find the 3 cities with the greatest number of customers.
select customer_city from customers GROUP BY 1, where customers_state IN 
(SELECT 
    customer_state
FROM
    customers
GROUP BY 1
ORDER BY COUNT(*) DESC
LIMIT 3)
order by sum(*) desc limit 3;

# 5. From the closed_deals table, how many distinct business segments are there (not including null)?
select count(distinct business_segment) from closed_deals where business_segment is not null;

SELECT 
    business_segment
FROM
    closed_deals
GROUP BY 1
ORDER BY SUM(declared_monthly_revenue) DESC
LIMIT 3;

# 7. From the order_reviews table, find the total number of distinct review score values.
SELECT count(distinct review_score) FROM order_reviews;

# 8. In the order_reviews table, create a new column with a description that corresponds to each number category for each review score from 1 - 5.
select review_id, review_score,
(case when review_score='1' then 'shit' when review_score='2' then 'bad' when review_score='3' then 'alright' when review_score='4' then 'cool' when review_score='5' then 'great' else 'huh' end) description
FROM order_reviews;


# 9. From the order_reviews table, find the review score occurring most frequently and how many times it occurs.
select review_score, count(*) from order_reviews where review_score = (select review_score from order_reviews GROUP BY 1 ORDER BY count(*) desc limit 1);