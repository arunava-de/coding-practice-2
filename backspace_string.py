def backspace_compare(s, t):
    stack_s = []
    stack_t = []

    n1 = len(s)
    n2 = len(t)

    for i in range(n1):
        if s[i]!='#':
            stack_s.append(s[i])
        else:
            if stack_s==[]:
                continue 
            else:
                stack_s.pop()
    
    for i in range(n2):
        if t[i]!='#':
            stack_t.append(t[i])
        else:
            if stack_t==[]:
                continue 
            else:
                stack_t.pop()

    return stack_s==stack_t

