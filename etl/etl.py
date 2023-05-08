import configparser
import psycopg2
from etl.sql_queries import copy_table_queries, insert_table_queries

class Etl():
    conn = None
    def __init__(self) -> None:
        self.CONFIG = configparser.ConfigParser()
        self.CONFIG.read('dwh.cfg')
        self.connect_to_database()        
        if self.conn is not None:
            self.load_staging_tables()
            self.insert_tables()
            #self.conn.close()  # Close Database connection
        
        
    def connect_to_database(self) -> None:
        try:
            self.conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*self.CONFIG['CLUSTER'].values()))
            self.conn.autocommit = True
            self.cur = self.conn.cursor()
        except (Exception, psycopg2.Error) as e:
            print("Error connecting to database:", e)


    def execute_sql_commands(self, my_command:str) -> None:
        try:
            self.cur.execute(my_command)
        except Exception as e:
            print("Error executing SQL command:", e)
            

    def insert_tables(self) -> None:
        for query in insert_table_queries:  # imported object
            self.execute_sql_commands(query)

            
    def load_staging_tables(self) -> None:
        """Loads staging tables into database from s3 bucket"""
        for query in copy_table_queries:  # imported object
            self.execute_sql_commands(query)


if __name__ == "__main__":
    Etl()