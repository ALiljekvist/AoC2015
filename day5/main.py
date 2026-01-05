def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return [x.strip() for x in f.readlines() if x]
    except:
        return None

def is_nice(word):
    if 'ab' in word:
        return 0
    if 'cd' in word:
        return 0
    if 'pq' in word:
        return 0
    if 'xy' in word:
        return 0
    if not any([x == y for x, y in zip(word, word[1:])]):
        return 0
    if sum([1 if s in 'aeiou' else 0 for s in word]) < 3:
        return 0
    return 1

def part1(data):
    return sum([is_nice(word) for word in data])

def is_nicer(word):
    found_match = False
    for i in range(len(word)-1):
        for j in range(i+2, len(word)-1):
            if word[i:i+2] == word[j:j+2]:
                found_match = True
                break
    if not found_match:
        return 0
    found_match = False
    for i in range(len(word)-2):
        if word[i] == word[i+2]:
            found_match = True
            break
    if not found_match:
        return 0
    return 1

def part2(data):
    return sum([is_nicer(word) for word in data])

if __name__ == '__main__':
    data = read_input('input.txt')
    print(part1(data))
    print(part2(data))
