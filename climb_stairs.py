def climb_stairs(n):

    if n==1:
        return 1
    elif n==2:
        return 2
    elif n<=0:
        return 0
    
    return (climb_stairs(n-1) + climb_stairs(n-2))