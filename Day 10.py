import math

register = 1
cycle = 0
signal_strength_sum = 0
next_time_to_check = None


def increment_counter_and_check():
    global cycle, register, times_to_check, next_time_to_check
    if next_time_to_check is None:
        try:
            next_time_to_check = times_to_check.__next__()
        except:
            next_time_to_check = math.nan
    cycle += 1
    if next_time_to_check == cycle:
        signal_strength = cycle * register
        global signal_strength_sum
        signal_strength_sum += signal_strength
        next_time_to_check = None

with open('Day 10 input.txt') as file:
    global times_to_check
    times_to_check = iter(range(20, 240, 40))
    for line in file:
        if line.strip() == 'noop':
            increment_counter_and_check()
        else:
            increment_counter_and_check()
            increment_counter_and_check()
            (_, addend) = line.split()
            register += int(addend)

print(signal_strength_sum)

