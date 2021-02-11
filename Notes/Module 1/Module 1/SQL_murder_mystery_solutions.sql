/*Identify the witness requires you to find out details about how to locate them*/
SELECT * FROM crime_scene_report 
WHERE type = 'murder' AND city = 'SQL City' AND date = '20180115';

/*the above gave me information on the 2 witness,
the first witness lives at the last house on "Northwestern Dr"
the second witness, named Annabel, lives somewhere on "Franklin Ave".*/
# Identify the first witness
SELECT * FROM person WHERE address_street_name = 'Northwestern Dr' ORDER BY address_number DESC LIMIT 1;

# Identify the second witness
SELECT * FROM person WHERE address_street_name = 'Franklin Ave' AND name LIKE 'Annabel%';

# Interview transcripts for our two subjects
SELECT person.name, transcript FROM interview
JOIN person ON interview.person_id = person.id
WHERE person_id=(SELECT id FROM person WHERE address_street_name = 'Northwestern Dr' ORDER BY address_number DESC LIMIT 1)
OR person_id=(SELECT id FROM person WHERE address_street_name = 'Franklin Ave' AND name LIKE 'Annabel%');

/*Morty Schapiro: He had a "Get Fit Now Gym" bag
The membership number on the bag started with "48Z" 
Only gold members have those bags
The man got into a car with a plate that included "H42W"
Annabel Miller: I recognized the killer from my gym when I was working out last week on January the 9th.*/

# Find the murderer!
SELECT person.name FROM drivers_license 
JOIN person ON drivers_license.id = person.license_id
JOIN get_fit_now_member ON person.id = get_fit_now_member.person_id
JOIN get_fit_now_check_in ON get_fit_now_member.id = get_fit_now_check_in.membership_id
WHERE plate_number LIKE '%H42W%'
AND get_fit_now_member.id LIKE '48Z%'
AND check_in_date = '20180109';

# The REAL murderer!
/*Let's see what the murderer has to say first... */
SELECT person.name, transcript FROM drivers_license 
JOIN person ON drivers_license.id = person.license_id
JOIN get_fit_now_member ON person.id = get_fit_now_member.person_id
JOIN get_fit_now_check_in ON get_fit_now_member.id = get_fit_now_check_in.membership_id
JOIN interview ON person.id = interview.person_id
WHERE plate_number LIKE '%H42W%'
AND get_fit_now_member.id LIKE '48Z%'
AND check_in_date = '20180109'
;

/*I was hired by a woman with a lot of money. 
I don't know her name but I know she's around 5'5" (65") or 5'7" (67"). 
She has red hair and she drives a Tesla Model S. 
I know that she attended the SQL Symphony Concert 3 times in December 2017.*/

# Drum rolls
SELECT person.name FROM drivers_license
JOIN person ON drivers_license.id = person.license_id
JOIN facebook_event_checkin ON person.id = facebook_event_checkin.person_id
WHERE hair_color = 'red'
AND car_make = 'Tesla'
AND car_model = 'Model S'
AND height BETWEEN 65 AND 67
AND event_name = 'SQL Symphony Concert'
AND date LIKE '201712%'
GROUP BY person.id
HAVING COUNT(*) >2
;