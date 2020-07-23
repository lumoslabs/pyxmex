import os
import unittest
import datetime
from pyxmex import EMINQParser

class TestEMINQParser(unittest.TestCase):
    def setUp(self, session=None):
        self.parser = EMINQParser()
        self.dummy_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'support/dummy_eminq_raw')

    def test_process_parses_a_sample_file(self):
        parsed = self.parser.process(self.dummy_file_path)

        self.assertEqual(parsed[0]['SE_NO'], '9450000003')
        self.assertEqual(parsed[0]['CASE_NO'], 'E1307900972')
        self.assertEqual(parsed[0]['SE_REPLY_BY_DT'], datetime.datetime(2013, 4, 3))
        self.assertEqual(parsed[0]['TRANS_DATE'], datetime.datetime(2013, 1, 31))
        self.assertEqual(parsed[0]['TRANS_AMT'], 58.25)
        self.assertEqual(parsed[0]['TRANS_CURR_CD'], 'EUR')
        self.assertEqual(parsed[0]['FIRST_PRSNT_AMT'], 58.25)

        self.assertEqual(parsed[1]['TRANS_AMT'], 69.99)

if __name__ == '__main__':
    unittest.main()
