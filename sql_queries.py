# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS fact_song_play_trn"
user_table_drop = "DROP TABLE IF EXISTS dim_users"
song_table_drop = "DROP TABLE IF EXISTS dim_songs"
artist_table_drop = "DROP TABLE IF EXISTS dim_artists"
time_table_drop = "DROP TABLE IF EXISTS dim_time"

# CREATE TABLES

songplay_table_create = ("CREATE TABLE IF NOT EXISTS fact_song_play_trn (songplay_id SERIAL PRIMARY KEY, start_time TIMESTAMP, user_id varchar, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar)")

user_table_create = ("CREATE TABLE IF NOT EXISTS dim_users (user_id varchar, first_name varchar, last_name varchar, gender varchar, level varchar)")

song_table_create = ("CREATE TABLE IF NOT EXISTS dim_songs(song_id varchar, title varchar, artist_id varchar, year int, duration numeric)")

artist_table_create = ("CREATE TABLE IF NOT EXISTS dim_artists (artist_id varchar, name varchar, location varchar, latitude numeric, longitude numeric)")

time_table_create = ("CREATE TABLE IF NOT EXISTS dim_time (start_time TIMESTAMP, hour int, day int, week int, month int, year int, weekday varchar)")

# INSERT RECORDS

songplay_table_insert = ("INSERT INTO fact_song_play_trn (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s,%s,%s,%s,%s)")

user_table_insert = ("INSERT INTO dim_users(user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)")

song_table_insert = ("INSERT INTO dim_songs(song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)")

artist_table_insert = ("INSERT INTO dim_artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s)")


time_table_insert = ("INSERT INTO dim_time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)")

# To FIND SONGS


song_select = ("SELECT songs.song_id, songs.artist_id FROM dim_songs songs \
                LEFT JOIN dim_artists artists ON (songs.artist_id = artists.artist_id) \
                WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s ")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]