from utilities import get_data_as_csv
raw = get_data_as_csv('day2')

data = [str(row[0]) for row in raw]
sample = ["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]

def part1(data, print_out=True):
    total_valid = 0

    for row in data:
        # convert low-high char: pwd to individual vars
        rule_low = int(row.split(':')[0].split(' ')[0].split('-')[0])
        rule_high =int(row.split(':')[0].split(' ')[0].split('-')[1])
        character = row.split(':')[0].split(' ')[1]
        password = row.split(':')[1]

        character_count = password.count(character) # std func to count instances of substr
        # print(character_count)
        if (character_count >= rule_low and character_count <= rule_high):
            total_valid += 1
    if(print_out):
        print(total_valid)
    return total_valid

def part2(data, debug=False, print_out=True):
    total_valid = 0

    for row in data:
        # convert low-high char: pwd to individual vars
        rule_low = int(row.split(':')[0].split(' ')[0].split('-')[0])
        rule_high =int(row.split(':')[0].split(' ')[0].split('-')[1])
        character = row.split(':')[0].split(' ')[1]
        password = row.split(':')[1][1:] # trim leading whitespace

        position_1 = password[rule_low-1]
        position_2 = password[rule_high-1]
        one_and_not_two = position_1 == character and position_2 != character
        not_one_and_two = position_1 != character and position_2 == character
        if (one_and_not_two or not_one_and_two):
            total_valid += 1

    if(print_out):
        print(f'total_valid: {total_valid}')
    return total_valid

part2(data, debug=False)