numbers = {
    'one': '1', 'two': '2', 'three': '3', 
    'four': '4', 'five': '5', 'six': '6',
    'seven': '7', 'eight': '8', 'nine': '9'
}

def find_nums(line, part_two):
    found = []
    for k, v in numbers.items():
        fnd = [i for i in range(len(l)) if l.startswith(v, i)]
        for i in fnd: 
            found.append([v, i])
        if part_two:
            fnd_two = [i for i in range(len(l)) if l.startswith(k, i)]
            for i in fnd_two:
                found.append([v, i])
    return found

with open('input.txt') as f:
    lines = f.read().split('\n')
    nums, results = [], []

    for l in lines:
        found = find_nums(l, True)
        print(found)
        found_sorted = sorted(found, key=lambda x: x[1])
        nums = [v[0] for v in found_sorted]
        try:
            num = nums[0] + nums[-1]
        except: continue
        results.append(num)

    #results
    print(sum(list(map(int, results))))