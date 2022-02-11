#Reverse Array Queries

n = int(input()) #enter the array size
array = [] #initialize the empty array

for _ in range(n):
    array.append(int(input())) #read the array elements line by line

q = int(input()) #enter the operation array size
size = int(input()) #always 2

operations = []

for _ in range(q):
    operations.append(list(map(int, input().split()))) #read the operation array elements line by line

def performOperations(array, operations): #define the function
    new_array = array

    for oper in operations:
        new_array[oper[0]], new_array[oper[1]] = new_array[oper[1]], new_array[oper[0]] #switch elements in array

    return new_array #return new array


print(performOperations(array, operations))


"""
Test 1

3
1
2
3
3
2
0 2
1 2
0 2
"""
"""
Test 2

4
5
2
5
1
2
2
1 2
1 1
"""
