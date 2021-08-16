def decode_string(s):

    countstack = []
    stringstack = []

    times = 0
    curr = ""

    for i in range(len(s)):
        if s[i].isdigit():
            times = times*10 + int(s[i])
        elif s[i]=='[':
            countstack.append(times)
            stringstack.append(curr)
            curr = ""
            times = 0
        elif s[i].isalpha():
            curr = curr + s[i]
        else: # We get a closing bracket
            t = countstack.pop()
            res = stringstack.pop() + t*curr
            curr = res 

    return curr 

s = "3[a]2[bc]"
decode_string(s)

s = "3[a2[c]]"
decode_string(s)

s = "2[abc]3[cd]ef"
decode_string(s)

s = "abc3[cd]xyz"
decode_string(s)

