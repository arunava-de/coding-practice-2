import math

def dist(p):
    return math.sqrt(p[0]**2 + p[1]**2)

def k_closest(points, k):

    points = merge_sort(points)

    return points[:k]

def merge_sort(points):

    if len(points)==1:
        return points 
    elif len(points)==2:
        if dist(points[0])<dist(points[1]):
            return points 
        else:
            return [points[1],points[0]]

    mid = len(points)//2 

    left = merge_sort(points[:mid])
    right = merge_sort(points[mid:])

    return merge(left, right)

def merge(left, right):

    i = 0
    j = 0

    c = []

    while i<len(left) and j<len(right):
        if dist(left[i])<dist(right[j]):
            c.append(left[i])
            i += 1
        else:
            c.append(right[j])
            j += 1

    while i<len(left):
        c.append(left[i])
        i += 1
    
    while j<len(right):
        c.append(right[j])
        j += 1

    return c

points = [[1,3],[-2,2]]
k = 1
k_closest(points, k)

points = [[3,3],[5,-1],[-2,4]]
k = 2
k_closest(points, k)

points = [[-5,4],[-6,-5],[4,6]]
k = 2
k_closest(points, k)