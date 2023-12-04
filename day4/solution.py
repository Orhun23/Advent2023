t = 0 

for x in open("C:\\Users\\orhun\\OneDrive\\Documenten\\adventofcode\\Advent2023-1\\day4\\input.txt"):
    x = x.split(":")[1].strip()
    a, b = [list(map(int,k.split())) for k in x.split(" | ")] 
    print(a, b)
    j = sum(q in a for q in b)
    if j > 0: 
        t += 2**(j-1) 

print(t)