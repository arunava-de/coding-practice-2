def wildlcard_matching(s,p):

    if len(s)==0 and len(p)==0:
        return True

    match = [[False for j in range(len(p)+1)] for i in range(len(s)+1)] # match[i][j] corresponds to whether s[:i] and p[:j] match or not

    match[0][0] = True

    for j in range(1,len(p)+1):
        if p[j-1]=='*':
            match[0][j] = match[0][j-1]

    for i in range(1,len(s)+1):
        for j in range(1,len(p)+1):
            if s[i-1]==p[j-1] or p[j-1]=='?':
                match[i][j] = match[i-1][j-1]
            else:
                if p[j]=='*':
                    match[i][j] = match[i][j-1] or match[i-1][j]
                else:
                    return match[i][j] = False

    return match[-1][-1]
        

# def wildlcard_matching(s,p):

#     if len(s)==0 and len(p)==0:
#         return True
#     elif len(p)>1 and p[0]=='*' and len(s)==0:
#         return False
    
#     if p[0]==s[0]:
#         return wildlcard_matching(p[1:], s[1:])
#     else:
#         if p[0]=='?':
#             return wildlcard_matching(p[1:],s[1:])
#         elif p[0]=='*':
#             return wildlcard_matching(s,p[1:]) or wildlcard_matching(s[1:],p) # Here either we use null string for * or don't
#         else:
#             return False

# s, p = input().split()

# print(wildlcard_matching(s,p))
