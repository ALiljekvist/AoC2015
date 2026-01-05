import hashlib

def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except:
        return None

# TODO: Replace with own implementation for MD5

def part1(data):
    i = 1
    while True:
        key = data + str(i)
        hashed = hashlib.md5(key.encode()).hexdigest()
        if hashed.startswith('00000'):
            return i
        i += 1

def part2(data):
    i = 1
    while True:
        key = data + str(i)
        hashed = hashlib.md5(key.encode()).hexdigest()
        if hashed.startswith('000000'):
            return i
        i += 1

if __name__ == '__main__':
    data = read_input('input.txt')
    print(part1(data))
    print(part2(data))