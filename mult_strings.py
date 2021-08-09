def str_to_int(s):

    res = 0

    for i in range(len(s)):
        res *= 10
        res += ord(s[i]) - ord('0')

    return res

def multiply_strings(num1, num2):

    return str_to_int(num1)*str_to_int(num2)
