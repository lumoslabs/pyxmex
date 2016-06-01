# Pyxmex
Parse American Express EPTRN files in python

## Installation
`$ pip install pyxmex`

## Usage
```python
from pyxmex import Parser
parser = Parser()

parsed = parser.parse_detail_record_from_file('MYCOMPANY.EPTRN')

parsed['RECORD_OF_CHARGE_DETAIL_RECORD'][0]['TLRR_PAYMENT_NUMBER']
# => 'DUMT1234'
```
