import unittest
from functions import add, subtract

class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        # Add more test cases

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        # Add more test cases

if __name__ == '__main__':
    unittest.main()
