def heapify(arr, n, i):

    smallest = i 
    left = 2*i + 1
    right = 2*i + 2

    if left<n and arr[left]<smallest:
        smallest = left

    if right<n and arr[right]<smallest:
        smallest = right 

    if smallest!=i: # In this case we need to change the subtree
        arr[i], arr[smallest] = arr[smallest], arr[i]

        heapify(arr, n, smallest)

def make_heap(arr):
    n = len(arr)

    start = n//2 - 1 

    for i in range(start, -1, -1):
        heapify(arr, n, i)

    return arr 

    