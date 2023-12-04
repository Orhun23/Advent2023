m = {} 

for i, x in enumerate(open("C:\\Users\\orhun\\OneDrive\\Documenten\\adventofcode\\Advent2023-1\\day4\\input.txt")):
    if i not in m: 
        m[i] = 1
    x = x.split(":")[1].strip()
    a, b = [list(map(int,k.split())) for k in x.split(" | ")] 
    print(a, b)
    j = sum(q in a for q in b)

    for n in range (i + 1, i + j+1):
        m[n] = m.get(n, 1) + m[i]

print(sum(m.values()))