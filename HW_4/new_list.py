#using the for loop
from math import sqrt
a = [2,9,16,25]
b = []
for i in range(len(a)):
    b.append(sqrt(a[i]))
print(b)    

#based on the map function
print(list(map(sqrt,a)))

#by the generator list
c = [sqrt(a[i]) for i in range(len(a))]
print(c)
