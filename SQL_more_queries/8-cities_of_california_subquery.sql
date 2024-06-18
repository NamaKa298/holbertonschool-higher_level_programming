-- ============================================================================================
-- script that lists all the cities of California that can be found in the database hbtn_0d_usa
-- ============================================================================================
SET @cities_id := (SELECT id FROM states WHERE name = 'California');
SELECT id, name FROM cities WHERE cities_id = cities.id ORDER BY cities.id ASC;