def partition(l, r, arr):
    pivot = arr[l]
    pi = l 

    while l<r: 

        while l<len(arr) and arr[l]<=pivot:
            l += 1 

        while arr[r]>pivot:
            r -= 1

        if l<r:
            arr[l], arr[r] = arr[r], arr[l]
    
    arr[r], arr[pi] = arr[pi], arr[r]

    return r

def quicksort(l, r, arr):

    if l<r:
        pi = partition(l, r, arr)

        quicksort(l, pi-1, arr)
        quicksort(pi+1, r, arr)

arr = [1,4,2,7,4,9]
quicksort(0, len(arr)-1, arr)
