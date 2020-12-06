from utilities import get_data_as_csv
raw = get_data_as_csv('day3')

data = [str(row[0]) for row in raw]

for row in data: print(row)