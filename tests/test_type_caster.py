import os
import unittest
import datetime
from pyxmex import TypeCaster

class TestTypeCaster(unittest.TestCase):
    def test_parse_parses_decimals_correctly(self):
        self.assertEqual(TypeCaster.parse('decimal', '000000001199N'), -119.95)
        self.assertEqual(TypeCaster.parse('decimal', '000000000799N'), -79.95)
        self.assertEqual(TypeCaster.parse('decimal', '000000001299R'), -129.99)
        self.assertEqual(TypeCaster.parse('decimal', '000000000119E'), 11.95)
        self.assertEqual(TypeCaster.parse('decimal', '000000000149E'), 14.95)

    def test_parse_parses_julians_correctly(self):
        self.assertEqual(TypeCaster.parse('julian', '2016144'), datetime.datetime(2016, 5, 23))
        self.assertEqual(TypeCaster.parse('julian', '2013001'), datetime.datetime(2013, 1, 1))

    def test_parse_parses_date_and_time_patterns_correctly(self):
        self.assertEqual(TypeCaster.parse('date(%Y-%m-%d)', '2016-03-01'), datetime.datetime(2016, 3, 1))
        self.assertEqual(TypeCaster.parse('time(%Y-%m-%d %H:%M:%S)', '2018-11-12 13:22:56'), datetime.datetime(2018, 11, 12, 13, 22, 56))

    def test_parse_parses_numeric_correctly(self):
        self.assertEqual(TypeCaster.parse('numeric', '10'), 10)

    def test_parse_parses_string_correctly(self):
        self.assertEqual(TypeCaster.parse('string', '10'), '10')

    def test_not_real_type_raises_a_helpful_error(self):
        with self.assertRaises(ValueError) as context:
            TypeCaster.parse('x', '2016-03-01')

        self.assertTrue('ValueError: Could not parse 2016-03-01 with type x', str(context.exception))

if __name__ == '__main__':
    unittest.main()
