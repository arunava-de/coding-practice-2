import math 

def partition(arr, start, end, k):

    l = start
    r = end
    pivot = arr[l][0]
    pi = l 

    while l<r:

        while l<len(arr) and arr[l][0]<=pivot:
            l += 1

        while arr[r][0]>pivot:
            r -= 1 

        if l<r:
            arr[l], arr[r] = arr[r], arr[l]

    arr[r], arr[pi] = arr[pi], arr[r]

    if r-start+1==k: 
        return
    if r-start+1>k: # We look at left side
        partition(arr, start, r, k)
    else: # We look at right side, keeping in mind that we've already found r-start+1 elements
        partition(arr, r+1, end, k-(r-start+1))

def dist(p):
    return math.sqrt(p[0]**2 + p[1]**2)
    
def kClosest(points, k):
    
    dists = [(dist(p), p) for p in points]

    partition(dists, 0, len(dists)-1, k)

    return [dists[i][1] for i in range(k)]


points = [[1,3],[-2,2]]
k = 1
kClosest(points, k)

points = [[3,3],[5,-1],[-2,4]]
k = 2
kClosest(points, k)

points = [[-5,4],[-6,-5],[4,6]]
k = 2
kClosest(points, k)
    
