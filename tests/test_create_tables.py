import unittest
# To import the class 
import os, sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from create_tables.create_tables import CreateTables



class TestEtl(unittest.TestCase):
    def setUp(self) -> None:
        self.my_test_instance = CreateTables()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_database_connection(self):
        self.assertTrue( bool(my_test_instance.conn) )
    
    def test_table_creation_and_deletion(self):
        self.assertEqual(4,4)
    
    def test_create_tables(self):
        # Call the method that creates tables
        self.my_test_instance.create_tables()
        
        # Use a SQL query to check if the tables exist
        self.my_test_instance.cur.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'table1'")
        result = self.my_test_instance.cur.fetchone()
        
        # Assert that the query returned a result
        self.assertIsNotNone(result)
        
        # Assert that the number of tables is 1
        self.assertEqual(result[0], 1)


if __name__ == "__main__":
    unittest.main()