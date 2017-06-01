import re
import datetime
import utils


class TypeCaster():
    # See page 55 of https://secure.cmax.americanexpress.com/Internet/MSWS/English/EPTRN_v1.9_October2015_Final.pdf
    DECIMAL_VALUE_CODES = {
        'A': '1',
        'B': '2',
        'C': '3',
        'D': '4',
        'E': '5',
        'F': '6',
        'G': '7',
        'H': '8',
        'I': '9',
        'J': '1',
        'K': '2',
        'L': '3',
        'M': '4',
        'N': '5',
        'O': '6',
        'P': '7',
        'Q': '8',
        'R': '9',
        '{': '0',
        '}': '0'
    }

    DATE_PATTERN = '^date\((.+)\)$'
    TIME_PATTERN = '^time\((.+)\)$'

    @classmethod
    def type_handling(self):
        return {
          'string': lambda raw_value: str(raw_value),
          'julian': self._parse_raw_julian,
          'date': lambda raw_value: datetime.datetime.strptime(raw_value, '%Y-%m-%d'),
          'numeric': lambda raw_value: int(raw_value),
          'float': lambda raw_value: float(raw_value),
          'decimal': self._parse_raw_decimal
        }

    @classmethod
    def parse(self, type_name, raw_value):
        if raw_value == '':
            return None

        handler_function = self.type_handling().get(type_name)

        if handler_function:
            return handler_function(raw_value)

        datetime_match = re.search(self.DATE_PATTERN, type_name) or re.search(self.TIME_PATTERN, type_name)

        if datetime_match:
            return datetime.datetime.strptime(raw_value, datetime_match.group(1))

        raise ValueError("Could not parse {0} with type {1}".format(raw_value, type_name))

    @staticmethod
    def _parse_raw_julian(julian_date):
        year_string = utils.range_from_list(julian_date, 0, 3)
        year = datetime.datetime.strptime(year_string, '%Y')
        days_string = utils.range_from_list(julian_date, 4, 6)
        adjusted_days = int(days_string) - 1 # adjust because we are already counting the first day of the year
        return year + datetime.timedelta(days=adjusted_days)

    @classmethod
    def _parse_raw_decimal(self, amex_decimal):
        if not re.search('^[0-9]*[0-9A-R{}]$', amex_decimal):
            raise ValueError("Unexpected decimal format for {}".fomat(amex_decimal))

        is_credit = bool(re.search('[JKLMNOPQR}]', amex_decimal))

        decoded_value_string = ''.join(self.DECIMAL_VALUE_CODES.get(s) or s for s in amex_decimal)

        dollars = float(decoded_value_string)  / 100

        # A debit amount is positive according to the docs
        return dollars * (-1 if is_credit else 1)
