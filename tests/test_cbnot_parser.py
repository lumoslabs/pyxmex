import os
import unittest
import datetime
from pyxmex import CBNOTParser

class TestCBNOTParser(unittest.TestCase):
    def setUp(self, session=None):
        self.parser = CBNOTParser()
        self.dummy_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'support/dummy_cbnot_raw')

    def test_process_parses_a_sample_file(self):
        parsed = self.parser.process(self.dummy_file_path)

        self.assertEqual(parsed[0]['SE_NUMB'], '1234398429')
        self.assertEqual(parsed[0]['CB_REFERENCE_CODE'], '17512345')
        self.assertEqual(parsed[0]['DATE_OF_CHARGE'], datetime.datetime(2017, 1, 11))
        self.assertEqual(parsed[0]['CB_AMOUNT'], -89.95)

        self.assertEqual(parsed[1]['CB_AMOUNT'], -33.10)

        self.assertEqual(parsed[2]['SE_NUMB'], '1554988333')
        self.assertEqual(parsed[2]['CB_REFERENCE_CODE'], '12217749')
        self.assertEqual(parsed[2]['DATE_OF_CHARGE'], datetime.datetime(2017, 1, 15))
        self.assertEqual(parsed[2]['CB_AMOUNT'], -40.07)


if __name__ == '__main__':
    unittest.main()
