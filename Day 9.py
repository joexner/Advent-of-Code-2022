from numpy import sign

directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}
def translate(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])


positions = [(0,0) for _ in range(10)]
visited_positions = {(0,0)}

def print_grid():
    min_x = min(e[0] for e in positions)
    min_y = min(e[1] for e in positions)
    max_x = max(e[0] for e in positions)
    max_y = max(e[1] for e in positions)
    output_grid = [["." for _ in range(min_y, max_y + 1)] for _ in range(min_x, max_x + 1)]
    knot_names = ["H"]
    knot_names.extend(map(str, range(1,10)))
    for (knot_pos, knot_name) in zip(reversed(positions), reversed(knot_names)):
        output_grid[knot_pos[0] - min_x][knot_pos[1] - min_y] = knot_name
    print()
    for row in output_grid:
        print(''.join(row))


with open('Day 9 input.txt') as file:
    for line in file:
        (dir_name, steps) = line.split()
        dir = directions[dir_name]
        for step in range(int(steps)):
            # print_grid()
            positions[0] = translate(positions[0], dir)
            for p in range(1, 10):
                leading = positions[p-1]
                trailing = positions[p]
                vert_dist = leading[0] - trailing[0]
                horiz_dist = leading[1] - trailing[1]
                if max(abs(vert_dist), abs(horiz_dist)) > 1:
                    positions[p] = (
                        trailing[0] + int(sign(vert_dist)),
                        trailing[1] + int(sign(horiz_dist))
                    )
            if positions[9] not in visited_positions:
                visited_positions.add(positions[9])

print(len(visited_positions))


