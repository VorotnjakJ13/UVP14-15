sez = [5,1,2,8,7,3,6,3]


def vrni_minimalnega(sez):
    tmpmin = sez[0]
    for i in range(len(sez)):
        if sez[i] < tmpmin:
            tmpmin = sez[i]
    return tmpmin

def vrni_indeks_od_minimalnega(sez):
    tmpi = 0
    for i in range(len(sez)):
        if sez[i] < sez[tmpi]:
            tmpi = i
    return tmpi
            

def najdi(sez, i):
    tmpi = i
    for j in range(i, len(sez)):
        if sez[j] < sez[tmpi]:
            tmpi = j
    return tmpi    

def uredi(sez):
    for i in range(len(sez)):
        j = najdi(sez, i)
        sez[i],sez[j] = sez[j],sez[i]


