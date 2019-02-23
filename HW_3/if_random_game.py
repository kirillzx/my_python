from random import *
n = randint(0, 5)
a = int(input('Guess the number: '))
if a == n:
    print('Victory!!! You guessed the number')
elif a > n:
    print('Its more than necessary\nTry again')
elif a < n:
    print('Its less than necessary\nTry again')
