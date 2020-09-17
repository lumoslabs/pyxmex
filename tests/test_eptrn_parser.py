import os
import unittest
import datetime
from pyxmex import EPTRNParser

from pyxmex.type_caster import TypeCaster

class TestEPTRNParser(unittest.TestCase):
    def setUp(self, session=None):
        self.parser = EPTRNParser()
        self.dummy_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'support/dummy_eptrn_raw')

    def test_process_parses_a_sample_file(self):
        parsed = self.parser.process(self.dummy_file_path)

        self.assertEqual(parsed['RECORD_OF_CHARGE_DETAIL_RECORD'][0]['TLRR_PAYMENT_NUMBER'], 'DUMT1234')
        self.assertEqual(parsed['RECORD_OF_CHARGE_DETAIL_RECORD'][0]['TLRR_CM_REF_NO'], '12345LMNA11')

        self.assertEqual(parsed['RECORD_OF_CHARGE_DETAIL_RECORD'][1]['TLRR_PAYMENT_NUMBER'], 'DUMT1237')
        self.assertEqual(parsed['RECORD_OF_CHARGE_DETAIL_RECORD'][1]['TLRR_CM_REF_NO'], '12998LMNA22')

    def test_process_has_types_casted_when_they_are_configured(self):
        parsed = self.parser.process(self.dummy_file_path)

        self.assertEqual(parsed['RECORD_OF_CHARGE_DETAIL_RECORD'][0]['TLRR_SOC_AMOUNT'], 373.05)
        self.assertEqual(parsed['RECORD_OF_CHARGE_DETAIL_RECORD'][0]['TLRR_TRAN_DATE'], datetime.datetime(2013, 3, 6))
        self.assertEqual(parsed['SUMMARY_RECORD'][0]['DEBIT_BALANCE_AMOUNT'], 0.0)

        self.assertEqual(parsed['RECORD_OF_CHARGE_DETAIL_RECORD'][1]['TLRR_SOC_AMOUNT'], 123.02)
        self.assertEqual(parsed['RECORD_OF_CHARGE_DETAIL_RECORD'][1]['TLRR_TRAN_DATE'], datetime.datetime(2013, 3, 8))
        self.assertEqual(parsed['SUMMARY_RECORD'][1]['DEBIT_BALANCE_AMOUNT'], 0.0)

if __name__ == '__main__':
    unittest.main()
