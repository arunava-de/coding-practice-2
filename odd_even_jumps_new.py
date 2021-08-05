def odd_jump_idx(i, arr):
    n = len(arr)

    min_val = float('inf')
    min_ind = i
    for j in range(i+1,n):
        if arr[j]>=arr[i] and arr[j]<min_val:
            min_val = arr[j]
            min_ind = j
    if min_ind == i: #No legal jumps present
        return None
    return min_ind

def even_jump_idx(i, arr):
    n = len(arr)

    max_val = -float('inf')
    max_ind = i
    for j in range(i+1,n):
        if arr[j]<=arr[i] and arr[j]>max_val:
            max_val = arr[j]
            max_ind = j
    if max_ind == i: #No legal jumps present
        return None
    return max_ind

def odd_even_jumps(arr):

    n = len(arr)

    starts = [False]*len(arr) # True if n-1 can be reached from i
    even_starts = [False]*len(arr) # True if n-1 can be reached from i on landing at i after odd number of steps

    starts[n-1] = True 
    even_starts[n-1] = True 

    c = 1 #Counting number of jumps

    for i in range(n-2,-1,-1):
        odd = odd_jump_idx(i, arr)
        even = even_jump_idx(i, arr)

        if odd!=None and even_starts[odd]:
            starts[i] = True 
            c += 1
        
        even_starts[i] = (even!=None and starts[even]==True)

    return c

        
test1 = [10, 13, 12, 14, 15]
test2 = [2,3,1,1,4]

print(odd_even_jumps(test1))
print(odd_even_jumps(test2))
