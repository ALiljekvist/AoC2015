def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return [x.strip() for x in f.readlines() if x]
    except:
        return None

def part1(instructions):
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for i in instructions:
        parts = i.split(' ')
        try:
            r,c = [int(x) for x in parts[2].split(',')]
        except:
            r,c = [int(x) for x in parts[1].split(',')]
        re,ce = [int(x) for x in parts[-1].split(',')]
        for ri in range(r, re+1):
            for ci in range(c, ce+1):
                if i.startswith("turn on"):
                    lights[ri][ci] = 1
                elif i.startswith("turn off"):
                    lights[ri][ci] = 0
                else:
                    lights[ri][ci] = (lights[ri][ci] + 1) % 2
    return sum([sum(row) for row in lights])

def part2(data):
    
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for i in instructions:
        parts = i.split(' ')
        try:
            r,c = [int(x) for x in parts[2].split(',')]
        except:
            r,c = [int(x) for x in parts[1].split(',')]
        re,ce = [int(x) for x in parts[-1].split(',')]
        for ri in range(r, re+1):
            for ci in range(c, ce+1):
                if i.startswith("turn on"):
                    lights[ri][ci] += 1
                elif i.startswith("turn off"):
                    lights[ri][ci] -= 1
                    if lights[ri][ci] < 0:
                        lights[ri][ci] = 0
                else:
                    lights[ri][ci] += 2
    return sum([sum(row) for row in lights])

if __name__ == '__main__':
    instructions = read_input('input.txt')
    print(part1(instructions))
    print(part2(instructions))
