def trapping_water(height):

    n = len(height)

    if n==1:
        return 0 

    left_max = [-1]*n
    right_max = [-1]*n
    left_max[0] = height[0]
    right_max[-1] = height[-1]
    
    for i in range(1,n):
        left_max[i] = max(left_max[i-1], height[i])

    for i in range(n-1,-1,-1):
        right_max[i] = max(right_max[i+1], height[i])

    res = 0

    for i in range(n-1):
        res += min(left_max[i], right_max[i])-height[i]

    return res 
