import utils
from pyxmex.type_caster import TypeCaster


class Parser(object):
    def _parse_line(self, field_formats, line):
        fields = {}

        for field_format in field_formats:
            raw_value = utils.range_from_list(line, *field_format['RANGE']).rstrip(' ')
            fields[field_format['NAME']] = TypeCaster.parse(field_format['TYPE'], raw_value) if field_format.get('TYPE') else raw_value

        return fields
