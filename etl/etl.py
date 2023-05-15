import configparser
import psycopg2
import boto3
from sql_queries import copy_table_queries, insert_table_queries

class Etl():
    conn = None
    def __init__(self) -> None:
        self.check_parameters()
        self.connect_to_database()   
        if self.conn is not None:
            '''
            self.execute_sql_commands(
                    """
                    SELECT 
                        *
                    FROM staging_songs
                    """
            )
            row = self.cur.fetchone()
            while row:
                print(row)
                row = self.cur.fetchone()
            '''            
            self.load_staging_tables()
            self.insert_tables()
            self.conn.close()  # Comment this for tests
    
    
    def check_parameters(self) -> None:
        """Check if some of the required parameters are missing in the configuration file
        Raises an error if any are missing."""
        self.CONFIG = configparser.ConfigParser()
        self.CONFIG.read('dwh.cfg')
        self.missing_parameters = [option for section in self.CONFIG .sections() 
                                   for option in self.CONFIG .options(section) 
                                   if not len(self.CONFIG .get(section, option))]
        if len(self.missing_parameters):
            raise MissingParameterError(
                    """Missing parameter(s):\
                    \n\t>>> {}\
                    \nPlease check your configuration file and try again!
                    """.format('\n\t>>> '.join(self.missing_parameters)))
        
        
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
        # Old code
        config = configparser.ConfigParser()
        config.read('dwh.cfg')
        s3 = boto3.resource('s3',
                            region_name="us-west-2",
                            aws_access_key_id=f"{config.get('IAM_USER', 'KEY')}",
                            aws_secret_access_key=f"{config.get('IAM_USER', 'SECRET')}")
        bucket = s3.Bucket('udacity-dend')
        i=0
        for obj in bucket.objects.filter(Prefix='song-data'):
            print("Loading {} into database".format(obj.key))
            if i==0:
                print('jumping!')
                i+=1
                continue
            self.execute_sql_commands(
                    """
                    COPY staging_songs FROM 's3://udacity-dend/{}' 
                    CREDENTIALS 'aws_iam_role={}'
                    FORMAT AS json 'auto'
                    TRUNCATECOLUMNS
                    compupdate off region 'us-west-2';
                    """.format(obj.key, config.get('IAM_ROLE', 'ARN'))
            )
            i+=1
            if i>10000:
                pass # break
        
        return   
        '''
        for query in copy_table_queries:  # imported object
            print("Current query: {}\n".format(query))
            self.execute_sql_commands(query)
        '''

class MissingParameterError(Exception):
    """Just an exception to be raised when a required parameter is missing from configuration file"""
    pass


if __name__ == "__main__":
    Etl()