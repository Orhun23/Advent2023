import math
import re
from collections import defaultdict

with open("C:\\Users\\OrhunErdogan\\.vscode\\adventOfCode2023\\Advent2023\\day2\\in.txt") as f:
    ls = f.read().strip().split("\n")


good_ids = 0
total_power = 0
for l in ls:
    parts = re.sub("[;,:]", "", l).split()
    colormax = defaultdict(int)
    for count, color in zip(parts[2::2], parts[3::2]):
        colormax[color] = max(colormax[color], int(count))
    power = math.prod(colormax.values())
    if colormax["red"] <= 12 and colormax["green"] <= 13 and colormax["blue"] <= 14:
        good_ids += int(parts[1])
    total_power += power

# part 1 answer 
print(good_ids)

#part 2 answer
print(total_power)