def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return [x.strip() for x in f.readlines() if x.strip()]
    except:
        return None

WEAPONS = [
    ('Dagger', 8, 4, 0),
    ('Shortsword', 10, 5, 0),
    ('Warhammer', 25, 6, 0),
    ('Longsword', 40, 7, 0),
    ('Greataxe', 74, 8, 0),
]

ARMOR  = [
    ('Leather', 13, 0, 1),
    ('Chainmail', 31, 0, 2),
    ('Splintmail', 53, 0, 3),
    ('Bandemail', 75, 0, 4),
    ('Platemail', 102, 0, 5),
]

RINGS = [
    ('Damage +1', 25, 1, 0),
    ('Damage +2', 50, 2, 0),
    ('Damage +3', 100, 3, 0),
    ('Defense +1', 20, 0, 1),
    ('Defense +2', 40, 0, 2),
    ('Defense +3', 80, 0, 3),
]

def parse_boss_stats(data):
    boss = {}
    for line in data:
        parts = line.split(': ')
        match parts[0]:
            case 'Hit Points':
                val = 'hp'
            case 'Damage':
                val = 'dmg'
            case 'Armor':
                val = 'arm'
        boss[val] = int(parts[1])
    return boss

def fight(player, boss):
    if player['dmg'] <= boss['arm']:
        return False
    if boss['dmg'] <= player['arm']:
        return True
    p_turns = boss['hp'] // (player['dmg'] - boss['arm'])
    if boss['hp'] % (player['dmg'] - boss['arm']) != 0:
        p_turns += 1
    b_turns = player['hp'] // (boss['dmg'] - player['arm'])
    if player['hp'] % (boss['dmg'] - player['arm']) != 0:
        b_turns += 1
    return b_turns >= p_turns

def choose_max_2(alternatives):
    combs = []
    for i in range(len(alternatives)):
        combs.append([alternatives[i]])
        for j in range(i+1, len(alternatives)):
            combs.append([alternatives[i], alternatives[j]])
    return combs

def buy_all_the_things(things, combs):
    if 'weapon' not in things:
        for weapon in WEAPONS:
            things['weapon'] = weapon
            buy_all_the_things(things, combs)
            things.pop('weapon')
        return
    # Try with just the weapon
    combs.append(things.copy())
    if 'armor' not in things:
        things['armor'] = ('None', 0, 0, 0)
        buy_all_the_things(things, combs)
        things.pop('armor')
        for armor in ARMOR:
            things['armor'] = armor
            buy_all_the_things(things, combs)
            things.pop('armor')
        return
    ring_alternatives = choose_max_2(RINGS)
    for alt in ring_alternatives:
        to_remove = []
        for i in range(len(alt)):
            thing = f'ring{i+1}'
            to_remove.append(thing)
            things[thing] = alt[i]
        combs.append(things.copy())
        for thing in to_remove:
            things.pop(thing)
    return

def part1(boss):
    combs = []
    buy_all_the_things({}, combs)
    combs.sort(key=lambda c: sum([v[1] for _, v in c.items()]))
    for comb in combs:
        cost = sum([v[1] for _, v in comb.items()])
        player = {
            'hp': 100,
            'dmg': sum([v[2] for _, v in comb.items()]),
            'arm': sum([v[3] for _, v in comb.items()]),
        }
        if fight(player, boss):
            return cost
    return -1

def part2(boss):
    combs = []
    buy_all_the_things({}, combs)
    combs.sort(key=lambda c: sum([v[1] for _, v in c.items()]), reverse=True)
    for comb in combs:
        cost = sum([v[1] for _, v in comb.items()])
        player = {
            'hp': 100,
            'dmg': sum([v[2] for _, v in comb.items()]),
            'arm': sum([v[3] for _, v in comb.items()]),
        }
        if not fight(player, boss):
            return cost
    return -1

if __name__ == '__main__':
    data = read_input('input.txt')
    boss = parse_boss_stats(data)
    print(part1(boss))
    print(part2(boss))
