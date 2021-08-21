def max_profit(prices):

    n = len(prices)

    if n==1:
        return 0

    mins = [0]*n 
    mins[0] = prices[0]
    maxprof = 0 

    for i in range(1,n):

        if prices[i]<mins[i-1]: # Here we don't sell, but update the min till now
            mins[i] = prices[i]
        else: # There's a possibility of selling
            mins[i] = mins[i-1]
            if prices[i] - mins[i]>maxprof:
                maxprof = prices[i] - mins[i]
    
    return maxprof

prices = [7,1,5,3,6,4]
print(max_profit(prices))

prices = [7,6,4,3,1]
print(max_profit(prices))