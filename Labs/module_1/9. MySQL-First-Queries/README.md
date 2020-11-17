![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | My first queries

Please, connect to the Data Bootcamp Google Database using the credentials provided in class. Choose the database called *appleStore*. Use the *data* table to query the data about Apple Store Apps and answer the following questions: 

**1. What are the different genres?**
23 genres : 
Games, Productivity, Weather, Shopping, Reference, Finance, Music, Utilities, Travel, Social Networking, Sports, Business, Health & Fitness, Entertainment, Photo & Video, Navigation, Education, Lifestyle, Food & Drink, News, Book, Medical, Catalogs

**2. Which is the genre with the most apps rated?**
Games with 3,400 apps rated.

**3. Which is the genre with most apps?**
Game with 3,862 apps

**4. Which is the one with least?**
Catalogs with 10 apps

**5. Find the top 10 apps most rated.**
1. Facebook	2974676
2. Instagram	2161558
3. Clash of Clans	2130805
4. Temple Run	1724546
5. Pandora - Music & Radio	1126879
6. Pinterest	1061624
7. Bible	985920
8. Candy Crush Saga	961794
9. Spotify Music	878563
10. Angry Birds	824451

**6. Find the top 10 apps best rated by users.**
*Problem : there is more than 10 apps rated 5, so it can be a mistake.*
King of Dragon Pass	5
TurboScanã¢ Pro - document & receipt scanner: scan multiple pages and photos to PDF	5
Plants vs. Zombies	5
Learn to Speak Spanish Fast With MosaLingua	5
Plants vs. Zombies HD	5
The Photographer's Ephemeris	5
ÐÈSudoku +	5
Flashlight Òã	5
Infinity Blade	5

**7. Take a look at the data you retrieved in question 5. Give some insights.**
The genres of the apps are :
1. Games (4 apps)
2. Social Networking (2 apps) +  Instagram (which genre is Photo & Video)
3. Music (2 apps)
4. Reference (1 app)

All the apps are free
User ratings are between 3.5 to 4.5

The users rate the apps because they are the most installed. 
Bad rates because haters gonna hate.

**8. Take a look at the data you retrieved in question 6. Give some insights.**
The genres of the apps are :
1. Games (6 apps)
2. Business (1 app) + Education (1 app) + Photo & Video (1 app) + Utilities (1 app)
The number of ratings varies a lot between 426,463 and 9 votes.
Half a million scored 5 for the app: probably a fraud

**9. Now compare the data from questions 5 and 6. What do you see?**
All top 10 most rated apps are free, but only one in top 10 best rated.
4 of the most rated are game, and 6 for the best rated.
There is also 3 apps in the best rated which have less than 1000 ratings, so it can be the app company employees' that have done the most of the rating.

**10. How could you take the top 3 regarding both user ratings and number of votes?**


**11. Do people care about the price of an app?** Do some queries, comment why are you doing them and the results you retrieve. What is your conclusion?
Query 1 : select count(*) from Apps where price = 0; & select count(*) from Apps;
Query 2 : select * from Apps order by price limit 10.

On the 7,197 apps, 4,056 are free (56.36%)


There are 2 apps costing more than 200.00$! Their genre is Education. 
The genres of the most expensives are Education, Productivity, Navigation and Business.
Generally the number of votes for the expensive apps is low with ratings between 3.5 and 4.5.



All top 10 most rated apps are free, but only one in top 10 best rated.


## Deliverables 
You need to submit a `.sql` file that includes the queries used to answer the questions above, as well as an `.md` file including your answers. 
