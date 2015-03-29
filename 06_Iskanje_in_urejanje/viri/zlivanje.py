def zlij(sez1, sez2):
    """Zlije dva urejena seznama v urejen seznam in ga vrne."""
    s1 = 0    # števca prvega elementa po dveh tabelah
    s2 = 0
    sez = []    # nova tabela
    for i in range(len(sez1) + len(sez2)):
        if s1 >= len(sez1):
            sez.append(sez2[s2]); s2 += 1
        elif s2 >= len(sez2):
            sez.append(sez1[s1]); s1 += 1
        elif sez1[s1] < sez2[s2]:
            sez.append(sez1[s1]); s1 += 1
        else:
            sez.append(sez2[s2]); s2 += 1
    return sez

def uredi_zlivanje(sez):
    def urediR(i, j):
           # vrne urejen seznam, za podseznam sez[i:j]
        if (j - i) <= 1:
            return sez[i:j]
        k = (i + j)//2
        sez1 = urediR(i, k)
        sez2 = urediR(k, j)
        return zlij(sez1, sez2)
    nov = urediR(0, len(sez))
    sez.clear()
    sez += nov
            
sez = [2,4,1,6,2,9,5,10,7,8]           
    
def uredi_zlivanje2(t):
    "Urejanje seznama z zlivanjem samo z enim dodatnim seznamom."
    def urediR(t, t2, i, j):
        if j - i <= 1:
            return
        k = (i + j)//2
        urediR(t, t2, i, k)
        urediR(t, t2, k, j)
        r, s, p = i, k, i # inicializacija števcev
        for x in range(i,j):
            if r >= k: 
                t2[p] = t[s]
                s += 1
            elif s >= j:
                t2[p] = t[r]
                r += 1
            elif t[r] <= t[s]:
                t2[p] = t[r]
                r += 1
            else:
                t2[p] = t[s]
                s += 1
            p += 1
        for x in range(i, j):
            t[x] = t2[x]
    t2 = list(t)
    urediR(t, t2, 0, len(t))


