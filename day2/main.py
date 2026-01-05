def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return [x.strip() for x in f.readlines() if x]
    except:
        return None

def combs(parts):
    for i in range(len(parts)):
        for j in range(i+1, len(parts)):
            yield (parts[i], parts[j])

def part1(data):
    tot = 0
    for gift in data:
        area = 0
        sides = [int(s) for s in gift.split('x')]
        areas = [s1*s2 for s1, s2 in combs(sides)]
        area = sum([2*a for a in areas]) + min(areas)
        tot += area
    return tot

def part2(data):
    tot = 0
    for gift in data:
        sides = [int(s) for s in gift.split('x')]
        volume = 1
        for s in sides:
            volume *= s
        tot += volume + min([2*(s1+s2) for s1, s2 in combs(sides)])
    return tot

if __name__ == '__main__':
    data = read_input('input.txt')
    # data = read_input('example.txt')
    print(part1(data))
    print(part2(data))
