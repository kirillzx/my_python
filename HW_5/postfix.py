
def calc(expr):
    '''
    >>> calc("1 2 + 4 * 3 +")
    '15'
    >>> calc("1 2 3 * + 2 -")
    '5'
    '''

    stack=[]
    for i in expr:
        if i.isdigit():
            stack.append(int(i))
        elif i == '+':
            first = stack.pop()
            second = stack.pop()
            stack.append(int(first)+int(second))
        elif i == '-':
            first = stack.pop()
            second = stack.pop()
            stack.append(int(second)-int(first))
        elif i == '*':
            first = stack.pop()
            second = stack.pop()
            stack.append(int(second)*int(first)) 

    return str(stack[0])


print(calc("1 2 3 * + 2 -"))

import doctest
doctest.testmod()
