def sum_span(l, r, A):

    s = 0
    for i in range(l,r):
        s = s + A[i]
    return s

def solve(A, B):

    n = len(A)
    left = B-1
    right = n

    max_sum = -1000000

    while left>=-1:

        temp = sum_span(0, left+1, A) + sum_span(right, n, A)
        if temp>max_sum:
            max_sum = temp
        left -= 1
        right -= 1

    return max_sum