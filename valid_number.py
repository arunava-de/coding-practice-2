def is_valid(s):

    n_dot = 0
    n_exp = 0 
    dig_flag = False 

    for idx,c in enumerate(s):
        if c in ["-", "+"]:
            if idx==0 or s[idx-1] in ["e", "E"]: #Either number starts with a sign, or sign is for the exponent
                continue 
            else:
                return False 
        elif c=='.':
            if n_dot==1 or n_exp==1: #Either more than one decimal point present, or power is not integer
                return False
            n_dot += 1
        elif c in ["e", "E"]:
            if n_exp==1 or not dig_flag: #Either exponent symbol has appeared already, or there's no digit before this
                return False 
            n_exp += 1
            dig_flag = False #Need to check valid integer after this
        elif c.isalpha(): #Any character other than 'e' or 'E' is invalid
            return False
        elif c.isnumeric():
            dig_flag = True 
        
    if dig_flag==True:
        return True 

    return False 

test1 = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]

for t in test1:
    print(t, is_valid(t))

test2 = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

for t in test2:
    print(t, is_valid(t))

            