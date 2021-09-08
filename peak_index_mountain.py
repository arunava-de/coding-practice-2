def peak_index(arr):
    n = len(arr)
    
    for i in range(1,len(arr)-1):
        
        if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
            break
            
    return i 