def trapping_water(height):

    n = len(height)

    if n==1:
        return 0 

    left_max = [-1]*n
    right_max = [-1]*n

    for i in range(n-1):
        for j in range(i+1,n):
            left_max[i] = max(left_max[i], height[j])
    
    for i in range(n-1,0,-1):
        for j in range(i):
            right_max[i] = max(right_max[i], height[j])

    res = 0

    for i in range(1,n-1):
        if left_max[i]!=-1 and right_max[i]!=-1:
            res += max(min(left_max[i], right_max[i])-height[i], 0)

    return res 

height = [0,1,0,2,1,0,1,3,2,1,2,1]

height = [4,2,0,3,2,5]