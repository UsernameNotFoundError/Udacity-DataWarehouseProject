import unittest
from create_tables.create_tables import CreateTables


class TestEtl(unittest.TestCase):

    def setUp(self) -> None:
        self.my_test_instance = CreateTables()
    
    def tearDown(self) -> None:
        return super().tearDown()
    

if __name__ == "__main__":
    unittest.main()