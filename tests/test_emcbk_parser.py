import os
import unittest
import datetime
from pyxmex import EMCBKParser

class TestEMCBKParser(unittest.TestCase):
    def setUp(self, session=None):
        self.parser = EMCBKParser()
        self.dummy_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'support/dummy_emcbk_raw')

    def test_process_parses_a_sample_file(self):
        parsed = self.parser.process(self.dummy_file_path)

        self.assertEqual(parsed[0]['SE_NO'], '9490000016')
        self.assertEqual(parsed[0]['CASE_NO'], 'E1301100302')
        self.assertEqual(parsed[0]['CHRGBK_DT'], datetime.datetime(2013, 3, 29))
        self.assertEqual(parsed[0]['CHRGBK_AMT'], 100.00)
        self.assertEqual(parsed[0]['CHRGBK_CURR_CD'], 'EUR')
        self.assertEqual(parsed[0]['CHRGBK_RSN_CD'], '4763')

        self.assertEqual(parsed[1]['CHRGBK_AMT'], 222.00)

if __name__ == '__main__':
    unittest.main()
