#Selecting Stocks

saving = int(input()) #enter the saving money
n = int(input()) #enter the array size of current prices

currentPrices = [] #initialize the empty array of current prices

for _ in range(n): #read the array elements line by line
    currentPrices.append(int(input()))

n = int(input()) #enter the array size of futureP pices

futurePrices = [] #initialize the empty array of future prices

for _ in range(n): #read the array elements line by line
    futurePrices.append(int(input()))

def selectStocks(saving, current, future):
    profit = [] #array of profits
    p = 0 #the result of all stock profits

    for i in range(len(current)): #get the profit of each stock
        temp = future[i] - current[i] #calc the difference between the future price and current

        if temp > 0: #take just positive values
            profit.append((i, temp))

    if len(profit) != 0: #if we can get the profit from stocks, so there are values greater then 0
        profit = sorted(profit, reverse=True, key=lambda x: x[1]) #sort in descending order by second element (by profit)

        cost = current[profit[0][0]] #price of greater stock

        for i, item in profit:
            if  cost <= saving: #if price under constraint
                p += item       #calc the profit
                cost += current[i]  #increase the current price

        return p

    else: #if profit equal or less zero then return 0
        return 0

print(selectStocks(saving, currentPrices, futurePrices))

"""
Test 1

30
4
1
2
4
6
4
5
3
5
6

"""

"""
Test 2

500
5
150
199
200
168
153
5
140
175
199
121
111

"""
