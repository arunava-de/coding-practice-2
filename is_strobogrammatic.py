def is_strobogrammtic(num):

    flips = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

    num = str(num)
    n = len(num)

    for c in num:
        if c not in flips:
            return False

    mid = n//2

    if n%2!=0:
        if num[mid]=='6' or num[mid]=='9':
            return False 

    for i in range(mid):
        if flips[num[i]]!=num[n-i-1]:
            return False 

    return True

is_strobogrammtic(1001)
is_strobogrammtic(9009)
is_strobogrammtic(8698)
