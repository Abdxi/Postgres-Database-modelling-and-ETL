"""
In this module we write all the nessary sql queties needed in the project.

module converts the most used queries into variables o ease queries usage.

"""

# create tables queries


#query of creating the fact table songplays
create_songplays = ("""
CREATE TABLE IF NOT EXISTS songplays
    (songplay_id SERIAL PRIMARY KEY, 
    start_time bigint NOT NULL, 
    user_id int NOT NULL, 
    level varchar,
    song_id varchar, 
    artist_id varchar, 
    session_id int, 
    location text, 
    user_agent text);

""")

create_users = ("""

CREATE TABLE IF NOT EXISTS users 
    (user_id int PRIMARY KEY, 
    first_name varchar, 
    last_name varchar, 
    gender varchar(1), 
    level varchar);
""")

create_songs = ("""

CREATE TABLE IF NOT EXISTS songs 
    (song_id varchar PRIMARY KEY, 
    title text, 
    artist_id varchar, 
    year int, 
    duration numeric);
""")

create_artist = ("""

CREATE TABLE IF NOT EXISTS artist

(artist_id varchar PRIMARY KEY, 
    name varchar, 
    location text, 
    latitude decimal, 
    longitude decimal);

""")

create_time = (""" 
CREATE TABLE IF NOT EXISTS time 
    (start_time timestamp PRIMARY KEY, 
    hour int, 
    day int, 
    week int, 
    month int, 
    year int, 
    weekday varchar);
""")


# drop queries for each table


drop_songplays = "DROP TABLE IF EXISTS songplays"
drop_songs = "DROP TABLE IF EXISTS songs"
drop_artist = "DROP TABLE IF EXISTS artist"
drop_users = "DROP TABLE IF EXISTS users"
drop_time = "DROP TABLE IF EXISTS time"



# group create tables in one list

create_queries = [create_songplays, create_users, create_songs, create_artist, create_time]

# group drop table in one list

drop_queries = [drop_songplays, drop_users, drop_songs, drop_artist, drop_time]



# insert data into each table

insert_songplays = ("""

INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)

""")


insert_users = ("""
INSERT INTO users(user_id, first_name, last_name, gender, level) 
VALUES (%s, %s, %s, %s, %s) 
ON CONFLICT (user_id) 
    DO UPDATE
    SET level = EXCLUDED.level


""")

insert_songs = ("""

INSERT INTO songs(song_id, title, artist_id, year, duration) 
VALUES (%s, %s, %s, %s, %s) 
ON CONFLICT (song_id) 
    DO NOTHING

""")

insert_artist =("""
INSERT INTO artist(artist_id, name, location, latitude, longitude) 
VALUES (%s, %s, %s, %s, %s) 
ON CONFLICT (artist_id) 
    DO NOTHING


""")

insert_time = ("""
INSERT INTO time(start_time, hour, day, week, month, year, weekday) 
VALUES (%s, %s, %s, %s, %s, %s, %s) 
ON CONFLICT (start_time) 
    DO NOTHING 


""")


select_ids = ("""

SELECT artist.artist_id, songs.song_id

FROM songs

JOIN artist 

ON songs.artist_id = artist.artist_id

WHERE songs.title = %s AND artist.name = %s  AND songs.duration = %s


 """)




