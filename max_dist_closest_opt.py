def max_dist_to_closest(seats):

    n = len(seats)
    if n==2:
        return 1

    closest_left = [0]*n # ith position stores distance to closest seat on the left
    closest_right = [0]*n # ith position stores distance to closest seat on the right

    dist = 0 
    if seats[0]==0:
        dist = -1

    for i in range(n):
        if seats[i]==0:
            if dist>-1:
                dist += 1
            else:
                dist = -1
        else:
            dist = 0
        closest_left[i] = dist
    
    dist = 0
    if seats[-1]==0:
        dist = -1

    for i in range(n-1,-1,-1):
        if seats[i]==0:
            if dist>-1:
                dist += 1
            else:
                dist = -1
        else:
            dist = 0
        closest_right[i] = dist

    max_close = 0

    for i in range(n): 
        if seats[i]==0:
            if closest_right[i]>-1 and closest_left[i]>-1:
                max_close = max(max_close,min(closest_left[i], closest_right[i]))
            else:
                max_close = max(max_close,max(closest_left[i], closest_right[i]))

    return max_close

seats = [1,0,0,0,1,0,1]
max_dist_to_closest(seats)

seats = [1,0,0,0] 
max_dist_to_closest(seats)

seats = [0,1]
max_dist_to_closest(seats)

seats = [0,0,1]
max_dist_to_closest(seats)

