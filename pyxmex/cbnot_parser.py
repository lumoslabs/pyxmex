from yaml import safe_load
import os
from . import utils
from .parser import Parser

class CBNOTParser(Parser):
    def __init__(self, config_file=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config/cbnot.yml')):
        super(self.__class__, self).__init__()

        with open(config_file) as f:
            config = safe_load(f)

        self.field_formats = config['CHARGEBACK_DETAIL_RECORD']['FIELDS']
        self.record_type_field = config['GENERAL']['RECORD_TYPE_FIELD']
        self.record_types_to_skip = [config['DATA_FILE_HEADER_RECORD']['RECORD_TYPE'],
                                     config['DATA_FILE_TRAILER_RECORD']['RECORD_TYPE']]


    def process(self, file_name):
        result = []

        with open(file_name) as f:
            content = f.readlines()

            for line in content:
                # ignore the unneeded header and footer
                if utils.range_from_list(line, *self.record_type_field) in self.record_types_to_skip:
                    continue

                result.append(self._parse_line(self.field_formats, line))

        return result
