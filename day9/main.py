def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return [x.strip() for x in f.readlines() if x]
    except:
        return None

def parse_distances(data):
    dists = {}
    for pair in data:
        parts = pair.split(' ')
        dist = int(parts[-1])
        a_dists = dists.get(parts[0], [])
        a_dists.append((parts[2], dist))
        dists[parts[0]] = a_dists
        b_dists = dists.get(parts[2], [])
        b_dists.append((parts[0], dist))
        dists[parts[2]] = b_dists
    return dists

def insert_queue(item, queue, comp_func):
    i = 0
    while i < len(queue) and comp_func(queue[i], item):
        i += 1
    queue.insert(i, item)

def find_shortest_path(dists, comp_func=lambda x, y: x[0] < y[0]):
    target = len(dists.keys())
    queue = [(0, [s]) for s in list(dists.keys())]
    while queue:
        steps, hist = queue.pop(0)
        if len(hist) == target:
            return steps
        curr = hist[-1]
        for (dest, new_steps) in dists[curr]:
            if dest in hist:
                continue
            updated = hist.copy()
            updated.append(dest)
            insert_queue((steps+new_steps, updated), queue, comp_func)
    return -1

def part1(dists):
    return find_shortest_path(dists)

def part2(dists):
    return find_shortest_path(dists, comp_func=lambda x, y: x[0] > y[0])

if __name__ == '__main__':
    data = read_input('input.txt')
    dists = parse_distances(data)
    print(part1(dists))
    print(part2(dists))
