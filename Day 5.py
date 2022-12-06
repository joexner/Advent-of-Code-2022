import re

filename = 'Day 5 input.txt'

with open(filename) as file:
    line_iter = iter(file)
    num_stacks = 9
    stacks = [list() for n in range(num_stacks)]
    for _ in range(8):
        row_data = line_iter.__next__()
        for col_num in range(num_stacks):
            val = row_data[col_num * 4 + 1]
            if val.isalpha():
                stacks[col_num].append(val)
    num_row = line_iter.__next__()
    blank_row = line_iter.__next__()

    for line in line_iter:
        match = re.match("move (\d+) from (\d+) to (\d+)", line)
        (a, b, c) = map(int, match.groups())
        removed_items = [stacks[b-1].pop(0) for _ in range(a)]
        stacks[c-1] = removed_items + stacks[c-1]

    f = ''.join([s[0] for s in stacks])
    print(f)