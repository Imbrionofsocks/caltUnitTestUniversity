import unittest

from main import add, subtract, multiply, divide, power, sqrtl, factorial


class TestCalculatorFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-3, 5), 2)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(8, 5), 3)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-3, 5), -15)
        self.assertEqual(multiply(0, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(15, 5), 3)
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(10, 3), 10 / 3)
        self.assertEqual(divide(0, 5), 0)
        self.assertEqual(divide(5, 0), "Error")

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(-2, 2), 4)

    def test_sqrtl(self):
        self.assertEqual(sqrtl(9), 3)
        self.assertEqual(sqrtl(-16), "Error")
        self.assertEqual(sqrtl(25), 5)
        self.assertEqual(sqrtl(0), 0)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(-5), "Error")


if __name__ == '__main__':
    unittest.main()
