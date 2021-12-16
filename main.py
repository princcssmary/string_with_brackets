def find_bracket(string):
    count = 0
    while True:
        if '(' not in string and ')' not in string:
            return False
        if list(string)[0] == ')':
            return False
        for elem in string:
            if elem == '(':
                count += 1
            if elem == ')':
                count -= 1
        if count == 0:
            return True
        else:
            return False
print(find_bracket(str(input('Enter your string: '))))