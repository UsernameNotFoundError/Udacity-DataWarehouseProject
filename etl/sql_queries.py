import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# STAGING TABLES
staging_events_copy = (
    """
    COPY staging_events FROM '{}' 
    CREDENTIALS 'aws_iam_role={}' FORMAT JSON '{}'
    compupdate off region 'us-west-2';
    """
).format(config.get('S3', 'LOG_DATA'), config.get('IAM_ROLE', 'ARN'), config.get('S3', 'LOG_JSONPATH'))


staging_songs_copy = (
    """
    COPY staging_songs FROM '{}' 
    CREDENTIALS 'aws_iam_role={}'
    FORMAT AS json 'auto'
    TRUNCATECOLUMNS 
    compupdate off region 'us-west-2';
    """
).format(config.get('S3', 'SONG_DATA'), config.get('IAM_ROLE', 'ARN')) # MAXERROR 100

# FINAL TABLES

songplay_table_insert = (
        """
        INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
        SELECT 
        DATEADD(MILLISECONDS, staging_events.ts, 'epoch') AS start_time,
            staging_events.userId AS user_id,
            staging_events.level AS level,
            staging_songs.song_id AS song_id,
            staging_songs.artist_id AS artist_id,
            staging_events.sessionId AS session_id,
            staging_events.location AS location,
            staging_events.userAgent AS user_agent
        FROM staging_events 
        JOIN staging_songs ON staging_events.song = staging_songs.title AND staging_events.artist = staging_songs.artist_name
        """
)

user_table_insert = (
        """
        INSERT INTO users (user_id, first_name, last_name, gender, level)
        SELECT 
            userId AS user_id, 
            firstName AS first_name, 
            lastName AS last_name, 
            gender, 
            level
        FROM staging_events
        """
)

song_table_insert = (
        """
        INSERT INTO songs (song_id, title, artist_id, year, duration)
        SELECT 
            song_id,
            title,
            artist_id,
            year,
            duration
        FROM staging_songs
        """
)

artist_table_insert = (
        """
        INSERT INTO artists (artist_id, name, location, latitude, longitude)
        SELECT 
            artist_id, 
            artist_name AS name, 
            artist_location AS location, 
            artist_latitude AS latitude, 
            artist_longitude AS longitude
        FROM staging_songs;
"""
)

time_table_insert = (
        """
       INSERT INTO time (start_time, hour, day, week, month, year, weekday)
        SELECT 
                start_time,
                EXTRACT(hour FROM start_time) AS hour,
                EXTRACT(day FROM start_time) AS day,
                EXTRACT(week FROM start_time) AS week,
                EXTRACT(month FROM start_time) AS month,
                EXTRACT(year FROM start_time) AS year,
                EXTRACT(dayofweek FROM start_time) AS weekday
        FROM (
                SELECT DATEADD(MILLISECONDS, ts, 'epoch') AS start_time
                FROM staging_events
        )
        """
)

# QUERY LISTS
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
