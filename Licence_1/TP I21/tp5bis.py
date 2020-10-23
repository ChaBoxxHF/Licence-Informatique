def fusionner(T1, T2) :
    tab = []
    k = 0
    while True :
        if T1 == [] or T2 == [] :
            tab += T1
            tab += T2
            return tab, k
        if T1[0] < T2[0] :
            tab.append(T1.pop(0))
        else :
            tab.append(T2.pop(0))
        k += 1
