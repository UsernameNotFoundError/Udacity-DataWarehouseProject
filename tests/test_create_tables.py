import unittest
# To import the class 
import os, sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from create_tables.create_tables import CreateTables

class TestEtl(unittest.TestCase):
    """Test class for the create_tables."""
    def setUp(self) -> None:
        self.my_test_instance = CreateTables()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_database_connection(self):
        """Check that the database connection is not None"""
        self.assertTrue( self.my_test_instance.conn is not None )
    
    
    def test_table_creation_and_deletion(self):
        self.my_test_instance.create_tables()
        self.my_test_instance.cur.execute("SELECT COUNT(*) FROM information_schema.tables")
        my_sql_query_result = self.my_test_instance.cur.fetchone()
        print('HEllo\n', my_sql_query_result)
        self.assertIsNotNone( my_sql_query_result[0] )


if __name__ == "__main__":
    unittest.main()