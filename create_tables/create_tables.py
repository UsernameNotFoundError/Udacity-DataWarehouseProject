import configparser
import psycopg2
import sys
import os
# To import the variable
current_dir = os.path.dirname(os.path.realpath(__file__))
print(current_dir)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from create_tables.sql_queries import create_table_queries, drop_table_queries

class CreateTables():
    conn = None
    cur = None
    def __init__(self) -> None:
        self.connect_to_database()   
        if self.conn is not None:
            self.drop_tables()
            self.create_tables()
            #self.conn.close() 


    def connect_to_database(self) -> None:
        config = configparser.ConfigParser()
        config.read('dwh.cfg')
        try:
            self.conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
            self.conn.autocommit = True
            self.cur = self.conn.cursor()
        except (Exception, psycopg2.Error) as e:
            print("Error connecting to database:", e)
        

    def create_tables(self) -> None:
        for query in create_table_queries:  # imported object
            self.execute_sql_commands(query)
            
            
    def drop_tables(self) -> None:
        for query in drop_table_queries:  # imported object
            self.execute_sql_commands(query)

    
    def execute_sql_commands(self, my_command:str) -> None:
        try:
            self.cur.execute(my_command)
        except Exception as e:
            print("Error executing SQL command:", e)


if __name__ == "__main__":
    CreateTables()