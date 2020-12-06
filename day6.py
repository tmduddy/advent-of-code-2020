from functools import reduce
from utilities import get_data_as_csv
raw = get_data_as_csv('day6')
data = [str(row[0]) if len(row) > 0 else "" for row in raw]
sample = [
    "abc",
    "",
    "a",
    "b",
    "c",
    "",
    "ab",
    "ac",
    "",
    "a",
    "a",
    "a",
    "a",
    "",
    "b"
]

alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
]
def empty_string_to_pipe(i):
    if i == "":
        return "|"
    return i
    
def part1(data):
    piped_data = [empty_string_to_pipe(i) for i in data]
    combined_data = ('').join(piped_data)
    split_data = combined_data.split('|')
    set_data = [set(i) for i in split_data]
    counts = [len(i) for i in set_data]
    final_sum = reduce(lambda x,y: x+y, counts)
    print(final_sum)

def part2(data):
    piped_data = [empty_string_to_pipe(i) for i in data]
    combined_data = (';').join(piped_data)
    split_data = combined_data.split('|')
    group_sums = []
    for i, group in enumerate(split_data):
        if i == 0 or i == len(split_data)-1:
            group += ";" # so that I can count the semi colons as num_participants for all cases
        group_total = 0
        num_participants = group.count(';')-1
        for question in alphabet:
            group_count = group.count(question)
            if group_count == 0:
                continue
            # print(f'question {question} had {group_count} answers across {num_participants} members')
            if group_count == num_participants:
                group_total += 1
        # print('-----')
        group_sums.append(group_total)
    final_sum = reduce(lambda x,y: x+y, group_sums)
    print(f'final answer {final_sum}')

# part1(data)
part2(data)
