def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return [x.strip() for x in f.readlines() if x]
    except:
        return None

def count_chars(word: str):
    count = 0
    # All words are encased by "", so only count the inner ones
    i = 1
    while i < len(word)-1:
        if word[i] == '\\':
            match word[i+1]:
                # ASCII
                case 'x':
                    i += 4
                    count +=1
                # Other scpecial character
                case _:
                    i += 2
                    count += 1
            continue
        count += 1
        i += 1
    return count

def part1(data):
    return sum([len(word)-count_chars(word) for word in data])

def encode(word:str):
    encoded = '\"'
    for i in range(len(word)):
        if word[i].isalnum():
            encoded += word[i]
        else:
            encoded += f"\\{word[i]}"
    encoded += '\"'
    return encoded

def part2(data):
    return sum([len(encode(word))-len(word) for word in data])

if __name__ == '__main__':
    data = read_input('input.txt')
    print(part1(data))
    print(part2(data))
