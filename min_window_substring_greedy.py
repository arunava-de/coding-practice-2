def min_window(s, t):
    m = len(s)
    n = len(t)

    if n>m:
        return ""
    
    if n==1 and m==1:
        if s==t:
            return s
        else:
            return ""

    s_d = dict() # This dictionary stores details of s

    for i in range(m):
        if s[i] in s_d.keys():
            s_d[s[i]] += 1
        else:
            s_d[s[i]] = 1

    t_d = dict() # This dictionary stores details of t

    for i in range(n):
        if t[i] in t_d.keys():
            t_d[t[i]] += 1
        else:
            t_d[t[i]] = 1

    l = 0
    r = m-1 
    # min_window = ""
    # f = 0 
    l_min = 0
    r_min = m-1

    while l<=r:
        left_cand = s[l]
        right_cand = s[r]
        # f = 0 

        if left_cand not in t_d.keys() or s_d[left_cand]-1>=t_d[left_cand]: # We can afford to move left pointer
            # f = 1
            l += 1 
            s_d[left_cand] -= 1
            l_min = l
        elif s_d[left_cand]-1<t_d[left_cand]: # We stop moving left and start expanding right

            # min_window =  s[l:r+1]
            l = 0
            if right_cand not in t_d.keys() or s_d[right_cand]-1>=t_d[right_cand]: # We can contract from right
                # f = 1
                r -= 1
                r_min = r
                s_d[right_cand] -= 1
                continue
            elif s_d[right_cand]-1<t_d[right_cand]:
                break 
    
    cand = s[l_min:r_min+1]

    for c in cand:
        if c not in t_d.keys():
            continue
        else:
            t_d[c] -= 1
            if t_d[c]<0:
                return ""
    
    for c in t_d.keys():
        if t_d[c]!=0:
            return ""

    return cand

print(min_window("aa", "a"))
print(min_window("a", "aa"))
print(min_window("a", "a"))
print(min_window("ADOBECODEBANC", "ABC"))
print(min_window("ADBCCCGH", "ZAC"))
print(min_window("ab", "a"))
print(min_window("AB", "a"))
print(min_window("bbaac", "aba"))