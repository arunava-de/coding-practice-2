def new_sqrt(x):

    if x==0:
        return 0 

    low = 1
    high = x

    while low<=high:

        mid = (low+high)//2

        if mid*mid<x:
            if (mid+1)*(mid+1)>x:
                return mid 
            else:
                low = mid+1
        elif mid*mid>x:
            if (mid-1)*(mid-1)<=x:
                return mid-1
            else:
                high = mid-1
        else:
            return mid

    