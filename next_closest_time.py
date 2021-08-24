def next_closest(time):

    h, m = list(map(int, time.split(':')))
    
    digs = set([time[0], time[1], time[3], time[4]])

    cand = ""

    while True:

        if m<59:
            m += 1
        else:
            m = 0
            h += 1
            if h==24:
                h = 0
        
        if h<10 and m<10:
            cand = '0' + str(h) + ':' + '0' + str(m)
        else:
            if h<10:
                cand = '0' + str(h) + ":" + str(m)[0] + str(m)[1]
            elif m<10:
                cand = str(h)[0] + str(h)[1] + ":" + '0' + str(m)
            else:
                cand = str(h)[0] + str(h)[1] + ":" + str(m)[0] + str(m)[1]

        if not set([cand[0], cand[1]]).issubset(digs): # We can directly skip this hour and save some complexity
            m = 59
            continue

        if set([cand[0], cand[1], cand[3], cand[4]]).issubset(digs):
            return cand

time = "19:34"
next_closest(time)

time = "23:59"
next_closest(time)

time = "20:48"
next_closest(time)


