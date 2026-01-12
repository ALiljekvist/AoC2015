def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return [int(x.strip()) for x in f.readlines() if x.strip()]
    except:
        return None

def find_smallest_package_groups(curr, packages, target, combs):
    if sum(curr) > target:
        return
    if len(combs) > 0 and len(curr) > min([len(c) for c in combs]):
        return
    if sum(curr) == target:
        combs.append(curr.copy())
        return
    for i, p in enumerate(packages):
        curr.append(p)
        find_smallest_package_groups(curr, packages[i+1:], target, combs)
        curr.pop()
    return

def quantum_entanglement(comb):
    entanglement = 1
    for c in comb:
        entanglement *= c
    return entanglement

def part1(packages):
    packages.sort(reverse=True)
    tot = sum(packages)
    combs = []
    find_smallest_package_groups([], packages, tot//3, combs)
    combs = [c for c in combs if len(c) == min([len(ci) for ci in combs])]
    return min([quantum_entanglement(comb) for comb in combs])

def part2(packages):
    packages.sort(reverse=True)
    tot = sum(packages)
    combs = []
    find_smallest_package_groups([], packages, tot//4, combs)
    combs = [c for c in combs if len(c) == min([len(ci) for ci in combs])]
    return min([quantum_entanglement(comb) for comb in combs])

if __name__ == '__main__':
    packages = read_input('input.txt')
    print(part1(packages))
    print(part2(packages))
