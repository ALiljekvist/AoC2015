def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return [x.strip() for x in f.readlines() if x]
    except:
        return None

def connect_wiring(data):
    wiring = {}
    for connection in data:
        parts = connection.split(' -> ')
        wiring[parts[1]] = parts[0].split()
    return wiring

def get_input(wiring, val, cache):
    try:
        return int(val)
    except:
        return calculate_value(wiring, val, cache)

def calculate_value(wiring, val, cache):
    if val in cache:
        return cache[val]
    parts = wiring.get(val, [])
    signal = None
    match len(parts):
        case 0:
            print(f"{val} not in wiring")
            signal = -1
        case 1:
            # Direct
            signal = get_input(wiring, parts[0], cache)
        case 2:
            # NOT case
            x = get_input(wiring, parts[1], cache)
            signal = (~x) % 2**16
        case 3:
            # Other cases
            x, y = get_input(wiring, parts[0], cache), get_input(wiring, parts[2], cache)
            match parts[1]:
                case 'AND':
                    signal = x & y
                case 'OR':
                    signal = x | y
                case 'LSHIFT':
                    signal = (x << y) % 2**16
                case 'RSHIFT':
                    signal = x >> y
                case _:
                    print("WEIRD INSTUCTION with len 3", parts)
                    signal = -1
        case _:
            print("WEIRD INSTUCTION", parts)
            signal = -1
    cache[val] = signal
    return signal

if __name__ == '__main__':
    data = read_input('input.txt')
    wiring = connect_wiring(data)
    cache = {}
    print(calculate_value(wiring, 'a', cache))
    new_cache = {}
    new_cache['b'] = cache['a']
    print(calculate_value(wiring, 'a', new_cache))

