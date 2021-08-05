def get_next_ind(idxs):
    stack = []
    result = [None]*len(idxs)

    for i in idxs:

        while stack and i>stack[-1]:
            result[stack.pop()] = i 
        stack.append(i)

    return result

def odd_even_jumps(arr):

    n = len(arr)

    if n==1:
        return 1

    sorted_idxs = sorted(range(n), key=lambda x: arr[x])
    odd_idxs = get_next_ind(sorted_idxs)
    sorted_idxs = sorted(range(n), key=lambda x: -arr[x])
    even_idxs = get_next_ind(sorted_idxs)

    starts = [False]*n
    even_starts = [False]*n 

    starts[n-1] = True 
    even_starts[n-1] = True

    c = 1 #Counting number of jumps

    for i in range(n-2,-1,-1):
        odd = odd_idxs[i]
        even = even_idxs[i]

        if odd!=None and even_starts[odd]:
            starts[i] = True 
            c += 1
        
        even_starts[i] = (even!=None and starts[even]==True)
    
    return c
    
test1 = [10, 13, 12, 14, 15]
test2 = [2,3,1,1,4]
test3 = [1]

print(odd_even_jumps(test1))
print(odd_even_jumps(test2))
print(odd_even_jumps(test3))