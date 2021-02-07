def str_to_int(s):
    res = 0
    for digit in s:
        res *= 10
        d = ord(digit) - ord('0')
        res += d
    
    return res


def multiply_strings(s1,s2):
    # Convert string to integer indirectly
    # 0-9 in ASCII is 48-57, we can use this fact

    return str_to_int(s1)*str_to_int(s2)

print(multiply_strings('123','200'))
    