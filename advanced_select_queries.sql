SELECT name, COUNT (musician_id) FROM genres_musicians
	JOIN music_genres AS m ON m.id = genre_id
	GROUP BY name
	ORDER BY COUNT (musician_id) DESC;

SELECT COUNT (tracks.name) FROM tracks
	JOIN albums a ON a.id = album_id
	WHERE release_date BETWEEN 2019 and 2021;

SELECT a.name, AVG (duration) FROM tracks
	JOIN albums a ON a.id = album_id
	GROUP BY a.name
	ORDER BY AVG (duration) DESC;

SELECT DISTINCT musicians.name FROM musicians
  WHERE musicians.name NOT IN (
    SELECT DISTINCT musicians.name FROM musicians
    JOIN musicians_albums ON musicians.id = musicians_albums.musician_id
    JOIN albums ON albums.id = musicians_albums.album_id
    WHERE albums.release_date = 2020
    )
  ORDER BY musicians.name;

SELECT collections.name FROM tracks_collections
	JOIN collections ON collections.id = collection_id
	JOIN tracks ON tracks.id = track_id
	JOIN albums ON albums.id = album_id
	JOIN musicians_albums ON albums.id = musicians_albums.album_id
	JOIN musicians ON musicians.id = musician_id
	WHERE musicians.name ILIKE '%prodigy%';

SELECT albums.name FROM musicians_albums
	JOIN albums ON albums.id = album_id
	JOIN musicians ON musicians.id = musician_id
	JOIN genres_musicians ON musicians.id = genres_musicians.musician_id
	GROUP BY albums.name
	HAVING COUNT (genres_musicians.genre_id) > 1
	ORDER BY albums.name;

SELECT name FROM tracks
	LEFT JOIN tracks_collections ON track_id = tracks.id
	WHERE track_id IS NULL;

SELECT musicians.name FROM musicians
	JOIN musicians_albums ON musicians.id = musicians_albums.musician_id
	JOIN albums ON albums.id = musicians_albums.album_id
	JOIN tracks ON tracks.album_id = albums.id
	WHERE tracks.duration = (SELECT MIN (tracks.duration) FROM tracks)
	GROUP BY musicians.name;

SELECT albums.name FROM albums
	JOIN tracks ON album_id = albums.id
	GROUP BY albums.name
	HAVING (SELECT MIN (mycount)
		FROM (SELECT COUNT (tracks.album_id) AS mycount
		FROM tracks
		GROUP BY tracks.album_id) AS mycount2) = COUNT (tracks.album_id)
	ORDER BY albums.name;







