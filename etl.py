"""
In this module, we desin all nessary functions that process and load data
to the postgres database

"""


import os
import glob

import pandas as pd
from sql_queries import *


# Get all the data files

def get_data(path):
    
    all_files = []
    for root,dire,file in os.walk(path):
    
        files = glob.glob(os.path.join(root,'*.json'))
        for file in files:
            all_files.append(file)

    return all_files


# process time in log file and extract different aspects of time

def handle_time(df2):

    df2['datetime'] = pd.to_datetime(df2['ts'],unit='ms')
    df2['year'] = df2['datetime'].dt.year
    df2['month'] = df2['datetime'].dt.month
    df2['day'] = df2['datetime'].dt.day
    df2['hour'] = df2['datetime'].dt.hour
    df2['day_name'] = df2['datetime'].dt.day_name()
    df2['week'] = df2['datetime'].dt.isocalendar().week

    df_t = df2[['datetime', 'hour', 'day', 'week', 'month', 'year', 'day_name']]

    return df_t




# processing the song file and load data to songs and artist tables


def process_song_files(curs, path):

    files = get_data(path)

    for file in files:

        df = pd.read_json(file, lines=True)
        
        songs_data = df[['song_id','title','artist_id', 'year', 'duration']].values[0].tolist()
        artist_data = df[['artist_id','artist_name','artist_location', 'artist_latitude', 'artist_longitude']].values[0].tolist()

        curs.execute(insert_songs, songs_data)
        curs.execute(insert_artist, artist_data)


def process_log_files(curs, path):

    files = get_data(path)

    for file in files:

        df = pd.read_json(file, lines=True)

        # filter by NextSong action
        df = df.loc[df['page'] == 'NextSong']

        #get data for time table
        df_t = handle_time(df)


        #get data for user table
        df_user = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

        for i, row in df_t.iterrows():
            curs.execute(insert_time, row.values.tolist())

        for i, row in df_user.iterrows():
            curs.execute(insert_users, row.values.tolist())



        #get data for songplays table

        for index, row in df.iterrows():

            out= curs.execute(select_ids, [row.song, row.artist, row.length])
    
            artist_id, song_id = out if out else None, None

            data_songplays = [row.ts, row.userId, row.level, song_id, artist_id, row.itemInSession, row.location, row.userAgent]

            curs.execute(insert_songplays, data_songplays)
    
        
    
        










    




        

    








