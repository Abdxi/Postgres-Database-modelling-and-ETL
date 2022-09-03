## Database Modelling with Postgres

### Overview
In this project, the client have data collected from their app and want to analyze it. 
they've been collecting on songs and user activity on their new music streaming app. 

The analytics team is particularly interested in understanding what songs users are listening to. 
Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

### Project description
Based on the client requirments we'll create a Postgres database with tables designed to optimize queries on song play analysis.

the steps we follow stated below:
- Design a star schema for the data
- Write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.
- Finally test the database and its functionality

### Dataset
There are two types of data files used in this project

#### Song Dataset:

The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.

`song_data/A/B/C/TRABCEI128F424C983.json`
`song_data/A/A/B/TRAABJL12903CDCF1A.json`

#### Log Dataset:
These files (in JSON format) contain user activeity data on the client new music streaming app.

Here are filepaths to two files in this dataset.

`log_data/2018/11/2018-11-12-events.json`
`log_data/2018/11/2018-11-13-events.json`

### Database Schema
We used a star schema used for this project to optimize the nalaytics jobs
There is a fact table that contain all the user activity measures, and 4 dimentional tables (users, artists, songs and time) referenced from the fact table by the primary keys.

![alt text](https://github.com/Abdxi/Postgres-Database-modelling-and-ETL/blob/main/images/database%20schema.png)
