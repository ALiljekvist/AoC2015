def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return [x.strip() for x in f.readlines() if x.strip()]
    except:
        return None

def parse_boss_stats(data):
    boss = {}
    for line in data:
        parts = line.split(': ')
        match parts[0]:
            case 'Hit Points':
                val = 'hp'
            case 'Damage':
                val = 'dmg'
        boss[val] = int(parts[1])
    return boss

MANACOST = [53, 73, 113, 173, 229]

def fight(turn, player, boss, mana_spent, min_mana_spent, hist, p2=False):
    # Check if we're less effective than previous best
    if mana_spent > min_mana_spent:
        return min_mana_spent
    if p2 and turn % 2 == 0:
        player['hp'] -= 1
    # Check if player has died, return previous best
    if player['hp'] < 1:
        return min_mana_spent
    # Chech if boss has died
    if boss['hp'] < 1:
        return mana_spent
    # Apply any active effects
    if player['recharge'] > 0:
        player['mana'] += 101
    player['recharge'] -= 1
    if player['poison'] > 0:
        boss['hp'] -= 3
    player['poison'] -= 1
    arm = 0
    if player['shield'] > 0:
        arm = 7
    player['shield'] -= 1
    # Check if boss died of poison
    if boss['hp'] < 1:
        return mana_spent

    new_min = min_mana_spent
    if turn % 2 == 1:
        # Boss turn
        updated_player = player.copy()
        updated_player['hp'] -= (boss['dmg'] - arm)
        spent = fight(turn+1, updated_player, boss, mana_spent, min_mana_spent, hist, p2)
        if spent < new_min:
            new_min = spent
        return new_min
    else:
        # Player turn
        for i in range(5):
            updated_player = player.copy()
            updated_boss = boss.copy()
            cost = MANACOST[i]
            if updated_player['mana'] < cost:
                break
            match i:
                case 0: # Magic Missile
                    updated_boss['hp'] -= 4
                    updated_player['mana'] -= cost
                    hist.append(0)
                    spent = fight(turn+1, updated_player, updated_boss, mana_spent + cost, new_min, hist, p2)
                    if spent < new_min:
                        new_min = spent
                    hist.pop()
                case 1: # Drain
                    updated_boss['hp'] -= 2
                    updated_player['hp'] += 2
                    updated_player['mana'] -= cost
                    hist.append(1)
                    spent = fight(turn+1, updated_player, updated_boss, mana_spent + cost, new_min, hist, p2)
                    if spent < new_min:
                        new_min = spent
                    hist.pop()
                case 2: # Shield
                    if updated_player['shield'] > 0:
                        # Not enough mana or effect already active
                        continue
                    updated_player['shield'] = 6
                    updated_player['mana'] -= cost
                    hist.append(2)
                    spent = fight(turn+1, updated_player, updated_boss, mana_spent + cost, new_min, hist, p2)
                    if spent < new_min:
                        new_min = spent
                    hist.pop()
                case 3: # Poison
                    if updated_player['poison'] > 0:
                        # Not enough mana or effect already active
                        continue
                    updated_player['poison'] = 6
                    updated_player['mana'] -= cost
                    hist.append(3)
                    spent = fight(turn+1, updated_player, updated_boss, mana_spent + cost, new_min, hist, p2)
                    if spent < new_min:
                        new_min = spent
                    hist.pop()
                case 4: # Recharge
                    if updated_player['recharge'] > 0:
                        # Not enough mana or effect already active
                        continue
                    updated_player['recharge'] = 5
                    updated_player['mana'] -= cost
                    hist.append(4)
                    spent = fight(turn+1, updated_player, updated_boss, mana_spent + cost, new_min, hist, p2)
                    if spent < new_min:
                        new_min = spent
                    hist.pop()
    return new_min

def part1(boss):
    player = {'hp': 50, 'mana': 500, 'shield': -1, 'poison': -1, 'recharge': -1}
    return fight(0, player, boss, 0, 10000000000000000, [])

def part2(boss):
    player = {'hp': 50, 'mana': 500, 'shield': -1, 'poison': -1, 'recharge': -1}
    return fight(0, player, boss, 0, 10000000000000000, [], p2=True)

if __name__ == '__main__':
    data = read_input('input.txt')
    boss = parse_boss_stats(data)
    print(part1(boss))
    print(part2(boss))
