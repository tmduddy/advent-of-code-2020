from math import ceil
from functools import reduce
from utilities import get_data_as_csv
raw = get_data_as_csv('day3')

data = [str(row[0]) for row in raw]
sample = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#"
]


def part1(data):
    # starting at the top left . (open square) how many # (trees)
    # would you encounter on a slope of right 3 down 1
    slopes = [
        {
            'x': 3,
            'y': -1
        }
    ]
    results = []
    for slope in slopes:
        num_trees = 0

        x_pos = 0
        y_pos = 0
        
        num_moves = ceil(len(data) / abs(slope['y']))
        map_width = len(data[0])

        for i in range(num_moves):
            spot = data[y_pos][x_pos % map_width]
            # print(f'checking {x_pos % map_width}, {y_pos}. found {spot}')
            if spot == "#":
                num_trees += 1
            x_pos += slope['x']
            y_pos -= slope['y']
        results.append(num_trees)
    print(results)


def part2(data):
    # starting at the top left . (open square) how many # (trees)
    # would you encounter on several different slopes? multiply the results
    slopes = [
        {
            'x': 1,
            'y': -1
        },
        {
            'x': 3,
            'y': -1
        },
        {
            'x': 5,
            'y': -1
        },
        {
            'x': 7,
            'y': -1
        },
        {
            'x': 1,
            'y': -2
        }
    ]
    results = []
    for slope in slopes:
        num_trees = 0

        x_pos = 0
        y_pos = 0
        
        num_moves = ceil(len(data) / abs(slope['y']))
        map_width = len(data[0])

        for i in range(num_moves):
            spot = data[y_pos][x_pos % map_width]
            # print(f'checking {x_pos % map_width}, {y_pos}. found {spot}')
            if spot == "#":
                num_trees += 1
            x_pos += slope['x']
            y_pos -= slope['y']
        results.append(num_trees)
    print(results)
    print(reduce(lambda x, y: x*y, results ))

# part1(data)
part2(data)