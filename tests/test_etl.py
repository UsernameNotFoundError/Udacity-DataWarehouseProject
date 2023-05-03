import unittest
from etl.etl import Etl


class TestEtl(unittest.TestCase):

    def setUp(self) -> None:
        self.my_test_instance = Etl()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_1(self):
        self.assertEqual(5,5.0)
    
    def test_2(self):
        self.assertEqual(4,4)

    def test_3(self):
        self.assertEqual(4,6)
        with self.assertRaises(ValueError):
            pass
    
if __name__ == "__main__":
    unittest.main()