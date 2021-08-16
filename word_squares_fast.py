def word_squares(words):

    sz = len(words[0])

    if sz==1:
        return [[w] for w in words]

    prefix_dict = {}

    for w in words:
        for pfx in (w[:i] for i in range(1, sz)):
            prefix_dict.setdefault(pfx, set()).add(w)
    
    results = []
    for w in words:
        get_squares(1, results, [w], prefix_dict, sz)

    return results

def get_squares(step, results, word_squares, prefix_dict, sz):

    if step==sz:
        results.append(word_squares[:])
        return 

    prefix = ''.join(w[step] for w in word_squares)

    if prefix in prefix_dict.keys():
        for word in prefix_dict[prefix]:
            word_squares.append(word)
            get_squares(step+1, results, word_squares, prefix_dict, sz)
            word_squares.pop()

    return 


words = ["area","lead","wall","lady","ball"]
print(word_squares(words))

words = ["abat","baba","atan","atal"]
print(word_squares(words))

