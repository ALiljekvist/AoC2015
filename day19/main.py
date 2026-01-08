def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return [x.strip() for x in f.readlines() if x.strip()]
    except:
        return None

def parse_replacements(data):
    replacements = {}
    for row in data:
        parts = row.split(' => ')
        x, y = parts[0], parts[1]
        replacements[x] = replacements.get(x, [])
        replacements[x].append(y)
    return replacements

def find(source, sub):
    inds = []
    i = 0
    while i + len(sub) < len(source):
        if source[i:i+len(sub)] == sub:
            inds.append(i)
        i += 1
    return inds

def part1(original, replacements):
    all_molecules = set()
    for fr, tos in replacements.items():
        for i in find(original, fr):
            for to in tos:
                new_molecule = original[:i] + to + original[i+len(fr):]
                all_molecules.add(new_molecule)
    return len(all_molecules)

def reduce_to_electron(molecule, replacements, cache):
    if molecule == 'e':
        return 0
    if molecule in cache:
        return cache[molecule]
    min_reduces = 100000000000
    for fr, to in replacements.items():
        for i in find(molecule, fr):
            new_molecule = original[:i] + to[0] + original[i+len(fr):]
            reduced = 1 + reduce_to_electron(new_molecule, replacements, cache)
            if reduced < min_reduces:
                min_reduces = reduced
    cache[molecule] = min_reduces
    return min_reduces

def part2(target, replacements):
    start = 'e'
    return -1

if __name__ == '__main__':
    data = read_input('input.txt')
    replacements = parse_replacements(data[:-1])
    original = data[-1]
    print(part1(original, replacements))
