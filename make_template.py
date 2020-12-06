import sys

arg = sys.argv[1]

if len(sys.argv) != 2 or (len(arg) != 4 and len(arg) != 5) or "day" not in arg:
    raise ValueError('Provide a day name and index e.g. day1')

template = f'''\
from utilities import get_data_as_csv
\
raw = get_data_as_csv('{arg}')
data = [str(row[0]) for row in raw]
sample = [

]

def part1(data):
    pass

def part2(data):
    pass

part1(sample)
'''

with open(f'{arg}.py', 'w') as f:
  f.write(template)

with open(f'input-files/{arg}.csv', 'w') as f:
    pass