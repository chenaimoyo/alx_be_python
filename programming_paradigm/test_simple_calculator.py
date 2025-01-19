import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, 0), -1)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-2, 7), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(5000000, 1000000), 6000000)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(5.5, 2.3), 7.8)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)  # Handle floating-point precision

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(1, -1), 2)
        self.assertEqual(self.calc.subtract(1, 0), 1)
        self.assertEqual(self.calc.subtract(-1, 0), -1)
        self.assertEqual(self.calc.subtract(5, 1), 4)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-2, -5), 3)
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertEqual(self.calc.multiply(0, 1), 0)
        self.assertEqual(self.calc.multiply(10, 10), 100)
        self.assertEqual(self.calc.multiply(-1, 0), 0)
        self.assertEqual(self.calc.multiply(-5, -5), 25)
        self.assertEqual(self.calc.multiply(5, -5), -25)
        self.assertEqual(self.calc.multiply(100, 0), 0)
        self.assertEqual(self.calc.multiply(1000, 1000), 1000000)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(10, -5), -2)
        self.assertEqual(self.calc.divide(10, 10), 1)
        self.assertEqual(self.calc.divide(-10, -5), 2)
        self.assertEqual(self.calc.divide(1000000, 10), 100000)
        self.assertEqual(self.calc.divide(1000000, 1), 1000000)
        self.assertEqual(self.calc.divide(1, -1), -1)

        # Division by zero
        self.assertIsNone(self.calc.divide(6, 0))
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == "__main__":
    unittest.main()
