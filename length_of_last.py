def length_of_last_word(s):
    words = s.split()
    if words==[]:
        return 0
    return len(words[-1])