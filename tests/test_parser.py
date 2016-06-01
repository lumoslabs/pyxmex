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

    def test_left_outer_join_sections_joins_sections_on_requested_fields(self):
        parsed = self.parser.parse_detail_record_from_file(self.dummy_file_path)

        def join_condition(left_instance, right_instance):
            return left_instance['TLRR_PAYMENT_NUMBER'] == right_instance['PAYMENT_NUMBER']

        joined = self.parser.left_outer_join_sections(
            left_collection=parsed['RECORD_OF_CHARGE_DETAIL_RECORD'],
            right_collection=parsed['SUMMARY_RECORD'],
            join_condition=join_condition
        )

        self.assertEqual(joined[0]['PAYMENT_DATE'], '2013068')
        self.assertEqual(joined[0]['AMEX_PAYEE_NUMBER'], '3491124567')
        self.assertEqual(joined[0]['PAYMENT_NUMBER'], joined[0]['TLRR_PAYMENT_NUMBER'])

if __name__ == '__main__':
    unittest.main()
