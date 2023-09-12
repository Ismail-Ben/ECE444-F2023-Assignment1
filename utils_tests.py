import unittest
from utils import Utils

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.utils = Utils()

    def test_reversed_with_integer_input(self):
        self.assertEqual(self.utils.reversed(12345), 54321)

    def test_formatter_with_integer_input(self):
        binary, octal = self.utils.formatter(8)
        self.assertEqual(binary, '0b1000')
        self.assertEqual(octal, '0o10')

    def test_reversed_with_string_input(self):
        with self.assertRaises(AssertionError):
            self.utils.reversed("hi")

    def test_formatter_with_string_input(self):
        with self.assertRaises(AssertionError):
            self.utils.formatter("hi")

    def test_reversed_with_float_input(self):
        with self.assertRaises(AssertionError):
            self.utils.reversed(4.20)

    def test_formatter_with_float_input(self):
        with self.assertRaises(AssertionError):
            self.utils.formatter(4.20)

if __name__ == '__main__':
    unittest.main()

