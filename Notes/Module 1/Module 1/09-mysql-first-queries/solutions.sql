# 1. What are the different genres?
SELECT DISTINCT prime_genre FROM applestore;

# 2. Which is the genre with the most apps rated?
SELECT prime_genre, SUM(rating_count_tot) AS num_apps_rated FROM applestore GROUP BY prime_genre ORDER BY 2 DESC LIMIT 1;
 
# 3. Which is the genre with most apps?
SELECT prime_genre, COUNT(*) AS num_app FROM applestore GROUP BY 1 ORDER BY 2 DESC LIMIT 1;

# 4. Which is the one with least? 
SELECT prime_genre, COUNT(*) AS num_app FROM applestore GROUP BY 1 ORDER BY 2 LIMIT 1;

# 5. Find the top 10 apps most rated.
SELECT track_name, rating_count_tot FROM applestore ORDER BY 2 DESC LIMIT 10;

# 6. Find the top 10 apps best rated by users.
SELECT track_name, user_rating, user_rating_ver FROM applestore ORDER BY 2 DESC LIMIT 10;

# 7. Take a look at the data you retrieved in question 5. Give some insights.
/* extremely popular social media and games apps*/

# 8. Take a look at the data you retrieved in question 6. Give some insights.
/* hard to differentiate them when they are all rated at 5*/

# 9. Now compare the data from questions 5 and 6. What do you see?
/* different apps*/

# 10. How could you take the top 3 regarding both user ratings and number of votes?
SELECT track_name, user_rating, rating_count_tot FROM applestore ORDER BY 2 DESC, 3 DESC LIMIT 3;

# 11. Do people care about the price of an app? Do some queries, comment why are you doing them and the results you retrieve. What is your conclusion?
SELECT AVG(user_rating) FROM applestore WHERE price > 0;
SELECT AVG(user_rating) FROM applestore WHERE price = 0;