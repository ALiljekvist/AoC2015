def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except:
        return None

def all_combs(curr, ps, combs, num=None):
    if len(ps) < 1:
        scalar = 1
        for c in curr:
            scalar *= c
        if num is not None and num // scalar > 50:
            return
        combs.add(scalar)
        return
    curr.append(ps[0])
    all_combs(curr, ps[1:], combs, num)
    curr.pop()
    curr.append(1)
    all_combs(curr, ps[1:], combs, num)
    curr.pop()

def score_from_primes(primes, num=None):
    all_ps = []
    for k, v in primes.items():
        for _ in range(v):
            all_ps.append(k)
    combs = set()
    all_combs([], all_ps, combs, num)
    if num is not None:
        return sum([11 * c for c in combs])
    return sum([10 * c for c in combs])

def primes_up_to(k):
    if k < 2:
        return []
    primes = [2]
    i = 3
    while i < k:
        prime = True
        for j in range(3, i//2+1):
            if i % j == 0:
                prime = False
                break
        if prime:
            primes.append(i)
        i += 2
    return primes

def primes2hash(primes):
    return ','.join([f'{x}:{primes[x]}' for x in sorted(primes.keys()) if primes[x] != 0])

def find_least_combination(curr, primes, target, cache, min_num_in, p2=False):
    hashed = primes2hash(curr)
    if hashed in cache:
        return cache[hashed]
    num = 1
    for val, cnt in curr.items():
        for _ in range(cnt):
            num *= val
    if num > min_num_in:
        return min_num_in
    if p2:
        presents = score_from_primes(curr, num)
    else:
        presents = score_from_primes(curr)
    if presents >= target:
        cache[hashed] = num
        return num
    min_num = min_num_in
    for p in primes:
        curr[p] = curr.get(p, 0) + 1
        new_min = find_least_combination(curr, primes, target, cache, min_num, p2)
        curr[p] -= 1
        if new_min < min_num:
            min_num = new_min
    cache[hashed] = min_num
    return new_min

def part1(target):
    # Assumption that this can be done with primes less than 15
    primes = primes_up_to(15)
    cache = {}
    min_num = find_least_combination({}, primes, target, cache, target)
    return min_num

def part2(target):
    # Assumption that this can be done with primes less than 15
    primes = primes_up_to(15)
    cache = {}
    min_num = find_least_combination({}, primes, target, cache, target, p2=True)
    return min_num

if __name__ == '__main__':
    data = read_input('input.txt')
    print(part1(int(data)))
    print(part2(int(data)))
