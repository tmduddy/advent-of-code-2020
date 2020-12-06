from utilities import get_data_as_csv
raw = get_data_as_csv('day5')
data = [str(row[0]) if len(row) > 0 else "" for row in raw]
sample = [
"BFFFBBFRRR",
"FFFBBBFRRR",
"BBFFBBFRLL"
]

def code_to_int(code, one_char):
    binary_rep = []
    for char in code:
        if char == one_char:
            binary_rep.append(1)
        else:
            binary_rep.append(0)
    
    binary_rep_rev = [i for i in reversed(binary_rep)]
    sum = 0
    for i,char in enumerate(binary_rep_rev):
        binary_mult = 2**i
        sum += (binary_mult * char)
    return sum

def part1(data):
    seat_ids = []
    for seat in data:
        row = code_to_int(seat[:7], "B")
        col = code_to_int(seat[7:], "R")
        seat_id = row * 8 + col
        seat_ids.append(seat_id)
    print(max(seat_ids))

def part2(data):
    seat_ids = []
    for seat in data:
        row = code_to_int(seat[:7], "B")
        col = code_to_int(seat[7:], "R")
        seat_id = row * 8 + col
        seat_ids.append(seat_id)
        
    seat_ids = sorted(seat_ids)
    for i in range(0, len(seat_ids)-1):
        if (seat_ids[i+1] - seat_ids[i]) != 1:
            print(seat_ids[i+1], seat_ids[i])

# part1(data)
part2(data)
