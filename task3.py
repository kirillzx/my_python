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
    profits = [] #array of profits
    n = len(current)

    for i in range(n): #get the profit of each stock
        profits.append(future[i] - current[i]) #calc the difference between the future price and current

    matrix = [[0 for _ in range(saving + 1)] for _ in range(n + 1)] #create the profits matrix for dynamic programming

    for i in range(n + 1): #for all stocks
        for price in range(saving + 1): #and for all prices
            if i == 0 or price == 0: #if we take 0 stocks then profit 0
                matrix[i][price] = 0

            elif current[i-1] <= price: #if current price of stock i less or equal then current price
                #choose the max between previous profit at the same price and the previous profit plus profit of current stock
                matrix[i][price] = max(profits[i-1] + matrix[i-1][price - current[i-1]], matrix[i-1][price])

            else: #if current price greater then saving
                matrix[i][price] = matrix[i-1][price]

    return matrix[n][saving]

print(selectStocks(saving, currentPrices, futurePrices))
