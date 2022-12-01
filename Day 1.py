from locale import atoi

filename = 'Day 1 - input.txt'
groups = []
with open(filename) as file:
    group_value = 0
    for line in file:
        line = line.strip()
        if len(line) > 0:
            group_value += atoi(line)
        else:
            groups.append(group_value)
            group_value = 0

print(max(groups))

print(sum(sorted(groups, reverse=True)[0:3]))
