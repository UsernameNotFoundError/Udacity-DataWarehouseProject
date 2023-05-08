# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create= ("""
        CREATE TABLE IF NOT EXISTS staging_events (
            artist VARCHAR(255),
            auth VARCHAR(50),
            firstName VARCHAR(50),
            gender CHAR(1),
            itemInSession INT,
            lastName VARCHAR(50),
            length FLOAT,
            level VARCHAR(50),
            location VARCHAR(255),
            method VARCHAR(25),
            page VARCHAR(35),
            registration BIGINT,
            sessionId INT,
            song VARCHAR(255),
            status INT,
            ts BIGINT,
            userAgent VARCHAR(255),
            userId INT
        )
        """
)

staging_songs_table_create = ("""
        CREATE TABLE IF NOT EXISTS staging_songs (
            num_songs INT,
            artist_id VARCHAR(50),
            artist_latitude FLOAT,
            artist_longitude FLOAT,
            artist_location VARCHAR(255),
            artist_name VARCHAR(255),
            song_id VARCHAR(50),
            title VARCHAR(255),
            duration FLOAT,
            year INT
        )
        """
)

songplay_table_create = ("""
        CREATE TABLE IF NOT EXISTS songplays (
            songplay_id INT IDENTITY(0,1) PRIMARY KEY,
            start_time TIMESTAMP NOT NULL,
            user_id INT NOT NULL,
            level VARCHAR(50),
            song_id VARCHAR(50),
            artist_id VARCHAR(50),
            session_id INT,
            location VARCHAR(255),
            user_agent VARCHAR(255)
        )
        """
)

user_table_create = ("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INT PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            gender CHAR(1),
            level VARCHAR(50)
        )
        """
)

song_table_create = ("""
        CREATE TABLE IF NOT EXISTS songs (
            song_id VARCHAR(50) PRIMARY KEY,
            title VARCHAR(255),
            artist_id VARCHAR(50),
            year INT,
            duration FLOAT
        )
        """
)

artist_table_create = ("""
        CREATE TABLE IF NOT EXISTS artists (
            artist_id VARCHAR(50) PRIMARY KEY,
            name VARCHAR(255),
            location VARCHAR(255),
            latitude FLOAT,
            longitude FLOAT
        )
        """
)

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
    start_time TIMESTAMP PRIMARY KEY,
    hour INT,
    day INT,
    week INT,
    month INT,
    year INT,
    weekday INT
);
""")
                     
# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]