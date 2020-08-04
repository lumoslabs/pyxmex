from yaml import load, FullLoader
import os
from . import utils
from .parser import Parser

class CBNOTParser(Parser):
    def __init__(self, config_file=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config/cbnot.yml')):
        super(self.__class__, self).__init__()

        with open(config_file) as file:
            config = load(file, Loader=FullLoader)

        self.field_formats = config['CHARGEBACK_DETAIL_RECORD']['FIELDS']

    def process_lines(self, content):
        result = []

        # remove the unneeded header and footer
        del content[0]
        del content[-1]

        for line in content:
            result.append(self._parse_line(self.field_formats, line))
        return result
