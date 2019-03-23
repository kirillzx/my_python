first = input('Enter the first digit')
second = input('Enter the second digit')
operand = input('Enter the operand')

def calc(a,b,c):
    
    try:
        a = int(first)
        b = int(second)
        if c == '+':
            return a+b
        elif c == '-':
            return a-b
        elif c == '*':
            return a*b
        elif c == '/':
            return a/b
    except ValueError:
        print('You entered not a number')
    except ZeroDivisionError:
        print('Cannot be devided by zero')
        
print(calc(first,second,operand))    
