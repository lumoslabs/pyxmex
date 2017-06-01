# Pyxmex
Parse American Express EPTRN (transaction) and CBNOT (chargeback) files in Python

## Installation
`$ pip install pyxmex`

## Usage
The EPTRN or CBNOT parser can be instantiated with no args to use the default EPTRN config, or you can pass a path to a config file.
The #process method is called with the location of the raw file you want parsed.
```python
from pyxmex import EPTRNParser
parser = EPTRNParser()

parsed = parser.process('MYCOMPANY.EPTRN')

parsed['RECORD_OF_CHARGE_DETAIL_RECORD'][0]['TLRR_PAYMENT_NUMBER']
# => 'DUMT1234'
```

```python
from pyxmex import CBNOTParser
parser = CBNOTParser()

parsed = parser.process('MYCOMPANY.CBNOT')

parsed[0]['CB_REFERENCE_CODE']
# => 'DUMT1234'
```

The joiner can be used to join different sections of the result.

```python
from pyxmex import Joiner

def join_condition(left_instance, right_instance):
    return left_instance['TLRR_PAYMENT_NUMBER'] == right_instance['PAYMENT_NUMBER']

joined = Joiner.left_outer_join_sections(
    left_collection=parsed['RECORD_OF_CHARGE_DETAIL_RECORD'],
    right_collection=parsed['SUMMARY_RECORD'],
    join_condition=join_condition
)

joined[0]['PAYMENT_NUMBER'] == joined[0]['TLRR_PAYMENT_NUMBER']
# => True
```
