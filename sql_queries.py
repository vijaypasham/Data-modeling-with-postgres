#DROP DATABASE

database_drop="DROP DATABASE IF EXISTS sparkifydb"

#CREATE DATABASE

database_create="CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0"

# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays
( 
songplay_id serial PRIMARY KEY, 
start_time timestamp NOT NULL, 
user_id int, 
level varchar(255) NOT NULL, 
song_id varchar(255), 
artist_id varchar(255), 
session_id int NOT NULL, 
location varchar(255), 
user_agent varchar(255)
);
""")

user_table_create = ("""

CREATE TABLE IF NOT EXISTS users
( 
user_id int PRIMARY KEY, 
first_name varchar(255) NOT NULL, 
last_name varchar(255), 
gender char(1), 
level varchar(255) NOT NULL
);
""")

song_table_create = ("""

CREATE TABLE IF NOT EXISTS songs
( 
song_id varchar(255) PRIMARY KEY, 
title varchar(255) NOT NULL, 
artist_id varchar(255) NOT NULL, 
year int NOT NULL, 
duration numeric NOT NULL
);

""")

artist_table_create = ("""

CREATE TABLE IF NOT EXISTS artists
( 
artist_id varchar(255) PRIMARY KEY, 
name varchar(255) NOT NULL, 
location varchar(255), 
lattitude numeric, 
longitude varchar(255)
);

""")

time_table_create = ("""

CREATE TABLE IF NOT EXISTS time
( 
start_time timestamp PRIMARY KEY, 
hour int NOT NULL, 
day int NOT NULL,  
week int NOT NULL,  
month int NOT NULL, 
year int NOT NULL, 
weekday varchar(255) NOT NULL
);

""")

# INSERT RECORDS

songplay_table_insert = ("""

INSERT INTO songplays (songplay_id,start_time,user_id,level,song_id,artist_id,session_id,location,user_agent)
Values
(%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING
""")

user_table_insert = ("""

INSERT INTO users (user_id,first_name,last_name,gender,level)
Values
(%s,%s,%s,%s,%s) ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert = ("""

INSERT INTO songs (song_id,title,artist_id,year,duration)
Values
(%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""

INSERT INTO artists (artist_id,name,location,lattitude,longitude)
Values
(%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING
""")


time_table_insert = ("""

INSERT INTO time (start_time,hour,day,week,month,year,weekday)
Values
(%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""

SELECT S.song_id, S.artist_id 
FROM songs S LEFT JOIN artists A ON (S.artist_id = A.artist_id)
WHERE S.title = %s
AND A.name = %s
AND S.duration = %s

""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]