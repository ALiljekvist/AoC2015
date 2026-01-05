def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except:
        return None

def find_numbers(data):
    nums = []
    val = ''
    for v in data:
        if v in '-0123456789':
            val += v
            continue
        else:
            if val != '':
                nums.append(int(val))
            val = ''
    return nums

def part1(data: str):
    return sum(find_numbers(data))

def sum_numbers_not_red(data, i, layer_type, f):
    nums = []
    val = ''
    ind = i
    counts = True
    if layer_type == 0:
        level = 0
        while ind < len(data):
            if data[ind] == 'r' and ind < len(data)-3:
                if data[ind:ind+3] == 'red' and level == 0:
                    counts = False
            if data[ind] == '{' or data[ind] == '[':
                level += 1
            if data[ind] == '}' or data[ind] == ']':
                if level == 0:
                    break
                level -= 1
            ind += 1
    if not counts:
        return 0, ind+1

    # Not in red layer
    while i < len(data):
        v = data[i]
        if v in '-0123456789':
            val += v
            i += 1
        else:
            match v:
                case '}':
                    if layer_type != 0:
                        print("Found object end in list layer")
                        quit()
                    break
                case ']':
                    if layer_type != 1:
                        print("Found list end in object layer")
                        quit()
                    break
                case '{':
                    val, i = sum_numbers_not_red(data, i+1, 0, f+1)
                    nums.append(val)
                    val = ''
                case '[':
                    val, i = sum_numbers_not_red(data, i+1, 1, f+1)
                    nums.append(val)
                    val = ''
                case _:
                    i += 1
            if val != '':
                nums.append(int(val))
            val = ''

    if val != '':
        nums.append(int(val))

    return sum(nums), i + 1

def part2(data):
    layer_type = 1
    if data[0] == '{':
        layer_type = 0
    tot, i = sum_numbers_not_red(data, 1, False, layer_type)
    if i != len(data):
        print("Did not cover all sequences")
    return tot

if __name__ == '__main__':
    data = read_input('input.txt')
    print(part1(data))
    print(part2(data))
