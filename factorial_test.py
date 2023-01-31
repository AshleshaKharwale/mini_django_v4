from factorial import *
import unittest


class TestFact(unittest.TestCase):
    def test_fact(self):
        result1 = fact(5)
        self.assertEqual(result1, 120)

    def test_fact_1(self):
        result2 = fact(0)
        self.assertEqual(result2, 1)

    def test_div_by_zero(self):
        self.assertRaises(ZeroDivisionError, div, 0)


if __name__ == "__main__":
    unittest.main()
