def simplify_path(path):

    if len(path)==1:
        return '/'

    res = []

    nodes = path.split("/")
    n = len(nodes)

    for i in range(n):
        
        if nodes[i]=='':
            continue
        elif nodes[i]=='.':
            continue 
        elif nodes[i]=='..':
            if res==[]:
                continue 
            else:
                res.pop()
        else:
            res.append(nodes[i])

    return '/' + '/'.join(res)

path = "/../"
simplify_path(path)

path = "/home//foo/"
simplify_path(path)

path = "/a/./b/../../c/"
simplify_path(path)

path = '/././.././'
simplify_path(path)

path = '/home_dir/a/b/../c/'
simplify_path(path)