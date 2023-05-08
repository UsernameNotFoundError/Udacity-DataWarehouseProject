import unittest
import sys
import os
# To import the class 
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from etl.etl import Etl

class TestEtl(unittest.TestCase):
    
    def setUp(self) -> None:
        self.my_test_instance = Etl()
    
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    
    def test_database_connection(self):
        """Check that the database connection is not None"""
        self.assertTrue( self.my_test_instance.conn is not None )
        
        
    def test_data_load_staging_tables(self):
        """Test is the Data insertion worked in staging tables"""
        self.my_test_instance.cur.execute("SELECT COUNT(*) FROM staging_songs")
        my_sql_query_result = self.my_test_instance.cur.fetchone()
        self.assertTrue( my_sql_query_result[0] )
        
        
    def test_data_inserted_into_database(self):
        """Test is the Data insertion works in teh tables"""
        self.my_test_instance.cur.execute("SELECT COUNT(*) FROM users")
        my_sql_query_result = self.my_test_instance.cur.fetchone()
        self.assertTrue( my_sql_query_result[0] )
        
    
if __name__ == "__main__":
    unittest.main()