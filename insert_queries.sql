INSERT INTO music_genres(name)
	VALUES('Grunge'),
	('Rock'),
	('Punk'),
	('Rap'),
	('Rock"N"Roll'),
	('Industrial Metal'),
	('Pop'),
	('Electronic Rock'),
	('Trash Metal'),
	('Punk Rock'),
	('Alternative Rock'),
	('Alternative Dance'),
	('Alternative Metal'),
	('Big Beat');

INSERT INTO musicians(name)
	VALUES('Nirvana'),
	('Fear Factory'),
	('Ramones'),
	('Eminem'),
	('����������� �������'),
	('The Offspring'),
	('The Prodigy'),
	('Marcy Playground'),
	('Rise Against'),
	('Sepultura'),
	('���');

INSERT INTO genres_musicians(genre_id, musician_id)
	VALUES(1, 1),
	(11, 1),
	(10, 1),
	(6, 2),
	(11, 3),
	(4, 4),
	(2, 5),
	(11, 6),
	(10, 6),
	(8, 7),
	(12, 7),
	(14, 7),
	(11, 8),
	(1, 8),
	(10, 9),
	(9, 10),
	(13, 10),
	(2, 11);

INSERT INTO albums(name, release_date)
	VALUES('Nevermind', 1991),
	('In Utero', 1993),
	('MTV Unplugged in New York', 1994),
	('Demanufacture', 1995),
	('Obsolete', 1998),
	('Aggression Continuum', 2021),
	('Rocket to Russia', 1977),
	('End of the Century', 1980),
	('The Slim Shady LP', 1999),
	('Kamikaze', 2018),
	('��� ���������� �����', 1988),
	('�����������', 1997),
	('Smash', 1994),
	('Americana', 1998),
	('Invaders Must Die', 2009),
	('The Fat of the Land', 1997),
	('Marcy Playground', 1997),
	('MP3', 2004),
	('Siren Song of the Counter Culture', 2004),
	('Nowhere Generation', 2021),
	('Roots', 1996),
	('SepulQuarta', 2021),
	('��� ��', 1995),
	('���� ����', 2018);

INSERT INTO tracks(name, duration, album_id)
	VALUES('Smells Like Teen Spirit', 5.01, 1),
	('Come as You Are', 3.39, 1),
	('Frances Farmer Will Have Her Ravenge on Seattle', 4.10, 2),
	('On a Plain', 3.45, 3),
	('Demanufacture', 4.14, 4),
	('Edgecrusher', 3.40, 5),
	('Disruptor', 3.45, 6),
	('I Don''t Care', 1.39, 7),
	('Rock''N''Roll HighSchool', 2.41, 8),
	('My Name is', 4.29, 9),
	('Not Alike', 4.48, 10),
	('��������� �� ���������', 2.32, 11),
	('��� �������', 4.51, 12),
	('Gotta Get Away', 3.52, 13),
	('Pretty Fly (For a White Guy)', 3.09, 14),
	('Omen', 3.36, 15),
	('Smack My Bitch Up', 5.43, 16),
	('Saint Joe on the School Bus', 3.20, 17),
	('Blood in Alphabet Soup', 2.20, 18),
	('Give it All', 2.50, 19),
	('Nowhere Generation', 3.52, 20),
	('Roots Bloody Roots', 3.32, 21),
	('Territory', 4.51, 22),
	('�������', 5.09, 23),
	('������-�������', 5.02, 24);

INSERT INTO collections(name, release_date)
	VALUES('Nirvana', 2002),
	('The Best of Fear Factory', 2006),
	('Ramones Mania', 1988),
	('Curtain Call: The Hits', 2005),
	('Greatest Hits', 2005),
	('Their Law: The Singles 1990-2005', 2005),
	('Rock Against Bush, Vol.1', 2004),
	('The Best of Sepultura', 2006);

INSERT INTO musicians_albums(musician_id, album_id)
	VALUES(1, 1),
	(1, 2),
	(1, 3),
	(2, 4),
	(2, 5),
	(2, 6),
	(3, 7),
	(3, 8),
	(4, 9),
	(4, 10),
	(5, 11),
	(5, 12),
	(6, 13),
	(6, 14),
	(7, 15),
	(7, 16),
	(8, 17),
	(8, 18),
	(9, 19),
	(9, 20),
	(10, 21),
	(10, 22),
	(11, 23),
	(11, 24);

INSERT INTO tracks_collections(track_id, collection_id)
	VALUES(1, 1),
	(5, 2),
	(9, 3),
	(10, 4),
	(15, 5),
	(17, 6),
	(20, 7),
	(23, 8);