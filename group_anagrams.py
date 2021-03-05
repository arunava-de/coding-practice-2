def groupAnagrams(strs):
    
    if len(strs)==0:
        return [[""]]
    elif len(strs)==1:
        return [strs]
    
    strs_sorted = [tuple(sorted(i)) for i in strs]

    sorted_dict = {}

    for i,s in enumerate(strs_sorted):
        if s in sorted_dict.keys():
            sorted_dict[s].append(i)
        else:
            sorted_dict[s] = [i]
    
    res = []

    for s in sorted_dict.keys():
        res = res + [[strs[i] for i in sorted_dict[s]]]

    return res 
        