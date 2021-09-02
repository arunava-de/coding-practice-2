import math

def closest_pair(P):
    if len(P)==1:
        return 0

    Px = sorted(P, key=lambda x:x[0])
    Py = sorted(P, key=lambda x:x[1])

    ans = closest_pair_recur(Px, Py)

    return ans 

def dist(p,q):

    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

def closest_pair_recur(Px, Py):

    n = len(Px)

    if n<=3:
        mindist = float('inf')
        s0 = None 
        s1 = None
        for i in range(n):
            for j in range(i+1,n):
                if dist(Px[i], Px[j])<mindist:
                    mindist = dist(Px[i], Px[j])
                    s0 = Px[i]
                    s1 = Px[j]

        return s0, s1 

    mid = n//2 

    Qx = Px[:mid]
    Rx = Px[mid:]

    Qy = []
    Ry = [] 

    for i in range(n):
        if Py[i][0] in Qx:
            Qy.append(Py[i])
        else:
            Ry.append(Py[i])

    q0, q1 = closest_pair_recur(Qx, Qy)
    r0, r1 = closest_pair_recur(Rx, Ry)

    delta = min(dist(q0, q1), dist(r0,r1))

    L = Qx[-1][0] # Max x-coordinate in Q 
    
    Sx = []

    for i in range(n):
        if abs(Px[i][0]-L)<delta:
            Sx.append(Px[i])

    Sy = []

    for i in range(n):
        if Py[i][0] in Sx:
            Sy.append(Py[i])

    mindist = float('inf')
    s0 = None 
    s1 = None 

    for i in range(len(Sy)):

        for j in range(i, i+15):
            if j>=len(Sy):
                break 
            if dist(Sy[i], Sy[j])<mindist:
                mindist = dist(Sy[i], Sy[j])
                s0 = Sy[i]
                s1 = Sy[j]

    if mindist!=float('inf'):
        return s0, s1 
    else:
        if dist(q0,q1)<dist(r0,r1):
            return q0, q1
        else:
            return r0, r1

P = [[1,3],[-2,2],[0,0]]
closest_pair(P)

P = [[3,3],[5,-1],[-2,4], [0,0]]
closest_pair(P)

P = [[2, 3], [12, 30], [40, 50], [5, 1], [12, 10], [3, 4]]
p,q = closest_pair(P)
dist(p, q)


