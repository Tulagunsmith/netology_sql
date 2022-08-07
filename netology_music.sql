CREATE TABLE IF NOT EXISTS music_genres (
	id SERIAL PRIMARY KEY, 
	name VARCHAR(60) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS musicians (
	id SERIAL PRIMARY KEY, 
	name VARCHAR(60) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS genres_musicians (
	id SERIAL PRIMARY KEY, 
	genre_id INTEGER NOT NULL REFERENCES music_genres(id),
	musician_id INTEGER NOT NULL REFERENCES musicians(id)
);

CREATE TABLE IF NOT EXISTS albums (
	id SERIAL PRIMARY KEY, 
	name VARCHAR(60) NOT NULL,
	release_date INTEGER CHECK(release_date > 1930 and release_date < 2050)
);

CREATE TABLE IF NOT EXISTS musicians_albums (
	id SERIAL PRIMARY KEY, 
	album_id INTEGER NOT NULL REFERENCES albums(id),
	musician_id INTEGER NOT NULL REFERENCES musicians(id)
);

CREATE TABLE IF NOT EXISTS tracks (
	id SERIAL PRIMARY KEY, 
	name VARCHAR(60) NOT NULL,
	duration NUMERIC NOT NULL CHECK(duration > 0 and duration < 10),
	album_id INTEGER NOT NULL REFERENCES albums(id)
);

CREATE TABLE IF NOT EXISTS collections (
	id SERIAL PRIMARY KEY, 
	name VARCHAR(60) NOT NULL,
	release_date INTEGER CHECK(release_date > 1930 and release_date < 2050)
);

CREATE TABLE IF NOT EXISTS tracks_collections (
	id SERIAL PRIMARY KEY, 
	track_id INTEGER NOT NULL REFERENCES tracks(id),
	collection_id INTEGER NOT NULL REFERENCES collections(id)
);