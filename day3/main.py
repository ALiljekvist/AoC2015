def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return [x.strip() for x in f.read() if x]
    except:
        return None

def part1(directions):
    x, y = 0, 0
    houses = {(x,y): 1}
    for d in directions:
        match d:
            case '^':
                y += 1
                houses[(x,y)] = houses.get((x,y), 0) + 1
            case '>':
                x += 1
                houses[(x,y)] = houses.get((x,y), 0) + 1
            case 'v':
                y -= 1
                houses[(x,y)] = houses.get((x,y), 0) + 1
            case '<':
                x -= 1
                houses[(x,y)] = houses.get((x,y), 0) + 1
    return len(houses.keys())

def part2(directions):
    positions = [(0,0), (0,0)]
    houses = {(0,0): 2}
    for i, d in enumerate(directions):
        x, y = positions[i%2]
        match d:
            case '^':
                y += 1
                houses[(x,y)] = houses.get((x,y), 0) + 1
            case '>':
                x += 1
                houses[(x,y)] = houses.get((x,y), 0) + 1
            case 'v':
                y -= 1
                houses[(x,y)] = houses.get((x,y), 0) + 1
            case '<':
                x -= 1
                houses[(x,y)] = houses.get((x,y), 0) + 1
        positions[i%2] = (x,y)
    return len(houses.keys())

if __name__ == '__main__':
    data = read_input('input.txt')
    print(part1(data))
    print(part2(data))