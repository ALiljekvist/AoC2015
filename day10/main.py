def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except:
        return None

def look_and_say(number):
    new_number = ''
    i = 0
    while i < len(number):
        j = i
        while j < len(number) and number[i] == number[j]:
            j += 1
        new_number += f"{j-i}{number[i]}"
        i = j
    return new_number

def part1(data):
    num = data
    for _ in range(40):
        num = look_and_say(num)
    return len(num)

def part2(data):
    num = data
    for _ in range(50):
        num = look_and_say(num)
    return len(num)

if __name__ == '__main__':
    data = read_input('input.txt')
    print(part1(data))
    print(part2(data))