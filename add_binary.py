def add_binary(a, b):
    
    if a=="0":
        return b
    elif b=="0":
        return a 

    carry = 0

    # Making both of same size
    if len(a)>len(b):
        b = "0"*(len(a)-len(b)) + b
    elif len(b)>len(a):
        a = "0"*(len(b)-len(a)) + a

    c = len(a)-1
    s = ""

    while c>=0:
        if a[c]=="0" and b[c]=="0":
            s = str(carry) + s
            carry = 0
        elif a[c]=="1" and b[c]=="1":
            if carry==1:
                s = "1" + s
                carry = 1
            else:
                s = "0" + s 
                carry = 1
        else:
            if carry==1:
                s =  "0" + s
                carry = 1
            else:
                s = "1" + s
                carry = 0
        c -= 1 

    if carry==0:
        return s
    
    return "1" + s
            
a = "11" 
b = "1"
add_binary(a,b)

a = "1010" 
b = "1011"
add_binary(a,b)