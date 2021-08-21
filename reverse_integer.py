def reverse(x):
    if x<0:
        sign = '-'
        rev = str(x)[1:][::-1]
    else:
        sign = '+'
        rev = str(x)[::-1]

    lower = str(2**31)
    upper = str(2**31-1)

    rev = '0'*(len(lower)-len(rev)) + rev


    if sign=='-':
        for i in range(len(lower)):
            if rev[i]>lower[i]:
                return 0
            elif rev[i]<upper[i]:
                break
            else:
                continue
        
        return -int(rev)
    else:
        for i in range(len(upper)):
            if rev[i]>upper[i]:
                return 0
            elif rev[i]<upper[i]:
                break
            else:
                continue

        return int(rev)

x = 123
reverse(x)

x = 2**32
reverse(x)

x = -2**33
reverse(x)
