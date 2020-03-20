import unittest
from bin2dec import convert_binary_to_decimal

class TestBin2Dec(unittest.TestCase):
    def test_convert_binary_to_decimal_success(self):
        self.assertEqual(convert_binary_to_decimal("100000000"), 256)
    
    def test_convert_binary_to_decimal_invalid_binary(self):
        with self.assertRaises(ValueError):
            convert_binary_to_decimal("256")


if __name__ == "__main__":
    unittest.main()