times, distances = [list(map(int, ["".join(line.split(":")[1].split())])) for line in open("C:\\Users\\OrhunErdogan\\.vscode\\adventOfCode2023\\Advent2023\\day6\\input.txt")]

n = 1

for time, distance in zip(times, distances):
    margin = 0
    for hold in range(time):
        if hold * (time - hold) > distance:
            margin += 1
    n *= margin

print(n)