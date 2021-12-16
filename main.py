# def find_bracket(string):
#     count = 0
#     while True:
#         if '(' not in string and ')' not in string:
#             return False
#         if list(string)[0] == ')':
#             return False
#         if list(string)[-1] == '(':
#             return False
#         for elem in string:
#             if elem == '(':
#                 count += 1
#             if elem == ')':
#                 count -= 1
#         if count == 0:
#             return True
#         else:
#             return False
# print(find_bracket(str(input('Enter your string: '))))


def find_bracket(string):
    list_elem=[]
    b = []
    if '(' not in string and ')' not in string:
        return False
    for elem in string:
        if elem == '(':
            b.append('(')
        if elem == ')':
            b.append(')')
    a = ''.join(b)
    # print(a)
    for i in range(0, len(a)):
        if a[i] == '(':
            list_elem.append('(')
            # print(1)
        elif a[i] == ')':
            # print(list_elem)
            if not list_elem:
                # print('hhhh')
                return False
            else:
                list_elem.pop()
    if not list_elem:
        return True
    else:
        return False
print(find_bracket(str(input('Enter your string: '))))



