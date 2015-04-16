# Testni seznam
sez = [5,2,3,6,1,7,9,2,1,3]


def uredi_izbiranje(sez):
    def najdi_in_zamenjaj(sez, i):
        mni = i
        for j in range(i + 1, len(sez)):
            if sez[j] < sez[mni]:
                mni = j
        sez[i],sez[mni] = sez[mni],sez[i]

    for i in range(len(sez)):
        najdi_in_zamenjaj(sez, i)

    
def uredi_vstavljanje(sez):
    def vstavi(sez, i):
        tmp = sez[i]
        for j in range(i - 1, -1, -1):
            if sez[j] > tmp:
                sez[j + 1] = sez[j]
            else:
                sez[j + 1] = tmp
                return
        sez[0] = tmp  
    for i in range(1, len(sez)):
        vstavi(sez, i)


def zlij(sez, zac, sred, kon):
    z1 = zac
    z2 = sred + 1
    novi = []
    for i in range(kon - zac + 1):
        if z1 > sred: # prva vrsta prazna
            novi.append(sez[z2])
            z2 += 1
        elif z2 > kon: # druga vrsta prazna
            novi.append(sez[z1])
            z1 += 1
        elif sez[z1] < sez[z2]:
            novi.append(sez[z1])
            z1 += 1
        else:
            novi.append(sez[z2])
            z2 += 1
            
    for i in range(len(novi)):
        sez[zac + i] = novi[i]

s = [5,6,7,8,1,2,3,4]
            

def uredite_zlivanje(sez, zac, kon):
    if kon - zac > 0:
        sred = (kon + zac) // 2
        uredite_mi(sez, zac, sred)
        uredite_mi(sez, sred + 1, kon)
        zlij(sez, zac, sred, kon)

