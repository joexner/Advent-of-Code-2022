import re

filename = 'Day 4 input.txt'
score = 0
with open(filename) as file:
    redundancies = 0
    for line in file:
        (a,b,c,d) = map(int, re.match("(\d+)-(\d+),(\d+)-(\d+)", line.strip()).groups())
        ab = set(range(a, b + 1))
        cd = set(range(c, d + 1))
        if ab <= cd or cd <= ab:
            redundancies += 1
    print(redundancies)


