t = 0 


for i, x in enumerate(open("C:\\Users\\orhun\\OneDrive\\Documenten\\adventofcode\\Advent2023\\day2\\in.txt")):
    groups = x.strip().split(": ")[1].split("; ") 
    for o in groups:
        colors = {"red" :0, "green":0, "blue":0}
        for z in o.split(", "):
            a,b = z.split()
            colors[b] = int(a) 
        if colors["red"] > 12 or colors["blue"] > 14 or colors["green"] > 13:
            break

    else:
        t += i + 1
       
print(t)
# this also works for the first part 
# i have already solved it so dont want to do it again 