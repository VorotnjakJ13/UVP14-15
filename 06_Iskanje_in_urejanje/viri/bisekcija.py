def bisekcija(sez, x):
    """Vrne True, če se v urejenem seznamu sez nahaja element x.
    Iskanje poteka z biseksijo."""
    i = 0                             # levi rob
    j = len(sez) - 1                  # desni rob
    if x < sez[i] or x > sez[j]:      # je možno, da je x v seznamu?
        return False                
    while i < j:                      # ponavljanje na manjših podseznamih
        k = (i + j)//2                # srednji element
        if sez[k] == x:               # smo ga našli?
            return True
        elif x < sez[k]:              # x je lahko le levem podseznamu
            j = k - 1  
        else:                         # x je lahko le v desnem podseznamu
            i = k + 1
    return i == j and sez[i] == x     # Ali je na koncu x najden.

sez = [1,2,2,4,5,7,10,12]

# Alternativni način delitve (brez preverjanja srednjega elementa).
def bisekcija2(sez, x):
    """Vrne True, če se v urejenem seznamu sez nahaja element x.
Iskanje poteka z biseksijo."""
    i = 0
    j = len(sez) - 1
    if x < sez[i] or x > sez[j]:
        return False
    while i < j:
        k = (i + j)//2
        if x <= sez[k]:
            j = k  
        else:
            i = k + 1
    return i == j and sez[i] == x

# Rekurzivna funkcija s časovno zahtevnostjo O(n) - zaradi kopiranja seznamov!!!
def bisekcijaR(sez, x):
    """Vrne True, če se v urejenem seznamu sez nahaja element x.
    Iskanje poteka z biseksijo."""
    if len(sez) == 0: return False
    if len(sez) == 1:
        return sez == [x]
    k = len(sez)//2
    if x < sez[k]:
        return bisekcijaR(sez[:k], x)
    else:
        return bisekcijaR(sez[k:], x)


# Rekurzivna funkcija brez kopiranja seznamov. 
def bisekcijaR2(sez, x):
    """Vrne True, če se v urejenem seznamu sez nahaja element x.
    Iskanje poteka z biseksijo."""    
    def poisci(sez, x, i, j):
        if i > j: return False
        if i == j: return x == sez[i]
        k = (i + j)//2
        if x <= sez[k]:
            return poisci(sez, x, i, k)
        else:
            return poisci(sez, x, k + 1, j)
    return poisci(sez, x, 0, len(sez) - 1)
    

def poisci(sez, x, i=0, j = None):
    """Vrne True, če se v urejenem seznamu sez nahaja element x.
Iskanje poteka z biseksijo."""    
    # None pomeni cel seznam. Stavek 'if' potreben, ker len(sez)
    # ne moremo podati kot privzeto vrednost.
    if j == None:   
        j = len(sez) - 1
    if i > j: return False
    if i == j: return x == sez[i]
    k = (i + j)//2
    if x <= sez[k]:
        return poisci(sez, x, i, k)
    else:
        return poisci(sez, x, k + 1, j)
