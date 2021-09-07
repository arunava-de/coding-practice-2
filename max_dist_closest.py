def max_dist_to_closest(seats):

    n = len(seats)
    if n==2:
        return 1

    seats = [-1] + seats + [-1]

    closest_left = [0]*(n+2) # ith position stores distance to closest seat on the left
    closest_right = [0]*(n+2) # ith position stores distance to closest seat on the right

    dist = 0 

    for i in range(n+2):
        if seats[i]==0:
            if dist>-float('inf'):
                dist += 1
            else:
                dist = -float('inf')
        elif seats[i]==1:
            dist = 0 
        else:
            dist = -float('inf')
        closest_left[i] = dist 
    
    for i in range(n+1,-1,-1):
        if seats[i]==0:
            if dist>-float('inf'):
                dist += 1
            else:
                dist = -float('inf')
        elif seats[i]==1:
            dist = 0 
        else:
            dist = -float('inf')
        closest_right[i] = dist

    max_close = 0

    for i in range(n+2): 
        if seats[i]==0:
            if closest_left[i]==-float('inf') or closest_right[i]==-float('inf'):
                max_close = max(max_close,max(closest_left[i], closest_right[i]))
            else:
                max_close = max(max_close,min(closest_left[i], closest_right[i]))

    return max_close

seats = [1,0,0,0,1,0,1]
max_dist_to_closest(seats)

seats = [1,0,0,0] 
max_dist_to_closest(seats)

seats = [0,1]
max_dist_to_closest(seats)

seats = [0,0,1]
max_dist_to_closest(seats)

