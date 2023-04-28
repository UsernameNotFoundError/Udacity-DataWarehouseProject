import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

def execute_sql_commands(my_command:str) -> None:

    try:
        # Connect to the Redshift database
        conn = psycopg2.connect(
            host="<your-redshift-hostname>",
            dbname="<your-redshift-dbname>",
            user="<your-redshift-username>",
            password="<your-redshift-password>",
            port="<your-redshift-port>"
        )
        
        # Create a cursor object
        cur = conn.cursor()
        
        # Execute the SQL command
        cur.execute("<your-sql-command>")
        
        # Commit the transaction
        conn.commit()
        
    except Exception as e:
        # Rollback the transaction if there's an error
        conn.rollback()
        print("Error executing SQL command:", e)
        

def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()