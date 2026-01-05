def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return [x.strip() for x in f.readlines() if x]
    except:
        return None

class Reindeer:
    def __init__(self, name, speed, burst, rest):
        self.name = name
        self.speed = speed
        self.burst = burst
        self.rest = rest
        self.time = 0
        self.traveled = 0
    
    def travel(self, duration):
        periods = duration // (self.burst + self.rest)
        dist_traveled = self.speed * self.burst * periods
        time_left = duration % (self.burst + self.rest)
        dist_traveled += self.speed * min(self.burst, time_left)
        return dist_traveled

    def move(self):
        if self.time < self.burst:
            self.traveled += self.speed
        self.time = (self.time + 1) % (self.burst + self.rest)

    def pos(self):
        return self.traveled

def map_reindeers(data):
    reindeers = []
    for deer in data:
        parts = deer.split(' ')
        reindeers.append(Reindeer(parts[0], int(parts[3]), int(parts[6]), int(parts[-2])))
    return reindeers

def part1(reindeers, seconds=2503):
    return max([deer.travel(seconds) for deer in reindeers])

def part2(reindeers, seconds=2503):
    score = [0 for _ in range(len(reindeers))]
    for _ in range(seconds):
        max_inds = []
        furthest = 0
        for i, deer in enumerate(reindeers):
            deer.move()
            if deer.pos() > furthest:
                max_inds = [i]
                furthest = deer.pos()
            elif deer.pos() == furthest:
                max_inds.append(i)
        for i in max_inds:
            score[i] += 1
    return max(score)

if __name__ == '__main__':
    data = read_input('input.txt')
    reindeers = map_reindeers(data)
    print(part1(reindeers))
    print(part2(reindeers))
