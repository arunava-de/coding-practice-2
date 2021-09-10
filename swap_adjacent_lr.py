def can_transform(start, end):

    n1 = len(start)
    n2 = len(end)

    if n1!=n2:
        return False 

    j = 0

    for i in range(n1):
        if start[i]!='X':
            while j<n1 and end[j]=='X':
                j += 1
            if j==n1:
                return False 
            if start[i]!=end[j] or (start[i]=='R' and j<i) or (start[i]=='L' and j>i):
                # 3 conditions covered, i) cars cannot cross each other ii) cars on right lane cannot move to left
                # iii) cars on left lane cannot move to right
                return False 
            j += 1

    while j<n1: # Exhaust remaining spaces
        if end[j]!='X': 
            return False 
        j += 1

    return True

start = "RXXLRXRXL"
end = "XRLXXRRLX"
can_transform(start, end)

start = "LLR"
end = "RRL"
can_transform(start, end)

start = "XLLR" 
end = "LXLX"
can_transform(start, end)




    


    
