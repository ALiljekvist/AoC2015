def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return [x.strip() for x in f.readlines() if x]
    except:
        return None

SCAN = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }

def part1(data):
    for sue in data:
        parts = sue.split(' ')
        things = [x.replace(':', '').replace(',', '') for x in parts[2:]]
        could_be = True
        for i in range(0, len(things), 2):
            if SCAN[things[i]] != int(things[i+1]):
                could_be = False
                break
        if not could_be:
            continue
        return int(parts[1][:-1])
    return -1

def part2(data):
    for sue in data:
        parts = sue.split(' ')
        things = [x.replace(':', '').replace(',', '') for x in parts[2:]]
        could_be = True
        for i in range(0, len(things), 2):
            match things[i]:
                case 'cats' | 'trees':
                    if SCAN[things[i]] >= int(things[i+1]):
                        could_be = False
                        break
                case 'pomeranians' | 'goldfish':
                    if SCAN[things[i]] <= int(things[i+1]):
                        could_be = False
                        break
                case _:
                    if SCAN[things[i]] != int(things[i+1]):
                        could_be = False
                        break
        if not could_be:
            continue
        return int(parts[1][:-1])
    return -1

if __name__ == '__main__':
    data = read_input('input.txt')
    print(part1(data))
    print(part2(data))
