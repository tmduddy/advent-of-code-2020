import csv

def get_data_as_csv(day):
    with open(f'input-files/{day}.csv', 'r') as f:
        return [row for row in csv.reader(f)]