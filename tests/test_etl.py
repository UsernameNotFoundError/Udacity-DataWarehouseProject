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
        pass #return super().tearDown()
    
    def test_database_connection(self):
        Etl.connect_to_database()
    
    def test_table_creation_and_deletion(self):
        self.assertEqual(4,4)

    def test_3(self):
        self.assertEqual(4,4)
        
    
if __name__ == "__main__":
    unittest.main()