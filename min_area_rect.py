
def min_area_rectangle(points):

    n = len(points)
    if n<4:
        return 0
    Xdict = {}

    for p in points:
        if p[0] not in Xdict:
            Xdict[p[0]] = []
        Xdict[p[0]].append(p[1])

    min_area = float('inf')
    lastx = {}

    for x in sorted(Xdict):
        line = Xdict[x]
        line.sort()
        for j, y2 in enumerate(line):
            for i in range(j):
                y1 = line[i]

                if (y1, y2) in lastx:
                    min_area = min(min_area, (y2-y1)*(x-lastx[(y1,y2)]))

                lastx[(y1,y2)] = x

    if min_area<float('inf'):
        return min_area
    return 0


points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
min_area_rectangle(points)

    
