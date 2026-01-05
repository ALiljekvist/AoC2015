def read_input(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except:
        return None

def increment(password, pos):
    if password[pos] == 'z':
        password = password[:pos] + 'a' + password[pos+1:]
        return increment(password, pos-1)
    password = password[:pos] + chr(ord(password[pos])+1) + password[pos+1:]
    return password

def check_valid(password):
    i = 0
    last_pair = -2
    ascending = False
    double_pair = False
    while i < len(password):
        if password[i] in 'iol':
            return False
        if i < len(password)-2:
            a, b, c = ord(password[i]), ord(password[i+1]), ord(password[i+2])
            if b == a+1 and c == b+1:
                ascending = True
        if i < len(password)-1:
            if last_pair < i-1 and password[i] == password[i+1]:
                if last_pair >= 0:
                    double_pair = True
                last_pair = i
        i += 1
    return ascending and double_pair

def find_new_password(data):
    new_pass = increment(data, len(data)-1)
    while not check_valid(new_pass):
        new_pass = increment(new_pass, len(new_pass)-1)
    return new_pass

if __name__ == '__main__':
    data = read_input('input.txt')
    new_pass = find_new_password(data)
    print(new_pass)
    print(find_new_password(new_pass))
