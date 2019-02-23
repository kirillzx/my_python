s = input('Entry the string: ')
n = int(input('Entry the number: '))
def str_n(s,n):
    if len(s) > n:
        return s.upper()
    else:
        return s
print(str_n(s,n))
