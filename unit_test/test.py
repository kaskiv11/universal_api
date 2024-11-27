import unittest
from operations import *


class TestOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 15), 25)

    def test_add_zero(self):
        self.assertEqual(add(10, 0), 10)
        self.assertEqual(add(0, 10), 10)

    def test_is_found_item_of_list(self):
        items = [1, 3, 7, 23, -40]
        self.assertIn(1, items)
        item = 23
        fake_item = 13
        self.assertTrue(is_found_item_of_list(items, item))
        self.assertFalse(is_found_item_of_list(items, fake_item))

    def test_merge_two_dicts(self):
        self.assertEqual(merge_two_dicts({"a": 1, "b": 2}, {"b": 6, "c": "7"}), {'a': 1, 'b': 8, 'c': '7'})

    def test_negative__check_positive_number(self):
        with self.assertRaises(ValueError) as contex:
            check_positive_number(-5)
        self.assertEqual(str(contex.exception), "The number cannot be negative.")

    def test_non_numeric_input_check_positive_number(self):
        with self.assertRaises(TypeError):
            check_positive_number("a string")
        with self.assertRaises(TypeError):
            check_positive_number(None)