from yaml import safe_load
import os
from . import utils
from .parser import Parser

class EPTRNParser(Parser):
    def __init__(self, config_file=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config/eptrn.yml')):
        super(self.__class__, self).__init__()

        with open(config_file) as f:
            config = safe_load(f)

        self.eptrn_config = config['DETAIL_RECORD']
        self.section_types = list(self.eptrn_config['TYPE_MAPPING'].values())

        self.record_type_field = config['GENERAL']['RECORD_TYPE_FIELD']
        self.record_types_to_skip = [config['DATA_FILE_HEADER_RECORD']['RECORD_TYPE'],
                                     config['DATA_FILE_TRAILER_RECORD']['RECORD_TYPE']]

    def process(self, file_name):
        result = {}

        for section_type in self.section_types:
            result[section_type] = []

        with open(file_name) as f:
            content = f.readlines()

            for line in content:
                # ignore the unneeded header and footer
                if utils.range_from_list(line, *self.record_type_field) in self.record_types_to_skip:
                    continue

                # find out what type of information this line contains
                section_type_mapping_key = utils.range_from_list(line, *self.eptrn_config['TYPE_FIELD'])
                section_type_name = self.eptrn_config['TYPE_MAPPING'][section_type_mapping_key]
                field_formats = self.eptrn_config['TYPES'][section_type_name]['FIELDS']

                # parse this line according to what type it is
                result[section_type_name].append(self._parse_line(field_formats, line))

        return result

