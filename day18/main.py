def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return [x.strip() for x in f.readlines() if x]
    except:
        return None

def parse_grid(data):
    grid = {}
    for r, row in enumerate(data):
        for c, light in enumerate(row):
            if light != '#':
                continue
            grid[(r,c)] = 1
    return grid

NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def animate(grid):
    new_grid = {}
    for r in range(100):
        for c in range(100):
            match sum([grid.get((r+dr, c+dc), 0) for (dr, dc) in NEIGHBORS]):
                case 3:
                    new_grid[(r,c)] = 1
                case 2:
                    if (r,c) in grid:
                        new_grid[(r,c)] = 1
    return new_grid 

def part1(grid):
    for _ in range(100):
        grid = animate(grid)
    return len(grid)

def part2(grid):
    for _ in range(100):
        grid[(0,0)] = 1
        grid[(99,0)] = 1
        grid[(0,99)] = 1
        grid[(99,99)] = 1
        grid = animate(grid)
    grid[(0,0)] = 1
    grid[(99,0)] = 1
    grid[(0,99)] = 1
    grid[(99,99)] = 1
    return len(grid)

if __name__ == '__main__':
    data = read_input('input.txt')
    grid = parse_grid(data)
    print(part1(grid.copy()))
    print(part2(grid))
