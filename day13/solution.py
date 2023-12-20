def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        
        above = above[:len(below)]
        below = below[:len(above)]
        
        if above == below:
            return r
        
    return 0

total = 0

for block in open("C:\\Users\\orhun\\OneDrive\\Documenten\\adventofcode\\Advent2023-1\\day13\\input.txt").read().split("\n\n"):
    grid = block.splitlines()

    row = find_mirror(grid)
    total += row * 100

    col = find_mirror(list(zip(*grid)))
    total += col

print(total)