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

SELECT DISTINCT m.name FROM musicians_albums
JOIN musicians m ON m.id = musician_id
JOIN albums a ON a.id = album_id
WHERE release_date != 2020
ORDER BY m.name;

SELECT collections.name FROM tracks_collections
JOIN collections ON collections.id = collection_id
JOIN tracks ON tracks.id = track_id
JOIN albums ON albums.id = album_id
JOIN musicians_albums ON albums.id = musicians_albums.album_id
JOIN musicians ON musicians.id = musician_id
WHERE musicians.name ILIKE '%prodigy%';