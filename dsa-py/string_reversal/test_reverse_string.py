import unittest
from reverse_string import reverseString

class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverseString("hello"), "olleh")
        self.assertEqual(reverseString("hello world"), "dlrow olleh")
        self.assertEqual(reverseString("123! abc!"), "!cba !321")
        self.assertEqual(reverseString("I went to the shop"), "pohs eht ot tnew I")

unittest.main()