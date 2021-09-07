def crack_safe(n, k):
    start = "0"*(n-1)
    res = []
    edges = set()

    def dfs(node):
        nonlocal res 

        for i in range(k):
            curr_edge = node + str(i)

            if curr_edge not in edges:
                edges.add(curr_edge)
                dfs(curr_edge[1:])
                res.append(str(i))

    dfs(start)
    res.extend(['0']*(n-1))

    return "".join(res)
