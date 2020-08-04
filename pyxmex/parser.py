from . import utils
from pyxmex.type_caster import TypeCaster


class Parser(object):
    def process(self, file_name):
        try:
            with open(file_name) as f:
                content = f.readlines()
                return self.process_lines(content)
        except UnicodeDecodeError:
            with open(file_name, 'rb') as f:
                content = f.readlines()
                return self.process_lines(content)

    def _parse_line(self, field_formats, line, range_offset=0):
        fields = {}

        for field_format in field_formats:
            field_range = []
            for index in field_format['RANGE']:
              field_range.append(index + range_offset)

            raw_value = utils.range_from_list(line, *field_range).rstrip(' ')
            fields[field_format['NAME']] = TypeCaster.parse(field_format['TYPE'], raw_value, field_name=field_format['NAME']) if field_format.get('TYPE') else raw_value

        return fields
