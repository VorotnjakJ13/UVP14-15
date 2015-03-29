def uredi(sez):
    "Urejanje po algoritmu 'quicksort'."
    def urediR(sez, i, j):
        if j - i == 2:  # samo dva elementa v seznamu
            if sez[i] > sez[j-1]:
                sez[i], sez[j-1] = sez[j-1], sez[i]
            return
        if j - i <= 1:  # samo en element v seznamu
            return
        k = pivot(sez, i, j)
        urediR(sez, i, k)
        urediR(sez, k + 1, j)

    def pivot(sez, i, j):
        z = i + 1
        k = j - 1
        while z < k:
            while z < k and sez[z] <= sez[i]: z += 1
            while sez[k] > sez[i]: k -= 1
            if z < k: (sez[z], sez[k]) = (sez[k], sez[z])
        sez[i], sez[k] = sez[k], sez[i]  # pivot na pravo mesto
        return k
                
    urediR(sez, 0, len(sez))

sez = [2,4,1,6,2,9,5,10,7,8]    
