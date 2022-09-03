"""
In this module we design all nessary
function that create the database and its schema.

To build a star schema we have function to create and drop all the tables:

"""
import psycopg2
from sql_queries import drop_queries, create_queries 


def create_database():


    # connect to the existed database
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=advanced")
    conn.set_session(autocommit=True)
    curs = conn.cursor()

    # drop the database first if existed
    curs.execute("DROP DATABASE IF EXISTS sparkify WITH (FORCE)")
    
    # create a new database 
    curs.execute("CREATE DATABASE sparkify")

    # close connection to default database
    conn.close() 


    # connect to sparkify database
    conn = psycopg2.connect("host=localhost dbname=sparkify user=postgres password=advanced")
    conn.set_session(autocommit=True)
    curs = conn.cursor()
    
    # return the connection and cursor to use in other functions

    return conn, curs
    

def drop_tables(conn,curs):

    for query in drop_queries:
        
        curs.execute(query)
        conn.commit()
        



def create_tables(conn,curs):

    for query in create_queries:
        
        curs.execute(query)
        conn.commit()

