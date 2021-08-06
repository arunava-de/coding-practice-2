def longest_non_repeating(s):

    if len(s)==0:
        return 0
    elif len(s)==1:
         return 1

    opt = [0]*len(s)
    opt[0] = 1
    start_curr = 0 #Stores starting of current longest subsequence

    for i in range(1, len(s)):
        if s[i] in s[start_curr:i]: # Here we find latest position the duplicate occurs
            for j in range(i-1,start_curr-1,-1):
                if s[j] == s[i]:
                    start_curr = j+1
                    break
            opt[i] = i-start_curr+1
        else:
            opt[i] = 1 + opt[i-1]
    
    return max(opt)

test1 = "abcabcbb"
print(longest_non_repeating(test1))

test2 = "bbbbb"
print(longest_non_repeating(test2))

test3 = "pwwkew"
print(longest_non_repeating(test3))

test4 = ""
print(longest_non_repeating(test4))

test5 = "aabbccdd"
print(longest_non_repeating(test5))

test6 = "aabcdefgg"
print(longest_non_repeating(test6))

test7 = "dvdf"
print(longest_non_repeating(test7))

test8 = 'ababababc'
print(longest_non_repeating(test8))