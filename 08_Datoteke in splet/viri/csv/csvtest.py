import csv

def preberi_podatke(dat= 'H103Ss.csv'):
    with open(dat, encoding="cp1250") as csvfile:
        for i in range(2):          # izpusti 2 vrstici       
            next(csvfile)
        vsebina = csv.reader(csvfile, delimiter=';', quotechar='"', )
        podatki = []
        for vrstica in vsebina:
            if len(vrstica) == 0:   # končaj branje pri prvi prazni vrstici
                break
            podatki.append(vrstica)
        return podatki


def stolpec_v_procente(seznam, j):
    skupaj = int(seznam[1][j])
    for i, v in enumerate(seznam):
        if i < 2 or v[j] == "-":   # vrstica z glavo in vrstica s SKUPAJ
            continue
        v[j] = "{:5.2f}".format(int(v[j])/skupaj).replace(".", ",")

def v_procente(podatki):
    for j in range(1, len(podatki[0])):
        stolpec_v_procente(podatki, j)

def zapisi(dat, podatki):
    with open(dat, "wt", encoding="cp1250") as f:
        zapisovalec = csv.writer(f, delimiter=';', )
        for vrstica in podatki:
            zapisovalec.writerow(vrstica)

def test(vhdat = "H103Ss.csv", izdat = "popravljena.csv"):
    podatki = preberi_podatke(vhdat)
    v_procente(podatki)
    zapisi(izdat, podatki)

test()
