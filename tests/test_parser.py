import os
import unittest
from pyxmex import Parser

class TestParser(unittest.TestCase):
    def setUp(self, session=None):
        self.parser = Parser()
        self.dummy_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'support/dummy_eptrn_raw')

    def test_parse_detail_record_from_file_parses_a_sample_file(self):
        parsed = self.parser.parse_detail_record_from_file(self.dummy_file_path)

        self.assertEqual(parsed['RECORD_OF_CHARGE_DETAIL_RECORD'][0]['TLRR_PAYMENT_NUMBER'], 'DUMT1234')
        self.assertEqual(parsed['RECORD_OF_CHARGE_DETAIL_RECORD'][0]['TLRR_CM_REF_NO'], '12345LMNA11')

if __name__ == '__main__':
    unittest.main()
