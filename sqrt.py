def new_sqrt(x):
    if x==0:
            return 0
        
    i = 1
    while i<=x:
        if i*i<=x and (i+1)*(i+1)>x:
            return i
        i += 1
        
    return