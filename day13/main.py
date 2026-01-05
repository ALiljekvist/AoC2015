import itertools

def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return [x.strip() for x in f.readlines() if x]
    except:
        return None

def parse_relations(data):
    people = list(set([rel.split(' ')[0] for rel in data]))
    people.sort()
    relations = [[0 for _ in range(len(people))] for _ in range(len(people))]
    for rel in data:
        parts = rel.split(' ')
        mult = -1 if parts[2] == 'lose' else 1
        score = int(parts[3])
        p1 = parts[0]
        p2 = parts[-1][:-1]
        i1 = people.index(p1)
        i2 = people.index(p2)
        relations[i1][i2] = score * mult
        pass
    return people, relations

def calc_happines(seating, relations):
    n = len(relations)
    return sum([relations[s][seating[(i-1)%n]] + relations[s][seating[(i+1)%n]] for i, s in enumerate(seating)])

def find_max_happiness(people, relations):
    max_happiness = 0
    for seating in itertools.permutations([i for i in range(len(people))]):
        happiness = calc_happines(seating, relations)
        if happiness > max_happiness:
            max_happiness = happiness
    return max_happiness

if __name__ == '__main__':
    data = read_input('input.txt')
    # Part 1, create relationship matrix and try out all combinations
    people, relations = parse_relations(data)
    print(find_max_happiness(people, relations))
    # Part 2, add self into the people and relations and redo part 1
    people.append('Me')
    for rel in relations:
        rel.append(0)
    relations.append([0 for _ in range(len(people))])
    print(find_max_happiness(people, relations))
