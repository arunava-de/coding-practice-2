def max_profit(prices):

    n = len(prices)

    if n==1:
        return 0

    # mins = [0]*n 
    min_till_now = prices[0]
    maxprof = 0 

    for i in range(1,n):

        if prices[i]<min_till_now: # Here we don't sell, but update the min till now
            min_till_now = prices[i]
        else: # There's a possibility of selling
            if prices[i] - min_till_now>maxprof:
                maxprof = prices[i] - min_till_now
    
    return maxprof

prices = [7,1,5,3,6,4]
print(max_profit(prices))

prices = [7,6,4,3,1]
print(max_profit(prices))