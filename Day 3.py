filename = 'Day 3 input.txt'
score = 0
with open(filename) as file:
    total_shared_item_values = 0
    for line in file:
        line = line.strip()
        compartment_size = int(len(line) / 2)
        comp_1_items = {x for x in line[:compartment_size]}
        comp_2_items = {x for x in line[compartment_size:]}
        (shared_item, ) = comp_1_items & comp_2_items
        shared_item_value = ord(shared_item) - ord('A')
        if shared_item_value > 32: # lower-case
            shared_item_value -= 31
        else:
            shared_item_value += 27
        total_shared_item_values += shared_item_value

    print(total_shared_item_values)

