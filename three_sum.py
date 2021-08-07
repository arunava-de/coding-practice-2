def three_sum(nums):

    if len(nums)<3:
        return []
    elif len(nums)==3: 
        if sum(nums)!=0:
            return []
        else:
            return[nums]

    out = []
    d = dict()

    for num in nums:
        if num in d.keys():
            d[num] += 1
        else:
            d[num] = 1

    for num in d.keys():
        d[num] -= 1
        target = -num

        for j in d.keys():
            if j==target-j:
                if d[j]>1:
                    res = sorted([num, j, target-j])
                else:
                    continue
            else:
                if d[j]>0 and target-j in d.keys() and d[target-j]>0:
                    res = sorted([num, j, target-j])
                else:
                    continue
            if res not in out:
                out.append(res)
    
    return out

test1 = [-1,0,1,2,-1,-4]
print(three_sum(test1))
