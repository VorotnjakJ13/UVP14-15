import os

def sestavi(ime, trenutna="."):
    dat = None
    with open(ime, encoding="utf8") as f:
        for vrstica in f:
            if vrstica.startswith("-"):
                if dat is not None:
                    dat.close()
                    dat = None
                pot = os.path.join(trenutna, vrstica.lstrip("-").strip())
                os.mkdir(pot) 
            elif vrstica.startswith("*"):
                if dat is not None:
                    dat.close()
                
                pot = os.path.join(trenutna, vrstica.lstrip("*").strip())
                dat = open(pot, "wt", encoding="utf8")
            elif dat is not None:
                dat.write(vrstica)
                               
#sestavi("mape_in_datoteke.txt")            

def nekaj_vrstic(pot, n=3):
    f = open(pot, encoding="utf8")
    rez = ""
    for i, vrstica in enumerate(f):
        if i >= n:
            break
        rez += vrstica
    return rez

def datoteka_info(pot):
    podatki = {}
    if not os.path.isfile(pot):
        print("'{0}' ni datoteka.", pot)
        return None
    mapa, ime = os.path.split(pot)
    velikost = os.path.getsize(pot)
    _, koncnica = os.path.splitext(pot)
    
    return """---------------
Ime: {0}
Mapa: {1}
Končnica: {2}
Velikost: {3}B
Vsebina:
{4}...""".format(ime, mapa, koncnica, velikost, nekaj_vrstic(pot))

def preglej_tekstovne(mapa, ext=".txt"):
    for pot, mape, datoteke in os.walk(mapa):
        for dat in datoteke:
            _, koncnica = os.path.splitext(dat)
            if koncnica.lower() == ext:
                print(datoteka_info(os.path.join(pot, dat)))
