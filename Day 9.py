directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}
def translate(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])

head_pos = (0, 0)
tail_pos = (0, 0)
visited_positions = {tail_pos}
with open('Day 9 input.txt') as file:
    for line in file:
        (dir_name, steps) = line.split()
        dir = directions[dir_name]
        for _ in range(int(steps)):
            new_head_pos = translate(head_pos, dir)
            if max(abs(new_head_pos[0] - tail_pos[0]), abs(new_head_pos[1] - tail_pos[1])) > 1:
                tail_pos = head_pos
                visited_positions.add(tail_pos)
            head_pos = new_head_pos

print(len(visited_positions))


