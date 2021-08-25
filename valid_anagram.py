def is_anagram(s, t):
    if len(s)!=len(t):
            return False 
        
    n = len(s)
    
    if n==0:
        return True 
    
    sdict = {}
    tdict = {}
    
    for i in range(26):
        sdict[chr(97+i)] = 0
        tdict[chr(97+i)] = 0
        
    for i in range(n):
        sdict[s[i]] += 1
        tdict[t[i]] += 1
        
    for i in range(26):
        if sdict[chr(97+i)]!=tdict[chr(97+i)]:
            return False 
            
    return True

