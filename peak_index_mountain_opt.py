def peak_index(arr):

    n = len(arr)
    low = 1
    high = n-2

    while low<high:
        mid = (low+high)//2

        if arr[mid-1]<arr[mid]<arr[mid+1]:
            low = mid+1

        elif arr[mid-1]>arr[mid]>arr[mid+1]:
            high = mid-1 
        else:
            return mid 
    
    return low 

arr = [0,1,0]
peak_index(arr)

arr = [0,2,1,0]
peak_index(arr)

arr = [0,10,5,2]
peak_index(arr)

arr = [3,4,5,1]
peak_index(arr)

arr = [24,69,100,99,79,78,67,36,26,19]
peak_index(arr)