import math
n = int(input('Entry the number'))
m = math.pi
def number_pi(n):
    return '{m:.{}f}'.format(n,m = math.pi)
    
print(number_pi(n))
