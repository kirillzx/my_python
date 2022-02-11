#Footbal scores

n = int(input()) #enter the array size of team A

teamA = [] #initialize the empty array of team A

for _ in range(n): #read the array elements line by line
    teamA.append(int(input()))

m = int(input()) #enter the array size of team B

teamB = [] #initialize the empty array of team B

for _ in range(m): #read the array elements line by line
    teamB.append(int(input()))

def counts(teamA, teamB):
    res = [] #initialize the res empty array

    for goalsB in teamB: #for each match of team B we look for all matches of team A and
        k = 0            #count the number of matches where goals teamA <= teamB
        for goalsA in teamA:
            if goalsA <= goalsB:
                k += 1

        res.append(k) #append to res array the number of mathces that under constraints
    return res #return result

print(counts(teamA, teamB))

"""
Test 1

4
1
4
2
4
2
3
5

"""


"""
Test 2

5
2
10
5
4
8
4
3
1
7
8

"""
