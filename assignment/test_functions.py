import unittest
from functions import add, subtract, multiply, divide

class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(3, 4), -1)

    def test_multiply(self):
        self.assertEqual(multiply(2,3), 6)
        self.assertEqual(multiply(2,0), 0)
        self.assertEqual(multiply(2,1), 2)
        self.assertEqual(multiply(-2,2), -4)

    def test_divide(self):
        self.assertEqual(divide(4,2), 2)
        self.assertEqual(divide(3,2), 1.5)

if __name__ == '__main__':
    unittest.main()
