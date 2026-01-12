def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except:
        return None

def part1(data):
    parts = data.split(' ')
    row = int(''.join([x for x in parts[-3] if x in '0123456789']))
    col = int(''.join([x for x in parts[-1] if x in '0123456789']))
    mult = 252533
    rem = 33554393
    val = 20151125
    num = r = c = 1
    # Find the number by moving along the rows and cols
    # adding all the new numbers in the diagonal crossed
    # for each step.
    while r != row:
        num += r
        r += 1
    while c != col:
        num += r + c
        c += 1
    # Found the number, not we just need to perform all the
    # multiplications and modulos
    for _ in range(1, num):
        val = (val * mult) % rem
    return val

if __name__ == '__main__':
    data = read_input('input.txt')
    print(part1(data))
