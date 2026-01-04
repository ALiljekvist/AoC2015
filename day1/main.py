def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return [x.strip() for x in f.read() if x]
    except:
        return None

def part1(data):
    return sum([1 if s == '(' else -1 for s in data])

def part2(data):
    floor = 0
    i = 0
    while floor != -1:
        floor += 1 if data[i] == '(' else -1
        i += 1
    return i

if __name__ == '__main__':
    data = read_input('input.txt')
    print(part1(data))
    print(part2(data))
