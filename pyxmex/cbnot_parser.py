from yaml import load, dump
import os
import utils
from parser import Parser

class CBNOTParser(Parser):
    def __init__(self, config_file=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config/cbnot.yml')):
        super(self.__class__, self).__init__()

        self.field_formats = load(open(config_file))['CHARGEBACK_DETAIL_RECORD']['FIELDS']

    def process(self, file_name):
        result = []

        with open(file_name) as f:
            content = f.readlines()

            # remove the unneeded header and footer
            del content[0]
            del content[-1]

            for line in content:
                result.append(self._parse_line(self.field_formats, line))

        return result
