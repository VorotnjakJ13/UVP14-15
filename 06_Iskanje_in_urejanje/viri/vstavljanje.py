def uredi_vstavljanje(sez):
    """Uredi seznam sez z 'vstavljanjem'."""
    for i in range(len(sez)):   # začetek neurejenega dela
        j = i - 1               # sprehod po urejenem delu
        tmp = sez[i]            # element, ki ga vmeščamo
        while j >= 0 and sez[j] > tmp:
            sez[j + 1] = sez[j] # premik strogo večjih elementov
            j -= 1
        sez[j + 1] = tmp        # vpisovanje na pravo mesto

sez = [2,4,3,2,4,6,7,2,2,1]


    
