def interleave(a, l):
    res = []
#     print(a,l)
    res.append([a]+l)

    for i in range(1,len(l)):
        res.append(l[:i] + [a] + l[i:])
    
    res.append(l+[a])

    return res

def permuteUnique(nums):
    if len(nums)==1:
        return [[nums[0]]]
    else:
        res_temp = []
        for p in permuteUnique(nums[1:]):

            res_temp += interleave(nums[0],p)
        return [i for n, i in enumerate(res_temp) if i not in res_temp[:n]] 

