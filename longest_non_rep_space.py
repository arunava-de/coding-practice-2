def longest_non_repeating(s):    
    if len(s)==0:
        return 0
    elif len(s)==1:
            return 1

    opt = [0]*len(s)
    opt[0] = 1
    start_curr = 0 #Stores starting of current longest subsequence
    curr_elms = {s[0]}
    
    for i in range(1, len(s)):
        if s[i] in curr_elms: # Here we find latest position the duplicate occurs
            for j in range(i-1,start_curr-1,-1):
                if s[j] == s[i]:
                    start_curr = j+1
                    break
            opt[i] = i-start_curr+1
            if opt[i]==1:
                curr_elms = {s[i]}
            # curr_elms.remove(s[i])
        else:
            opt[i] = 1 + opt[i-1]
            curr_elms.add(s[i])

    return max(opt)