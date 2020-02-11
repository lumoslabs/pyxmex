import os
import unittest
import datetime
from pyxmex import INQ02Parser

class TestINQ02Parser(unittest.TestCase):
    def setUp(self, session=None):
        self.parser = INQ02Parser()
        self.dummy_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'support/dummy_inq02_raw')

    def test_process_parses_a_sample_file(self):
        parsed = self.parser.process(self.dummy_file_path)

        self.assertEqual(parsed[0]['INQUIRY_CASE_NUMBER'], 'OKE2508')
        self.assertEqual(parsed[0]['SE_REPLY_BY_DATE'], datetime.datetime(2001, 2, 8, 0, 0))
        self.assertEqual(parsed[0]['INQUIRY_REASON_CODE'], '155')
        self.assertEqual(parsed[0]['CASE_TYPE'], 'SEDIS')
        self.assertEqual(parsed[0]['CHARGE_AMOUNT'], 9195.0)
        self.assertEqual(parsed[0]['DISPUTED_AMOUNT'], 9195.0)

if __name__ == '__main__':
    unittest.main()
