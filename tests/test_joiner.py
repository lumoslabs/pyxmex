import os
import unittest
import datetime
from pyxmex import Parser, Joiner

class TestJoiner(unittest.TestCase):
    def setUp(self, session=None):
        self.parser = Parser()
        self.dummy_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'support/dummy_eptrn_raw')

    def test_left_outer_join_sections_joins_sections_on_requested_fields(self):
        parsed = self.parser.process(self.dummy_file_path)

        def join_condition(left_instance, right_instance):
            return left_instance['TLRR_PAYMENT_NUMBER'] == right_instance['PAYMENT_NUMBER']

        joined = Joiner.left_outer_join_sections(
            left_collection=parsed['RECORD_OF_CHARGE_DETAIL_RECORD'],
            right_collection=parsed['SUMMARY_RECORD'],
            join_condition=join_condition
        )

        self.assertEqual(joined[0]['PAYMENT_DATE'], datetime.datetime(2013, 3, 9))
        self.assertEqual(joined[0]['AMEX_PAYEE_NUMBER'], 3491124567)
        self.assertEqual(joined[0]['PAYMENT_NUMBER'], joined[0]['TLRR_PAYMENT_NUMBER'])

if __name__ == '__main__':
    unittest.main()
