def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return [x.strip() for x in f.readlines() if x.strip()]
    except:
        return None

def run(data, a_start=0):
    a, b = a_start, 0
    i = 0
    while i < len(data):
        op = data[i]
        match op[:3]:
            case 'hlf':
                if op[-1] == 'a':
                    a = a // 2
                else:
                    b = b // 2
                i += 1
            case 'tpl':
                if op[-1] == 'a':
                    a = a * 3
                else:
                    b = b * 3
                i += 1
            case 'inc':
                if op[-1] == 'a':
                    a += 1
                else:
                    b += 1
                i += 1
            case 'jmp':
                offset = int(op.split(' ')[-1])
                i += offset
            case 'jie':
                parts = op.split(',')
                offset = int(parts[-1])
                if parts[0][-1] == 'a':
                    reg = a
                else:
                    reg = b
                if reg % 2 == 0:
                    i += offset
                else:
                    i += 1
            case 'jio':
                parts = op.split(',')
                offset = int(parts[-1])
                if parts[0][-1] == 'a':
                    reg = a
                else:
                    reg = b
                if reg == 1:
                    i += offset
                else:
                    i += 1
    return b

if __name__ == '__main__':
    data = read_input('input.txt')
    print(run(data))
    print(run(data, a_start=1))
