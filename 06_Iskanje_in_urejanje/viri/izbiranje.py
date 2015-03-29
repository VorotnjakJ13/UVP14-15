def uredi_izbiranje(sez, z=0):
    """Uredi seznam sez z 'izbiranjem' (rekurzivno)."""
        # Vrne indeks, kjer se nahaja minimum v seznamu sez od indeks i dalje.
    def minind(sez, i):
        mni = i
        for j in range(i + 1, len(sez)):
            if sez[j] < sez[mni]:
                mni = j
        return mni
    if z == len(sez):                   # zaustavitveni pogoj
        return
    k = minind(sez, z)                  # min indeks
    sez[z], sez[k] = sez[k], sez[z]     # zamenjava
    uredi_izbiranje(sez, z + 1)         # rekurzivni klic

sez = [3,2,7,4,1,2,3,8,3,2]    

def uredi_izbiranje2(sez, z=0):
    "Uredi seznam sez z 'izbiranjem'."
    for i in range(len(sez)):
        mni = i
        for j in range(i + 1, len(sez)):
            if sez[j] < sez[mni]:
                mni = j
        sez[mni], sez[i] = sez[i], sez[mni]
