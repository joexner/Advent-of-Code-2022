heights = []
visibilities = []

with open('Day 8 input.txt') as file:
    for line in file:
        row_data = [int(c) for c in line.strip()]
        heights.append(row_data)
        visibilities.append([False for height in row_data])


def mark_visible(pos, direction, max_seen):
    current_height = heights[pos[0]][pos[1]]
    if current_height > max_seen:
        visibilities[pos[0]][pos[1]] = True
        max_seen = current_height
    new_pos = (pos[0] + direction[0], pos[1] + direction[1])
    if new_pos[0] >= 0           and new_pos[1] >= 0 and \
       new_pos[0] < len(heights) and new_pos[1] < len(heights[0]) :
            mark_visible(new_pos, direction, max_seen)

for row in range(len(heights)):
    mark_visible((row, 0               ), (0,  1), -1)
    mark_visible((row, len(heights) - 1), (0, -1), -1)

for col in range(len(heights[0])):
    mark_visible((0,                   col), (1,  0), -1)
    mark_visible((len(heights[0]) - 1, col), (-1, 0), -1)

num_visible = 0
for row in visibilities:
    visible_in_row = sum(1 if val else 0 for val in row)
    num_visible += visible_in_row

print(num_visible)

def viewing_distance(pos, direction, initial_height):
    target_pos = (pos[0] + direction[0], pos[1] + direction[1])
    if target_pos[0] >= 0           and target_pos[1] >= 0 and \
       target_pos[0] < len(heights) and target_pos[1] < len(heights[0]) :
        target_height = heights[target_pos[0]][target_pos[1]]
        if target_height < initial_height:
            return 1 + viewing_distance(target_pos, direction, initial_height)
        else:
            return 1
    return 0

max_score = 0

directions = [(-1, 0), (0, -1), (1, 0),  (0, 1)]

for row in range(len(heights)):
    for col in range(len(heights[row])):
        pos = (row, col)
        cur_height = heights[row][col]
        score = 1
        for dir in directions:
            distance_in_dir = viewing_distance(pos, dir, cur_height)
            score *= distance_in_dir
        if score > max_score:
            max_score = score

print(max_score)

