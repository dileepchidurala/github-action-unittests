import unittest

from calculator import addition, subtraction, multiplication, division


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(5, 10), 15)

    def test_subtraction(self):
        self.assertEqual(subtraction(10, 5), 5)

    def test_multiplication(self):
        self.assertEqual(multiplication(10, 5), 50)

    def test_division(self):
        self.assertEqual(division(10, 5), 2)
        # self.assertRaises(ZeroDivisionError, division, 10, 0)
        with self.assertRaises(ZeroDivisionError):
            division(10, 0)


if __name__ == '__main__':
    unittest.main()
