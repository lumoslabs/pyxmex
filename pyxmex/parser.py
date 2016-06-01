from yaml import load, dump
import os


class Parser():
    def __init__(self, config_file=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config/eptrn.yml')):
        self.eptrn_config = load(open(config_file))['DETAIL_RECORD']
        self.section_types = [v for k, v in self.eptrn_config['TYPE_MAPPING'].iteritems()]

    def _range_from_list(self, list_obj, range_start, range_end):
        result_string = ''

        for idx, val in enumerate(list_obj):
            if idx >= range_start and idx <= range_end:
                result_string += val

        return result_string

    def _parse_line(self, section_type, line):
        fields = {}
        field_formats = self.eptrn_config['TYPES'][section_type]['FIELDS']

        for field_format in field_formats:
            fields[field_format['NAME']] = self._range_from_list(line, *field_format['RANGE'])

        return fields

    def left_outer_join_sections(self, left_collection, right_collection, join_condition):
        merged_sections = []

        for left_instance in left_collection:
            right_matching = [right_instance for right_instance in right_collection if join_condition(left_instance, right_instance)]

            merge_instance = left_instance.copy()

            if len(right_matching):
                relevant_right = right_matching[0]
                merge_instance.update(relevant_right)

            merged_sections.append(merge_instance)

        return merged_sections

    def parse_detail_record_from_file(self, file_name):
        result = {}

        for section_type in self.section_types:
            result[section_type] = []

        with open(file_name) as f:
            content = f.readlines()

            # remove the unneeded header and footer
            del content[0]
            del content[-1]

            for line in content:
                # find out what type of information this line contains
                section_type_mapping_key = self._range_from_list(line, *self.eptrn_config['TYPE_FIELD'])
                section_type_name = self.eptrn_config['TYPE_MAPPING'][section_type_mapping_key]

                # parse this line according to what type it is
                result[section_type_name].append(self._parse_line(section_type_name, line))

        return result
