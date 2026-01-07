def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return [int(x.strip()) for x in f.readlines() if x]
    except:
        return None

def fill_containers(containers, left):
    if left == 0:
        return 1
    if len(containers) == 0:
        return 0
    tot = 0
    for i, vol in enumerate(containers):
        if vol > left:
            break
        tot += fill_containers(containers[i+1:], left-vol)
    return tot

AMOUNT = 150

def part1(containers):
    return fill_containers(containers, AMOUNT)

def find_least_amount(containers, chosen):
    if sum(chosen) == AMOUNT:
        return len(chosen)
    if sum(chosen) > AMOUNT:
        return None
    for i, val in enumerate(containers):
        chosen.append(val)
        res = find_least_amount(containers[i+1:], chosen)
        if res is not None:
            return res
        chosen.pop()
    return None

def count_x_containers(containers, chosen, x):
    if len(chosen) == x:
        if sum(chosen) != AMOUNT:
            return 0
        return 1
    tot = 0
    for i, val in enumerate(containers):
        chosen.append(val)
        part = count_x_containers(containers[i+1:], chosen, x)
        chosen.pop()
        tot += part
    return tot

def part2(containers):
    containers.sort(reverse=True)
    for x in range(1, len(containers)):
        res = count_x_containers(containers, [], x)
        if res != 0:
            return res
    return -1

if __name__ == '__main__':
    containers = read_input('input.txt')
    containers.sort()
    print(part1(containers))
    print(part2(containers))
