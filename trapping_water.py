def trap(height):
    # i-th position can store water if there are higher bars on the left and right of i
    # Amount of water stored by i-th position is determined by the min of highest bars on either side

    # We can use two stacks to maintain heights of bars on either side of i-th position. 
    if height == []:
        return 0
        
    left =[0] * len(height)
    left[0] = height[0] # Stack to store highest bars on left side
    right = [0] * len(height)
    right[-1] = height[-1] # Stack to store highest bars on right side

    for i in range(1,len(height)):
        left[i] = max(left[i-1], height[i])

    for i in range(len(height)-2,-1,-1):
        right[i] = max(right[i+1], height[i])

    water = 0
    for i in range(len(height)):
        water += min(left[i],right[i]) - height[i]

    return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))




    