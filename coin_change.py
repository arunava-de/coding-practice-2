def coin_change(coins, amount):
    if amount==0:
        return 0 
    elif len(coins)==1 and amount%coins[0]!=0:
        return -1 

    n = len(coins)
    opt = [float('inf')]*(amount+1)
    opt[0] = 0

    for i in range(n):
        for j in range(coins[i], amount+1):
            opt[j] = min(opt[j], opt[j-coins[i]]+1)

    return opt[-1]

    
coins = [1,2,5]
amount = 11
coin_change(coins, amount)

coins = [1]
amount = 2
coin_change(coins, amount)