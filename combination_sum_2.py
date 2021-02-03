def combinationSum2(candidates, target):
    candidates.sort() #Keeping candidates sorted ensures no duplicates

    # We go through list from left to right, each element can be start of the sum

    # for i in range(len(candidates)):
    
    def find_sol(l,t,path,out):
        if t<0:
            return 
        elif t==0:
            out.append(path)
        
        for i in range(len(l)):
            if i>0 and l[i]==l[i-1]:
                continue
            find_sol(l[i+1:], t-l[i], path + [l[i]], out)


    out = []
    find_sol(candidates, target, [], out)

    return out
    
    out = []
    return find_sol(candidates, target, [], out)

print(combinationSum2([2,5,2,1,2],5))



        