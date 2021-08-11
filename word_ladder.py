def ladder_length(begin, end, words):

    if end not in words:
        return 0

    pattern_dict = dict() # We use this to store all possible single character word changes for any word

    for w in words:
        for i in range(len(w)):
            temp = w[:i] + '*' + w[i+1:]
            
            if temp in pattern_dict.keys():
                pattern_dict[temp].append(w)
            else:
                pattern_dict[temp] = [w]
    
    Q = [(begin,1)]
    visited = set()
    visited.add(begin)

    while Q:
        u, l = Q.pop(0)
        
        patterns = []
        for i in range(len(u)):
            patterns.append(u[:i] + '*' + u[i+1:])

        for p in patterns:
            if p not in pattern_dict:
                pattern_dict[p] = []
                continue

            for w in pattern_dict[p]:
                if w==end:
                    # print(l+1)
                    # break
                    return l + 1
                if w not in visited:
                    visited.add(w)
                    Q.append((w,l+1))
            # pattern_dict[p] = []

    return 0

words = ["hot","dot","dog","lot","log","cog"]
begin = "hit"
end = "cog"

print(ladder_length(begin, end, words))
