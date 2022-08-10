SELECT name, release_date FROM albums
	WHERE release_date = 2018;

SELECT name, duration FROM tracks
	WHERE duration = (SELECT MAX(duration) FROM tracks);

SELECT name FROM tracks
	WHERE duration > 3.3;

SELECT name FROM collections
	WHERE release_date BETWEEN 2018 AND 2020;

/* Так вышло, что музыка в моей БД не попадает под требуемый период, поэтому ниже я продублирую
такой же SELECT запрос, но с подходящими моей БД датами*/

SELECT name FROM collections
	WHERE release_date BETWEEN 2003 AND 2005;

SELECT name FROM musicians
	WHERE name NOT LIKE '% %';

SELECT name FROM tracks
	WHERE name ILIKE '%my%' OR name ILIKE '%мой%';