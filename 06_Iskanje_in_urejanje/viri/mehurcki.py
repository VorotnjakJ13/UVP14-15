def uredi_mehurcki(sez):
    "Urejanje z algoritmom 'bubble sort'."
    for k in range(len(sez) - 1, 0, -1):  # končni indeks i-tega obhoda
        zamenjava = False         # ali je prišlo do zamenjave?
        for j in range(k):        # obhod: od začetka do k
            if sez[j] > sez[j + 1]:
                sez[j], sez[j + 1] = sez[j + 1], sez[j]
                zamenjava = True
        if not zamenjava:         # konec če ni zamenjave v obhodu
            break


sez = [2,3,1,4,2,5,7,3,2]
