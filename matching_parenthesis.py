def is_valid(s):

        n = len(s)

        if n==1:
            return False 

        stack = []
        open = ["[","{","("]
        close = {"[":"]", "{":"}", "(":")"}

        for i in range(n):
            if s[i] in open:
                stack.append(s[i])
            else:
                if stack==[]:
                    return False
                if s[i]!=close[stack[-1]]:
                    return False 
                else:
                    stack.pop()
        
        return stack==[]

is_valid("[[]](){")
is_valid("[[]](){}")
is_valid("[[({}){}(())]](){}")
is_valid("([)]")