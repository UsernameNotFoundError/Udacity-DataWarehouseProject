import configparser
import psycopg2
from .sql_queries import copy_table_queries, insert_table_queries

class Etl():
    def __init__(self) -> None:
        self.connect_to_database()        
        self.load_staging_tables()
        self.insert_tables()
        self.conn.close()  # Close Database connection

    def connect_to_database(self) -> None:
        config = configparser.ConfigParser()
        config.read('dwh.cfg')

        self.conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
        """# Connect to the Redshift database
        self.conn = psycopg2.connect(
        host="<your-redshift-hostname>",
        dbname="<your-redshift-dbname>",
        user="<your-redshift-username>",
        password="<your-redshift-password>",
        port="<your-redshift-port>"
        )"""
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def execute_sql_commands(self, my_command:str) -> None:
        try:
            self.cur.execute(my_command)
        except Exception as e:
            print("Error executing SQL command:", e)
            

    def load_staging_tables(self) -> None:
        for query in copy_table_queries:
            self.execute_sql_commands(query)


    def insert_tables(self) -> None:
        for query in insert_table_queries:
            self.execute_sql_commands(query)




if __name__ == "__main__":
    Etl()