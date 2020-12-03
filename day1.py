from utilities import get_data_as_csv

data = get_data_as_csv('day1')

goal = 2020

clean_data = [int(num[0]) for num in data if int(num[0]) <= goal]
# clean_data = [1721,979,366,299,675,1456]


def check_number_against_list(seed_number, data_list, goal=goal):
    for element in data_list:
        if seed_number + element == goal:
            return element
    return "not found"
        
def part_a(clean_data):
    '''
    * Specifically, they need you to find the two entries that
    * sum to 2020 and then multiply those two numbers together.
    '''
    for i in range(len(clean_data)):
        seed_number = clean_data[i]
        data_list = clean_data[i+1:]
        result = check_number_against_list(seed_number,data_list)
        if result == "not found":
            continue
        break

    print(seed_number, result)
    print(seed_number * result)
    
def part_b(clean_data):
    '''
    * Specifically, they need you to find the 3 entries that
    * sum to 2020 and then multiply those 3 numbers together.
    '''
    for i in range(1, len(clean_data)):
        base_number = clean_data[i-1]
        next_number = clean_data[i]
        seed_number = base_number + next_number

        data_list = clean_data[i+1:] # slice off seed number(s)

        result = check_number_against_list(seed_number,data_list)
        if result == "not found":
            continue
        break
    
    print(base_number, next_number, result)
    if result == "not found":    
        return
    
    print(base_number * next_number * result)
    
part_b(clean_data)