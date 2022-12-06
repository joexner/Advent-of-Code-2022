with open('Day 6 input.txt') as file:
    line = file.readline().strip()
    for n in range(4, len(line)):
        subsection = line[n - 4:n]
        if len(set(subsection)) == 4:
            print(n)
            exit(0)