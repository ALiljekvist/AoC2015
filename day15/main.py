import re

class Ingredient():
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)
    
    def score(self, amount):
        return [amount * x for x in [self.capacity, self.durability, self.flavor, self.texture]]

def parse_ingredient(raw: str) -> Ingredient:
    name = raw.split(':')[0]
    info = list(re.findall('-?\\d', raw))
    return Ingredient(name, info[0], info[1], info[2], info[3], info[4])

def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return [parse_ingredient(x.strip()) for x in f.readlines() if x]
    except:
        return None

def score(ingredients, amount):
    scores = [0 for _ in range(4)]
    for i, c in enumerate(amount):
        to_add = ingredients[i].score(c)
        for j, a in enumerate(to_add):
            scores[j] += a
    if any([s <= 0 for s in scores]):
        return 0
    tot_score = 1
    for s in scores:
        tot_score *= s
    return tot_score

def try_combination(ingredients, chosen, left, extra_requirement=None):
    if len(chosen) >= len(ingredients)-1:
        chosen.append(left)
        if extra_requirement is not None and not extra_requirement(ingredients, chosen):
            chosen.pop()
            return 0
        new_score = score(ingredients, chosen)
        chosen.pop()
        return new_score
    max_score = 0
    for i in range(left):
        chosen.append(i)
        new_score = try_combination(ingredients, chosen, left-i, extra_requirement=extra_requirement)
        if new_score > max_score:
            max_score = new_score
        chosen.pop()
    return max_score

def part1(ingredients):
    return try_combination(ingredients, [], 100)

def max_calorie_limit(ingredients, amounts):
    return sum([ingredients[i].calories * amounts[i] for i in range(len(amounts))]) == 500

def part2(ingredients):
    return try_combination(ingredients, [], 100, extra_requirement=max_calorie_limit)

if __name__ == '__main__':
    data = read_input('input.txt')
    # data = read_input('example.txt')
    print(part1(data))
    print(part2(data))
