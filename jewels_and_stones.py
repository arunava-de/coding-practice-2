def num_jewels_in_stones(jewels, stones):

    # jset = set(jewels)
    c = 0 

    for s in stones:
        # if s in jset:
        if s in jewels:
            c += 1

    return c

