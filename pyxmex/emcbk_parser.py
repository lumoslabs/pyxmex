from yaml import load, FullLoader
import os
from . import utils
from .parser import Parser

class EMCBKParser(Parser):
    def __init__(self, config_file=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config/emcbk.yml')):
        super(self.__class__, self).__init__()

        with open(config_file) as file:
            config = load(file, Loader=FullLoader)

        self.field_formats = config['CHARGEBACK_DETAIL_RECORD']['FIELDS']

        # Amex indexes are not zero based. Use an offset (typically -1) to convert Amex's
        # documented indexes to their zero based equivalents.
        self.range_offset = config.get('RANGE_OFFSET', 0)

    def process(self, file_name):
        try:
            with open(file_name) as f:
                content = f.readlines()
                return self.process_lines(content)
        except UnicodeDecodeError:
            with open(file_name, encoding='latin-1') as f:
                content = f.readlines()
                return self.process_lines(content)

    def process_lines(self, content):
        result = []

        # remove the unneeded header and footer
        del content[0]
        del content[-1]

        for line in content:
            result.append(self._parse_line(self.field_formats, line, range_offset=self.range_offset))
        return result
