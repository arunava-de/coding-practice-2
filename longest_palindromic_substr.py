def longest_palindrome(s):

    n = len(s)

    if n==1:
        return s 
    
    opt = [[None]*n for i in range(n)] # opt[i][j] stores longest palindrome starting at s[i] and ending at s[j]

    start = 0
    end = 0

    for i in range(n):
        opt[i][i] = True

    for i in range(n-1):
        if s[i] == s[i+1]:
            opt[i][i+1] = True 
            start = i
            end = i + 1
        else:
            opt[i][i+1] = False

    k = 3
    while k<n:
        i = 0
        while i<n-k+1:
            j = i+k-1

            if opt[i+1][j-1]==True and s[i]==s[j]:
                opt[i][j] = True 
            
                if k>end-start+1:
                    start = i
                    end = j 
            i += 1
        k += 1

    return s[start:end+1]

s = "babad"
longest_palindrome(s)

s = "cbbd"
longest_palindrome(s)

s = "a"
longest_palindrome(s)

s = "ac"
longest_palindrome(s)    

s = "aaaaaa"
longest_palindrome(s) 

s = "abababa"
longest_palindrome(s) 

s = "abbaccddcca"
longest_palindrome(s) 




